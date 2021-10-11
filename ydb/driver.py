# -*- coding: utf-8 -*-
import ydb

from . import credentials as credentials_impl, table, scheme, pool, auth_helpers
import six
import os


_grpcs_protocol = 'grpcs://'
_grpc_protocol = 'grpc://'


def is_secure_protocol(endpoint):
    return endpoint.startswith('grpcs://')


def wrap_endpoint(endpoint):
    if endpoint.startswith(_grpcs_protocol):
        return endpoint[len(_grpcs_protocol):]
    if endpoint.startswith(_grpc_protocol):
        return endpoint[len(_grpc_protocol):]
    return endpoint


def parse_connection_string(connection_string):
    cs = connection_string
    if not cs.startswith(_grpc_protocol) and not cs.startswith(_grpcs_protocol):
        # default is grpcs
        cs = _grpcs_protocol + cs

    p = six.moves.urllib.parse.urlparse(connection_string)
    b = six.moves.urllib.parse.parse_qs(p.query)
    database = b.get('database', [])
    assert len(database) > 0

    return p.scheme + "://" + p.netloc , database[0]


def default_credentials(credentials=None, tracer=None):
    tracer = tracer if tracer is not None else ydb.Tracer(None)
    with tracer.trace("Driver.default_credentials") as ctx:
        if credentials is not None:
            ctx.trace({"credentials.prepared": True})
            return credentials

        service_account_key_file = os.getenv("YDB_SERVICE_ACCOUNT_KEY_FILE_CREDENTIALS")
        if service_account_key_file is not None:
            ctx.trace({"credentials.service_account_key_file": True})
            from kikimr.public.sdk.python import iam
            return iam.ServiceAccountCredentials.from_file(service_account_key_file)

        anonymous_credetials = os.getenv("YDB_ANONYMOUS_CREDENTIALS", "0") == "1"
        if anonymous_credetials:
            ctx.trace({"credentials.anonymous": True})
            return credentials_impl.AnonymousCredentials()

        metadata_credentials = os.getenv("YDB_METADATA_CREDENTIALS", "0") == "1"
        if metadata_credentials:
            ctx.trace({"credentials.metadata": True})
            from kikimr.public.sdk.python import iam
            return iam.MetadataUrlCredentials(tracer=tracer)

        access_token = os.getenv("YDB_ACCESS_TOKEN_CREDENTIALS")
        if access_token is not None:
            ctx.trace({"credentials.access_token": True})
            return credentials_impl.AuthTokenCredentials(access_token)

        # (legacy instantiation)
        creds = auth_helpers.construct_credentials_from_environ()
        if creds is not None:
            ctx.trace({"credentials.legacy_instantiation": True})
            return creds

        from kikimr.public.sdk.python import iam
        return iam.MetadataUrlCredentials(tracer=tracer)


