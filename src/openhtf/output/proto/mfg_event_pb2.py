# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openhtf/output/proto/mfg_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from openhtf.output.proto import assembly_event_pb2 as openhtf_dot_output_dot_proto_dot_assembly__event__pb2
from openhtf.output.proto import test_runs_pb2 as openhtf_dot_output_dot_proto_dot_test__runs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='openhtf/output/proto/mfg_event.proto',
  package='openhtf',
  syntax='proto2',
  serialized_pb=_b('\n$openhtf/output/proto/mfg_event.proto\x12\x07openhtf\x1a)openhtf/output/proto/assembly_event.proto\x1a$openhtf/output/proto/test_runs.proto\"\xb4\x05\n\x08MfgEvent\x12\x14\n\ndut_serial\x18\x01 \x01(\tH\x00\x12&\n\x03lot\x18\x02 \x01(\x0b\x32\x17.openhtf.MfgEvent.ByLotH\x00\x12\x15\n\rstart_time_ms\x18\x03 \x02(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x04 \x01(\x03\x12\x13\n\x0btester_name\x18\x05 \x02(\t\x12\x11\n\ttest_name\x18\x06 \x02(\t\x12\x14\n\x0ctest_version\x18\x14 \x01(\t\x12\x18\n\x10test_description\x18\x15 \x01(\t\x12\x15\n\rtest_run_name\x18\x16 \x01(\t\x12-\n\x0btest_status\x18\x08 \x02(\x0e\x32\x0f.openhtf.Status:\x07\x43REATED\x12/\n\x0f\x61ssembly_events\x18\n \x03(\x0b\x32\x16.openhtf.AssemblyEvent\x12 \n\x07timings\x18\x0b \x03(\x0b\x32\x0f.openhtf.Timing\x12\x1e\n\x06phases\x18\x0c \x03(\x0b\x32\x0e.openhtf.Phase\x12\x17\n\x0f\x66ramework_build\x18\r \x01(\t\x12)\n\x0bmeasurement\x18\x0e \x03(\x0b\x32\x14.openhtf.Measurement\x12,\n\nattachment\x18\x0f \x03(\x0b\x32\x18.openhtf.EventAttachment\x12-\n\ttest_logs\x18\x10 \x03(\x0b\x32\x1a.openhtf.TestRunLogMessage\x12+\n\rfailure_codes\x18\x11 \x03(\x0b\x32\x14.openhtf.FailureCode\x12\x15\n\roperator_name\x18\x12 \x01(\t\x12\x11\n\tpart_tags\x18\x13 \x03(\t\x1a.\n\x05\x42yLot\x12\x12\n\nlot_number\x18\x01 \x02(\t\x12\x11\n\tlot_index\x18\x02 \x01(\tB\x05\n\x03\x64ut\"\xa6\x03\n\x0bMeasurement\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1f\n\x06status\x18\x02 \x01(\x0e\x32\x0f.openhtf.Status\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x11\n\timportant\x18\x12 \x01(\x08\x12\x15\n\rparameter_tag\x18\x10 \x03(\t\x12\x15\n\rnumeric_value\x18\x0b \x01(\x01\x12\x17\n\x0fnumeric_minimum\x18\x0c \x01(\x01\x12\x17\n\x0fnumeric_maximum\x18\r \x01(\x01\x12\x12\n\ntext_value\x18\x0e \x01(\t\x12\x15\n\rexpected_text\x18\x0f \x01(\t\x12\x13\n\x0bis_optional\x18\x11 \x01(\x08\x12\x17\n\x0fset_time_millis\x18\x13 \x01(\x03\x12*\n\tunit_code\x18\x14 \x01(\x0e\x32\x17.openhtf.Units.UnitCode\x12\x18\n\x10\x63ustom_unit_code\x18\x16 \x01(\t\x12\x1a\n\x12\x63ustom_unit_suffix\x18\x17 \x01(\t\x12\x1d\n\x15\x61ssociated_attachment\x18\x15 \x01(\t*\x06\x08\x88\'\x10\xd0(\"\xc4\x01\n\x0f\x45ventAttachment\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x14\n\x0cvalue_binary\x18\x02 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x17\n\x0fset_time_millis\x18\x04 \x01(\x03\x12\x15\n\rparameter_tag\x18\x05 \x03(\t\x12\'\n\x04type\x18\x06 \x01(\x0e\x32\x17.openhtf.InformationTagH\x00\x12\x13\n\tmime_type\x18\x07 \x01(\tH\x00\x42\n\n\x08\x64\x61tatype')
  ,
  dependencies=[openhtf_dot_output_dot_proto_dot_assembly__event__pb2.DESCRIPTOR,openhtf_dot_output_dot_proto_dot_test__runs__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MFGEVENT_BYLOT = _descriptor.Descriptor(
  name='ByLot',
  full_name='openhtf.MfgEvent.ByLot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lot_number', full_name='openhtf.MfgEvent.ByLot.lot_number', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lot_index', full_name='openhtf.MfgEvent.ByLot.lot_index', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=770,
  serialized_end=816,
)

_MFGEVENT = _descriptor.Descriptor(
  name='MfgEvent',
  full_name='openhtf.MfgEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dut_serial', full_name='openhtf.MfgEvent.dut_serial', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lot', full_name='openhtf.MfgEvent.lot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='openhtf.MfgEvent.start_time_ms', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time_ms', full_name='openhtf.MfgEvent.end_time_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tester_name', full_name='openhtf.MfgEvent.tester_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_name', full_name='openhtf.MfgEvent.test_name', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_version', full_name='openhtf.MfgEvent.test_version', index=6,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_description', full_name='openhtf.MfgEvent.test_description', index=7,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_run_name', full_name='openhtf.MfgEvent.test_run_name', index=8,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_status', full_name='openhtf.MfgEvent.test_status', index=9,
      number=8, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assembly_events', full_name='openhtf.MfgEvent.assembly_events', index=10,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timings', full_name='openhtf.MfgEvent.timings', index=11,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phases', full_name='openhtf.MfgEvent.phases', index=12,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='framework_build', full_name='openhtf.MfgEvent.framework_build', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='measurement', full_name='openhtf.MfgEvent.measurement', index=14,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attachment', full_name='openhtf.MfgEvent.attachment', index=15,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_logs', full_name='openhtf.MfgEvent.test_logs', index=16,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failure_codes', full_name='openhtf.MfgEvent.failure_codes', index=17,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator_name', full_name='openhtf.MfgEvent.operator_name', index=18,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='part_tags', full_name='openhtf.MfgEvent.part_tags', index=19,
      number=19, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MFGEVENT_BYLOT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='dut', full_name='openhtf.MfgEvent.dut',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=131,
  serialized_end=823,
)


_MEASUREMENT = _descriptor.Descriptor(
  name='Measurement',
  full_name='openhtf.Measurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openhtf.Measurement.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='openhtf.Measurement.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='openhtf.Measurement.description', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='important', full_name='openhtf.Measurement.important', index=3,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_tag', full_name='openhtf.Measurement.parameter_tag', index=4,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='openhtf.Measurement.numeric_value', index=5,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_minimum', full_name='openhtf.Measurement.numeric_minimum', index=6,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numeric_maximum', full_name='openhtf.Measurement.numeric_maximum', index=7,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text_value', full_name='openhtf.Measurement.text_value', index=8,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expected_text', full_name='openhtf.Measurement.expected_text', index=9,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_optional', full_name='openhtf.Measurement.is_optional', index=10,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_time_millis', full_name='openhtf.Measurement.set_time_millis', index=11,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_code', full_name='openhtf.Measurement.unit_code', index=12,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_unit_code', full_name='openhtf.Measurement.custom_unit_code', index=13,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_unit_suffix', full_name='openhtf.Measurement.custom_unit_suffix', index=14,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='associated_attachment', full_name='openhtf.Measurement.associated_attachment', index=15,
      number=21, type=9, cpp_type=9, label=1,
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
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(5000, 5200), ],
  oneofs=[
  ],
  serialized_start=826,
  serialized_end=1248,
)


