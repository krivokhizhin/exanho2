import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from itertools import islice
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


class GeneratedsSuper(object):
    __slots__ = ['gds_collector_', 'gds_elementtree_node_', 'original_tagname_', 'parent_object_', 'ns_prefix_']
    __hash__ = object.__hash__
    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
    class _FixedOffsetTZ(datetime_.tzinfo):
        def __init__(self, offset, name):
            self.__offset = datetime_.timedelta(minutes=offset)
            self.__name = name
        def utcoffset(self, dt):
            return self.__offset
        def tzname(self, dt):
            return self.__name
        def dst(self, dt):
            return None
    @staticmethod
    def gds_subclass_slots(member_data_items):
        slots = []
        for member in member_data_items:
            slots.append(member)
            slots.append("%s_nsprefix_" % member)
        return slots
    def gds_format_string(self, input_data, input_name=''):
        return input_data
    def gds_parse_string(self, input_data, node=None, input_name=''):
        return input_data
    def gds_validate_string(self, input_data, node=None, input_name=''):
        if not input_data:
            return ''
        else:
            return input_data
    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data)
    def gds_validate_base64(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data
    def gds_parse_integer(self, input_data, node=None, input_name=''):
        try:
            ival = int(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires integer value: %s' % exp)
        return ival
    def gds_validate_integer(self, input_data, node=None, input_name=''):
        try:
            value = int(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires integer value')
        return value
    def gds_format_integer_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_integer_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                int(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of integer values')
        return values
    def gds_format_float(self, input_data, input_name=''):
        return ('%.15f' % input_data).rstrip('0')
    def gds_parse_float(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires float or double value: %s' % exp)
        return fval_
    def gds_validate_float(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires float value')
        return value
    def gds_format_float_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_float_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of float values')
        return values
    def gds_format_decimal(self, input_data, input_name=''):
        return_value = '%s' % input_data
        if '.' in return_value:
            return_value = return_value.rstrip('0')
            if return_value.endswith('.'):
                return_value = return_value.rstrip('.')
        return return_value
    def gds_parse_decimal(self, input_data, node=None, input_name=''):
        try:
            decimal_value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return decimal_value
    def gds_validate_decimal(self, input_data, node=None, input_name=''):
        try:
            value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return value
    def gds_format_decimal_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return ' '.join([self.gds_format_decimal(item) for item in input_data])
    def gds_validate_decimal_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                decimal_.Decimal(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of decimal values')
        return values
    def gds_format_double(self, input_data, input_name=''):
        return '%s' % input_data
    def gds_parse_double(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires double or float value: %s' % exp)
        return fval_
    def gds_validate_double(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires double or float value')
        return value
    def gds_format_double_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_double_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(
                    node, 'Requires sequence of double or float values')
        return values
    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()
    def gds_parse_boolean(self, input_data, node=None, input_name=''):
        if input_data in ('true', '1'):
            bval = True
        elif input_data in ('false', '0'):
            bval = False
        else:
            raise_parse_error(node, 'Requires boolean value')
        return bval
    def gds_validate_boolean(self, input_data, node=None, input_name=''):
        if input_data not in (True, 1, False, 0, ):
            raise_parse_error(
                node,
                'Requires boolean value '
                '(one of True, 1, False, 0)')
        return input_data
    def gds_format_boolean_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_boolean_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires sequence of boolean values '
                    '(one of True, 1, False, 0)')
        return values
    def gds_validate_datetime(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_datetime(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    @classmethod
    def gds_parse_datetime(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        time_parts = input_data.split('.')
        if len(time_parts) > 1:
            micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
            input_data = '%s.%s' % (
                time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt
    def gds_validate_date(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_date(self, input_data, input_name=''):
        _svalue = '%04d-%02d-%02d' % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(
                            hours, minutes)
        except AttributeError:
            pass
        return _svalue
    @classmethod
    def gds_parse_date(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
        dt = dt.replace(tzinfo=tz)
        return dt.date()
    def gds_validate_time(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_time(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%02d:%02d:%02d' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%02d:%02d:%02d.%s' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue
    def gds_validate_simple_patterns(self, patterns, target):
        # pat is a list of lists of strings/patterns.
        # The target value must match at least one of the patterns
        # in order for the test to succeed.
        if not isinstance(target, str):
            target = str(target)
        found1 = True
        for patterns1 in patterns:
            found2 = False
            for patterns2 in patterns1:
                mo = re_.search(patterns2, target)
                if mo is not None and len(mo.group(0)) == len(target):
                    found2 = True
                    break
            if not found2:
                found1 = False
                break
        return found1
    @classmethod
    def gds_parse_time(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt.time()
    def gds_check_cardinality_(
            self, value, input_name,
            min_occurs=0, max_occurs=1, required=None):
        if value is None:
            length = 0
        elif isinstance(value, list):
            length = len(value)
        else:
            length = 1
        if required is not None :
            if required and length < 1:
                self.gds_collector_.add_message(
                    "Required value {}{} is missing".format(
                        input_name, self.gds_get_node_lineno_()))
        if length < min_occurs:
            self.gds_collector_.add_message(
                "Number of values for {}{} is below "
                "the minimum allowed, "
                "expected at least {}, found {}".format(
                    input_name, self.gds_get_node_lineno_(),
                    min_occurs, length))
        elif length > max_occurs:
            self.gds_collector_.add_message(
                "Number of values for {}{} is above "
                "the maximum allowed, "
                "expected at most {}, found {}".format(
                    input_name, self.gds_get_node_lineno_(),
                    max_occurs, length))
    def gds_validate_builtin_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value, input_name=input_name)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_validate_defined_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_str_lower(self, instring):
        return instring.lower()
    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path
    Tag_strip_pattern_ = re_.compile(r'\{.*\}')
    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)
    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1
    def gds_build_any(self, node, type_name=None):
        # provide default value in case option --disable-xml is used.
        content = ""
        content = etree_.tostring(node, encoding="unicode")
        return content
    @classmethod
    def gds_reverse_node_mapping(cls, mapping):
        return dict(((v, k) for k, v in mapping.items()))
    @staticmethod
    def gds_encode(instring):
        if sys.version_info.major == 2:
            if ExternalEncoding:
                encoding = ExternalEncoding
            else:
                encoding = 'utf-8'
            return instring.encode(encoding)
        else:
            return instring
    @staticmethod
    def convert_unicode(instring):
        if isinstance(instring, str):
            result = quote_xml(instring)
        elif sys.version_info.major == 2 and isinstance(instring, unicode):
            result = quote_xml(instring).encode('utf8')
        else:
            result = GeneratedsSuper.gds_encode(str(instring))
        return result
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        mro = self.__class__.__mro__
        return all(
            getattr(self, attribute) == getattr(other, attribute)
            for cls in islice(mro, 0, len(mro) - 2)
            for attribute in cls.member_data_items_)
    def __ne__(self, other):
        return not self.__eq__(other)
    # Django ETL transform hooks.
    def gds_djo_etl_transform(self):
        pass
    def gds_djo_etl_transform_db_obj(self, dbobj):
        pass
    # SQLAlchemy ETL transform hooks.
    def gds_sqa_etl_transform(self):
        return 0, None
    def gds_sqa_etl_transform_db_obj(self, dbobj):
        pass
    def gds_get_node_lineno_(self):
        if (hasattr(self, "gds_elementtree_node_") and
                self.gds_elementtree_node_ is not None):
            return ' near line {}'.format(
                self.gds_elementtree_node_.sourceline)
        else:
            return ""

    def get_xml_tag(self):
        return self.gds_elementtree_node_.tag

    def get_children(self):
        for child_name in self.__class__.member_data_items_.keys():
            if not hasattr(self, child_name):
                continue

            child_attr = getattr(self, child_name)
            if child_attr is None or not child_attr:
                continue

            try:
                for child in iter(child_attr):
                    yield child
            except TypeError:
                yield child_attr


def getSubclassFromModule_(module, class_):
    '''Get the subclass of a class from a specific module.'''
    name = class_.__name__ + 'Sub'
    if hasattr(module, name):
        return getattr(module, name)
    else:
        return None

