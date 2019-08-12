# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openhtf/output/proto/assembly_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='openhtf/output/proto/assembly_event.proto',
  package='openhtf',
  syntax='proto3',
  serialized_pb=_b('\n)openhtf/output/proto/assembly_event.proto\x12\x07openhtf\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xb9\x04\n\rAssemblyEvent\x12\x30\n\x06target\x18\x01 \x01(\x0b\x32 .openhtf.AssemblyEvent.Component\x12/\n\x05\x63hild\x18\x03 \x01(\x0b\x32 .openhtf.AssemblyEvent.Component\x12,\n\x02op\x18\x04 \x01(\x0e\x32 .openhtf.AssemblyEvent.Operation\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x96\x02\n\tComponent\x12\x13\n\x0bpart_number\x18\x01 \x01(\t\x12\x10\n\x06serial\x18\x02 \x01(\tH\x00\x12\x35\n\x03lot\x18\x03 \x01(\x0b\x32&.openhtf.AssemblyEvent.Component.ByLotH\x00\x12\x19\n\x11\x65lectronic_serial\x18\x04 \x01(\t\x12\x15\n\rinstance_name\x18\x05 \x01(\t\x12+\n\nextra_data\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x16\n\x0e\x64\x65viation_code\x18\x07 \x03(\t\x1a.\n\x05\x42yLot\x12\x12\n\nlot_number\x18\x01 \x01(\t\x12\x11\n\tlot_index\x18\x02 \x01(\tB\x04\n\x02id\"T\n\tOperation\x12\n\n\x06\x41TTACH\x10\x00\x12\n\n\x06\x44\x45TACH\x10\x01\x12\n\n\x06\x43REATE\x10\x02\x12\n\n\x06UPDATE\x10\x03\x12\x17\n\x13\x44\x45TACH_ALL_CHILDREN\x10\x04\"\x89\x02\n\x13StaticComponentInfo\x12\x1f\n\x17\x65xtraction_timestamp_ms\x18\x01 \x01(\x03\x12!\n\x19modification_timestamp_ms\x18\x02 \x01(\x03\x12\x0e\n\x06serial\x18\x03 \x01(\t\x12\x13\n\x0bpart_number\x18\x04 \x01(\t\x12\x15\n\rinstance_name\x18\x05 \x01(\t\x12\x12\n\ndeviations\x18\x06 \x03(\t\x12\x14\n\x0cupdate_count\x18\x07 \x01(\x03\x12\x33\n\tcomponent\x18\x08 \x01(\x0b\x32 .openhtf.AssemblyEvent.Component\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ASSEMBLYEVENT_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='openhtf.AssemblyEvent.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATTACH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DETACH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DETACH_ALL_CHILDREN', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=603,
  serialized_end=687,
)
_sym_db.RegisterEnumDescriptor(_ASSEMBLYEVENT_OPERATION)


_ASSEMBLYEVENT_COMPONENT_BYLOT = _descriptor.Descriptor(
  name='ByLot',
  full_name='openhtf.AssemblyEvent.Component.ByLot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lot_number', full_name='openhtf.AssemblyEvent.Component.ByLot.lot_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lot_index', full_name='openhtf.AssemblyEvent.Component.ByLot.lot_index', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=549,
  serialized_end=595,
)

_ASSEMBLYEVENT_COMPONENT = _descriptor.Descriptor(
  name='Component',
  full_name='openhtf.AssemblyEvent.Component',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='part_number', full_name='openhtf.AssemblyEvent.Component.part_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial', full_name='openhtf.AssemblyEvent.Component.serial', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lot', full_name='openhtf.AssemblyEvent.Component.lot', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='electronic_serial', full_name='openhtf.AssemblyEvent.Component.electronic_serial', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='openhtf.AssemblyEvent.Component.instance_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extra_data', full_name='openhtf.AssemblyEvent.Component.extra_data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviation_code', full_name='openhtf.AssemblyEvent.Component.deviation_code', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ASSEMBLYEVENT_COMPONENT_BYLOT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='id', full_name='openhtf.AssemblyEvent.Component.id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=323,
  serialized_end=601,
)

_ASSEMBLYEVENT = _descriptor.Descriptor(
  name='AssemblyEvent',
  full_name='openhtf.AssemblyEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='openhtf.AssemblyEvent.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='child', full_name='openhtf.AssemblyEvent.child', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op', full_name='openhtf.AssemblyEvent.op', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='openhtf.AssemblyEvent.time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ASSEMBLYEVENT_COMPONENT, ],
  enum_types=[
    _ASSEMBLYEVENT_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=687,
)