_EVENTATTACHMENT = _descriptor.Descriptor(
  name='EventAttachment',
  full_name='openhtf.EventAttachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='openhtf.EventAttachment.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_binary', full_name='openhtf.EventAttachment.value_binary', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='openhtf.EventAttachment.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_time_millis', full_name='openhtf.EventAttachment.set_time_millis', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_tag', full_name='openhtf.EventAttachment.parameter_tag', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='openhtf.EventAttachment.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='openhtf.EventAttachment.mime_type', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='datatype', full_name='openhtf.EventAttachment.datatype',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1251,
  serialized_end=1447,
)

_MFGEVENT_BYLOT.containing_type = _MFGEVENT
_MFGEVENT.fields_by_name['lot'].message_type = _MFGEVENT_BYLOT
_MFGEVENT.fields_by_name['test_status'].enum_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._STATUS
_MFGEVENT.fields_by_name['assembly_events'].message_type = openhtf_dot_output_dot_proto_dot_assembly__event__pb2._ASSEMBLYEVENT
_MFGEVENT.fields_by_name['timings'].message_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._TIMING
_MFGEVENT.fields_by_name['phases'].message_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._PHASE
_MFGEVENT.fields_by_name['measurement'].message_type = _MEASUREMENT
_MFGEVENT.fields_by_name['attachment'].message_type = _EVENTATTACHMENT
_MFGEVENT.fields_by_name['test_logs'].message_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._TESTRUNLOGMESSAGE
_MFGEVENT.fields_by_name['failure_codes'].message_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._FAILURECODE
_MFGEVENT.oneofs_by_name['dut'].fields.append(
  _MFGEVENT.fields_by_name['dut_serial'])
