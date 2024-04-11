# -*- coding: utf-8 -*-
# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: draft/ydb_dynamic_config_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb._grpc.v3.draft.protos import ydb_dynamic_config_pb2 as draft_dot_protos_dot_ydb__dynamic__config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='draft/ydb_dynamic_config_v1.proto',
  package='Ydb.DynamicConfig.V1',
  syntax='proto3',
  serialized_options=b'\n%tech.ydb.proto.draft.dynamicconfig.v1ZBgithub.com/ydb-platform/ydb-go-genproto/draft/Ydb_DynamicConfig_V1\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!draft/ydb_dynamic_config_v1.proto\x12\x14Ydb.DynamicConfig.V1\x1a%draft/protos/ydb_dynamic_config.proto2\x81\x08\n\x14\x44ynamicConfigService\x12V\n\tSetConfig\x12#.Ydb.DynamicConfig.SetConfigRequest\x1a$.Ydb.DynamicConfig.SetConfigResponse\x12\x62\n\rReplaceConfig\x12\'.Ydb.DynamicConfig.ReplaceConfigRequest\x1a(.Ydb.DynamicConfig.ReplaceConfigResponse\x12\\\n\x0bGetMetadata\x12%.Ydb.DynamicConfig.GetMetadataRequest\x1a&.Ydb.DynamicConfig.GetMetadataResponse\x12V\n\tGetConfig\x12#.Ydb.DynamicConfig.GetConfigRequest\x1a$.Ydb.DynamicConfig.GetConfigResponse\x12Y\n\nDropConfig\x12$.Ydb.DynamicConfig.DropConfigRequest\x1a%.Ydb.DynamicConfig.DropConfigResponse\x12n\n\x11\x41\x64\x64VolatileConfig\x12+.Ydb.DynamicConfig.AddVolatileConfigRequest\x1a,.Ydb.DynamicConfig.AddVolatileConfigResponse\x12w\n\x14RemoveVolatileConfig\x12..Ydb.DynamicConfig.RemoveVolatileConfigRequest\x1a/.Ydb.DynamicConfig.RemoveVolatileConfigResponse\x12\x62\n\rGetNodeLabels\x12\'.Ydb.DynamicConfig.GetNodeLabelsRequest\x1a(.Ydb.DynamicConfig.GetNodeLabelsResponse\x12\x62\n\rResolveConfig\x12\'.Ydb.DynamicConfig.ResolveConfigRequest\x1a(.Ydb.DynamicConfig.ResolveConfigResponse\x12k\n\x10ResolveAllConfig\x12*.Ydb.DynamicConfig.ResolveAllConfigRequest\x1a+.Ydb.DynamicConfig.ResolveAllConfigResponseBn\n%tech.ydb.proto.draft.dynamicconfig.v1ZBgithub.com/ydb-platform/ydb-go-genproto/draft/Ydb_DynamicConfig_V1\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[draft_dot_protos_dot_ydb__dynamic__config__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_DYNAMICCONFIGSERVICE = _descriptor.ServiceDescriptor(
  name='DynamicConfigService',
  full_name='Ydb.DynamicConfig.V1.DynamicConfigService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=99,
  serialized_end=1124,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.SetConfig',
    index=0,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._SETCONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._SETCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReplaceConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.ReplaceConfig',
    index=1,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._REPLACECONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._REPLACECONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMetadata',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.GetMetadata',
    index=2,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._GETMETADATAREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._GETMETADATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.GetConfig',
    index=3,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._GETCONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._GETCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DropConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.DropConfig',
    index=4,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._DROPCONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._DROPCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddVolatileConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.AddVolatileConfig',
    index=5,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._ADDVOLATILECONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._ADDVOLATILECONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveVolatileConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.RemoveVolatileConfig',
    index=6,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._REMOVEVOLATILECONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._REMOVEVOLATILECONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetNodeLabels',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.GetNodeLabels',
    index=7,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._GETNODELABELSREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._GETNODELABELSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResolveConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.ResolveConfig',
    index=8,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._RESOLVECONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._RESOLVECONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ResolveAllConfig',
    full_name='Ydb.DynamicConfig.V1.DynamicConfigService.ResolveAllConfig',
    index=9,
    containing_service=None,
    input_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._RESOLVEALLCONFIGREQUEST,
    output_type=draft_dot_protos_dot_ydb__dynamic__config__pb2._RESOLVEALLCONFIGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DYNAMICCONFIGSERVICE)

DESCRIPTOR.services_by_name['DynamicConfigService'] = _DYNAMICCONFIGSERVICE

# @@protoc_insertion_point(module_scope)