class DriverConfig(object):
    __slots__ = ('endpoint', 'database', 'ca_cert', 'channel_options', 'credentials', 'use_all_nodes',
                 'root_certificates', 'certificate_chain', 'private_key', 'grpc_keep_alive_timeout', 'secure_channel',
                 'table_client_settings', 'endpoints', 'primary_user_agent', 'tracer')

    def __init__(
            self, endpoint, database=None, ca_cert=None, auth_token=None,
            channel_options=None, credentials=None, use_all_nodes=False,
            root_certificates=None, certificate_chain=None, private_key=None,
            grpc_keep_alive_timeout=None, table_client_settings=None, endpoints=None,
            primary_user_agent='python-library', tracer=None):
        # type:(str, str, str, str, Any, ydb.Credentials, bool, bytes, bytes, bytes, float, ydb.TableClientSettings, list, str, ydb.Tracer) -> None
        """
        A driver config to initialize a driver instance

        :param endpoint: A endpoint specified in pattern host:port to be used for initial channel initialization and for YDB endpoint discovery mechanism
        :param database: A name of the database
        :param ca_cert: A CA certificate when SSL should be used
        :param auth_token: A authentication token
        :param credentials: An instance of AbstractCredentials
        :param use_all_nodes: A balancing policy that forces to use all available nodes.
        :param root_certificates: The PEM-encoded root certificates as a byte string.
        :param private_key: The PEM-encoded private key as a byte string, or None if no\
        private key should be used.
        :param certificate_chain: The PEM-encoded certificate chain as a byte string\
        to use or or None if no certificate chain should be used.
        :param grpc_keep_alive_timeout: GRpc KeepAlive timeout, ms
        :param ydb.Tracer tracer: ydb.Tracer instance to trace requests in driver.\
        If tracing aio ScopeManager must be ContextVarsScopeManager

        """
        self.endpoint = endpoint
        self.database = database
        self.ca_cert = ca_cert
        self.channel_options = channel_options
        self.secure_channel = is_secure_protocol(endpoint)
        self.endpoint = wrap_endpoint(self.endpoint)
        self.endpoints = []
        if endpoints is not None:
            self.endpoints = [wrap_endpoint(endp) for endp in endpoints]
        if auth_token is not None:
            credentials = credentials_impl.AuthTokenCredentials(auth_token)
        self.credentials = credentials
        self.use_all_nodes = use_all_nodes
        self.root_certificates = root_certificates
        self.certificate_chain = certificate_chain
        self.private_key = private_key
        self.grpc_keep_alive_timeout = grpc_keep_alive_timeout
        self.table_client_settings = table_client_settings
        self.primary_user_agent = primary_user_agent
        self.tracer = tracer if tracer is not None else ydb.Tracer(None)

    def set_database(self, database):
        self.database = database
        return self

    @classmethod
    def default_from_endpoint_and_database(cls, endpoint, database, root_certificates=None, credentials=None, **kwargs):
        return cls(
            endpoint,
            database,
            credentials=default_credentials(credentials),
            root_certificates=root_certificates,
            **kwargs
        )

    @classmethod
    def default_from_connection_string(cls, connection_string, root_certificates=None, credentials=None, **kwargs):
        endpoint, database = parse_connection_string(connection_string)
        return cls(
            endpoint,
            database,
            credentials=default_credentials(credentials),
            root_certificates=root_certificates,
            **kwargs
        )

    def set_grpc_keep_alive_timeout(self, timeout):
        self.grpc_keep_alive_timeout = timeout
        return self


ConnectionParams = DriverConfig


def get_config(
    driver_config=None,
    connection_string=None,
    endpoint=None,
    database=None,
    root_certificates=None,
    credentials=None,
    config_class=DriverConfig,
    **kwargs
):
    if driver_config is None:
        if connection_string is not None:
            driver_config = config_class.default_from_connection_string(connection_string, root_certificates,
                                                                        credentials, **kwargs)
        else:
            driver_config = config_class.default_from_endpoint_and_database(endpoint, database, root_certificates,
                                                                            credentials, **kwargs)
        return driver_config
    return driver_config


class Driver(pool.ConnectionPool):
    __slots__ = ('scheme_client', 'table_client')

    def __init__(self, driver_config=None, connection_string=None, endpoint=None, database=None, root_certificates=None, credentials=None, **kwargs):
        # type:(DriverConfig, str, str, str, bytes, ydb.AbstractCredentials, **Any) -> None

        """
        Constructs a driver instance to be used in table and scheme clients.
        It encapsulates endpoints discovery mechanism and provides ability to execute RPCs
        on discovered endpoints

        :param driver_config: A driver config
        :param connection_string: A string in the following format: <protocol>://<hostame>:<port>/?database=/path/to/the/database
        :param endpoint: An endpoint specified in the following format: <protocol>://<hostame>:<port>
        :param database: A database path
        :param credentials: A credentials. If not specifed credentials constructed by default.
        """
        driver_config = get_config(driver_config, connection_string, endpoint, database, root_certificates, credentials)

        super(Driver, self).__init__(driver_config)
        self.scheme_client = scheme.SchemeClient(self)
        self.table_client = table.TableClient(self, driver_config.table_client_settings)