_STATICCOMPONENTINFO = _descriptor.Descriptor(
  name='StaticComponentInfo',
  full_name='openhtf.StaticComponentInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='extraction_timestamp_ms', full_name='openhtf.StaticComponentInfo.extraction_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modification_timestamp_ms', full_name='openhtf.StaticComponentInfo.modification_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial', full_name='openhtf.StaticComponentInfo.serial', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='part_number', full_name='openhtf.StaticComponentInfo.part_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='openhtf.StaticComponentInfo.instance_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviations', full_name='openhtf.StaticComponentInfo.deviations', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_count', full_name='openhtf.StaticComponentInfo.update_count', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='component', full_name='openhtf.StaticComponentInfo.component', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='openhtf.StaticComponentInfo.description', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=955,
)

_ASSEMBLYEVENT_COMPONENT_BYLOT.containing_type = _ASSEMBLYEVENT_COMPONENT
_ASSEMBLYEVENT_COMPONENT.fields_by_name['lot'].message_type = _ASSEMBLYEVENT_COMPONENT_BYLOT
_ASSEMBLYEVENT_COMPONENT.fields_by_name['extra_data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ASSEMBLYEVENT_COMPONENT.containing_type = _ASSEMBLYEVENT
_ASSEMBLYEVENT_COMPONENT.oneofs_by_name['id'].fields.append(
  _ASSEMBLYEVENT_COMPONENT.fields_by_name['serial'])
_ASSEMBLYEVENT_COMPONENT.fields_by_name['serial'].containing_oneof = _ASSEMBLYEVENT_COMPONENT.oneofs_by_name['id']
_ASSEMBLYEVENT_COMPONENT.oneofs_by_name['id'].fields.append(
  _ASSEMBLYEVENT_COMPONENT.fields_by_name['lot'])
_ASSEMBLYEVENT_COMPONENT.fields_by_name['lot'].containing_oneof = _ASSEMBLYEVENT_COMPONENT.oneofs_by_name['id']
_ASSEMBLYEVENT.fields_by_name['target'].message_type = _ASSEMBLYEVENT_COMPONENT
_ASSEMBLYEVENT.fields_by_name['child'].message_type = _ASSEMBLYEVENT_COMPONENT
_ASSEMBLYEVENT.fields_by_name['op'].enum_type = _ASSEMBLYEVENT_OPERATION
_ASSEMBLYEVENT.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSEMBLYEVENT_OPERATION.containing_type = _ASSEMBLYEVENT
_STATICCOMPONENTINFO.fields_by_name['component'].message_type = _ASSEMBLYEVENT_COMPONENT
DESCRIPTOR.message_types_by_name['AssemblyEvent'] = _ASSEMBLYEVENT
DESCRIPTOR.message_types_by_name['StaticComponentInfo'] = _STATICCOMPONENTINFO

AssemblyEvent = _reflection.GeneratedProtocolMessageType('AssemblyEvent', (_message.Message,), dict(

  Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), dict(

    ByLot = _reflection.GeneratedProtocolMessageType('ByLot', (_message.Message,), dict(
      DESCRIPTOR = _ASSEMBLYEVENT_COMPONENT_BYLOT,
      __module__ = 'openhtf.output.proto.assembly_event_pb2'
      # @@protoc_insertion_point(class_scope:openhtf.AssemblyEvent.Component.ByLot)
      ))
    ,
    DESCRIPTOR = _ASSEMBLYEVENT_COMPONENT,
    __module__ = 'openhtf.output.proto.assembly_event_pb2'
    # @@protoc_insertion_point(class_scope:openhtf.AssemblyEvent.Component)
    ))
  ,
  DESCRIPTOR = _ASSEMBLYEVENT,
  __module__ = 'openhtf.output.proto.assembly_event_pb2'
  # @@protoc_insertion_point(class_scope:openhtf.AssemblyEvent)
  ))
_sym_db.RegisterMessage(AssemblyEvent)
_sym_db.RegisterMessage(AssemblyEvent.Component)
_sym_db.RegisterMessage(AssemblyEvent.Component.ByLot)

StaticComponentInfo = _reflection.GeneratedProtocolMessageType('StaticComponentInfo', (_message.Message,), dict(
  DESCRIPTOR = _STATICCOMPONENTINFO,
  __module__ = 'openhtf.output.proto.assembly_event_pb2'
  # @@protoc_insertion_point(class_scope:openhtf.StaticComponentInfo)
  ))
_sym_db.RegisterMessage(StaticComponentInfo)


# @@protoc_insertion_point(module_scope)