_MFGEVENT.fields_by_name['dut_serial'].containing_oneof = _MFGEVENT.oneofs_by_name['dut']
_MFGEVENT.oneofs_by_name['dut'].fields.append(
  _MFGEVENT.fields_by_name['lot'])
_MFGEVENT.fields_by_name['lot'].containing_oneof = _MFGEVENT.oneofs_by_name['dut']
_MEASUREMENT.fields_by_name['status'].enum_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._STATUS
_MEASUREMENT.fields_by_name['unit_code'].enum_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._UNITS_UNITCODE
_EVENTATTACHMENT.fields_by_name['type'].enum_type = openhtf_dot_output_dot_proto_dot_test__runs__pb2._INFORMATIONTAG
_EVENTATTACHMENT.oneofs_by_name['datatype'].fields.append(
  _EVENTATTACHMENT.fields_by_name['type'])
_EVENTATTACHMENT.fields_by_name['type'].containing_oneof = _EVENTATTACHMENT.oneofs_by_name['datatype']
_EVENTATTACHMENT.oneofs_by_name['datatype'].fields.append(
  _EVENTATTACHMENT.fields_by_name['mime_type'])
_EVENTATTACHMENT.fields_by_name['mime_type'].containing_oneof = _EVENTATTACHMENT.oneofs_by_name['datatype']
DESCRIPTOR.message_types_by_name['MfgEvent'] = _MFGEVENT
DESCRIPTOR.message_types_by_name['Measurement'] = _MEASUREMENT
DESCRIPTOR.message_types_by_name['EventAttachment'] = _EVENTATTACHMENT

MfgEvent = _reflection.GeneratedProtocolMessageType('MfgEvent', (_message.Message,), dict(

  ByLot = _reflection.GeneratedProtocolMessageType('ByLot', (_message.Message,), dict(
    DESCRIPTOR = _MFGEVENT_BYLOT,
    __module__ = 'openhtf.output.proto.mfg_event_pb2'
    # @@protoc_insertion_point(class_scope:openhtf.MfgEvent.ByLot)
    ))
  ,
  DESCRIPTOR = _MFGEVENT,
  __module__ = 'openhtf.output.proto.mfg_event_pb2'
  # @@protoc_insertion_point(class_scope:openhtf.MfgEvent)
  ))
_sym_db.RegisterMessage(MfgEvent)
_sym_db.RegisterMessage(MfgEvent.ByLot)

Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), dict(
  DESCRIPTOR = _MEASUREMENT,
  __module__ = 'openhtf.output.proto.mfg_event_pb2'
  # @@protoc_insertion_point(class_scope:openhtf.Measurement)
  ))
_sym_db.RegisterMessage(Measurement)

EventAttachment = _reflection.GeneratedProtocolMessageType('EventAttachment', (_message.Message,), dict(
  DESCRIPTOR = _EVENTATTACHMENT,
  __module__ = 'openhtf.output.proto.mfg_event_pb2'
  # @@protoc_insertion_point(class_scope:openhtf.EventAttachment)
  ))
_sym_db.RegisterMessage(EventAttachment)


# @@protoc_insertion_point(module_scope)