# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openhtf/output/proto/guzzle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='openhtf/output/proto/guzzle.proto',
  package='openhtf',
  syntax='proto2',
  serialized_pb=_b('\n!openhtf/output/proto/guzzle.proto\x12\x07openhtf\"N\n\x0fTestRunEnvelope\x12*\n\x0cpayload_type\x18\x02 \x01(\x0e\x32\x14.openhtf.PayloadType\x12\x0f\n\x07payload\x18\x03 \x01(\x0c*S\n\x0bPayloadType\x12\x17\n\x13\x43OMPRESSED_TEST_RUN\x10\x01\x12\x13\n\x0f\x43OMPRESSED_VARZ\x10\x02\x12\x16\n\x12\x43OMPRESSED_LOGFILE\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PAYLOADTYPE = _descriptor.EnumDescriptor(
  name='PayloadType',
  full_name='openhtf.PayloadType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMPRESSED_TEST_RUN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPRESSED_VARZ', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPRESSED_LOGFILE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=126,
  serialized_end=209,
)
_sym_db.RegisterEnumDescriptor(_PAYLOADTYPE)

PayloadType = enum_type_wrapper.EnumTypeWrapper(_PAYLOADTYPE)
COMPRESSED_TEST_RUN = 1
COMPRESSED_VARZ = 2
COMPRESSED_LOGFILE = 3



_TESTRUNENVELOPE = _descriptor.Descriptor(
  name='TestRunEnvelope',
  full_name='openhtf.TestRunEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='openhtf.TestRunEnvelope.payload_type', index=0,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='openhtf.TestRunEnvelope.payload', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=124,
)

_TESTRUNENVELOPE.fields_by_name['payload_type'].enum_type = _PAYLOADTYPE
DESCRIPTOR.message_types_by_name['TestRunEnvelope'] = _TESTRUNENVELOPE
DESCRIPTOR.enum_types_by_name['PayloadType'] = _PAYLOADTYPE

TestRunEnvelope = _reflection.GeneratedProtocolMessageType('TestRunEnvelope', (_message.Message,), dict(
  DESCRIPTOR = _TESTRUNENVELOPE,
  __module__ = 'openhtf.output.proto.guzzle_pb2'
  # @@protoc_insertion_point(class_scope:openhtf.TestRunEnvelope)
  ))
_sym_db.RegisterMessage(TestRunEnvelope)


# @@protoc_insertion_point(module_scope)
