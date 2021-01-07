#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jan  6 18:37:32 2021 by generateDS.py version 2.37.11.
# Python 3.7.3 (default, Jul 25 2020, 13:03:44)  [GCC 8.3.0]
#
# Command line options:
#   ('-f', '')
#   ('--one-file-per-xsd', '')
#   ('--output-directory', '/home/kks/git/exanho/exanho/eis44/ds')
#   ('--use-source-file-as-module-name', '')
#   ('--use-getter-setter', 'none')
#   ('--enable-slots', '')
#   ('--member-specs', 'dict')
#   ('--export', '')
#   ('--silence', '')
#
# Command line arguments:
#   /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/export_types.xsd
#
# Command line:
#   /home/kks/git/exanho/venv/bin/generateDS.py -f --one-file-per-xsd --output-directory="/home/kks/git/exanho/exanho/eis44/ds" --use-source-file-as-module-name --use-getter-setter="none" --enable-slots --member-specs="dict" --export --silence /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/export_types.xsd
#
# Current working directory (os.getcwd()):
#   kks
#

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


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from .generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    
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
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

from .BaseTypes import *

class attachmentListType(GeneratedsSuper):
    """Тип: Прикрепленные документы"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'attachmentInfo': MemberSpec_('attachmentInfo', 'attachmentInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'attachmentInfo', 'type': 'attachmentType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, attachmentInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if attachmentInfo is None:
            self.attachmentInfo = []
        else:
            self.attachmentInfo = attachmentInfo
        self.attachmentInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, attachmentListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if attachmentListType.subclass:
            return attachmentListType.subclass(*args_, **kwargs_)
        else:
            return attachmentListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.attachmentInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'attachmentInfo':
            class_obj_ = self.get_class_obj_(child_, attachmentType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.attachmentInfo.append(obj_)
            obj_.original_tagname_ = 'attachmentInfo'
# end class attachmentListType


class attachmentListSignCheckUrlType(GeneratedsSuper):
    """Тип: Прикрепленные документы с полем signatureCheckUrl"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'attachmentInfo': MemberSpec_('attachmentInfo', 'attachmentType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'attachmentInfo', 'type': 'attachmentInfo'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, attachmentInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if attachmentInfo is None:
            self.attachmentInfo = []
        else:
            self.attachmentInfo = attachmentInfo
        self.attachmentInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, attachmentListSignCheckUrlType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if attachmentListSignCheckUrlType.subclass:
            return attachmentListSignCheckUrlType.subclass(*args_, **kwargs_)
        else:
            return attachmentListSignCheckUrlType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.attachmentInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'attachmentInfo':
            obj_ = attachmentInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.attachmentInfo.append(obj_)
            obj_.original_tagname_ = 'attachmentInfo'
# end class attachmentListSignCheckUrlType


class attachmentListWithKindType(GeneratedsSuper):
    """Тип: Прикрепленные документы, с указанием вида"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'attachmentInfo': MemberSpec_('attachmentInfo', 'attachmentInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'attachmentInfo', 'type': 'attachmentWithKindType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, attachmentInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if attachmentInfo is None:
            self.attachmentInfo = []
        else:
            self.attachmentInfo = attachmentInfo
        self.attachmentInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, attachmentListWithKindType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if attachmentListWithKindType.subclass:
            return attachmentListWithKindType.subclass(*args_, **kwargs_)
        else:
            return attachmentListWithKindType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.attachmentInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'attachmentInfo':
            obj_ = attachmentWithKindType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.attachmentInfo.append(obj_)
            obj_.original_tagname_ = 'attachmentInfo'
# end class attachmentListWithKindType


class attachmentType(GeneratedsSuper):
    """Тип: Прикрепленный документ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'publishedContentId': MemberSpec_('publishedContentId', ['guidType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'publishedContentId', 'type': 'xs:string'}, None),
        'fileName': MemberSpec_('fileName', ['fileNameType', 'xs:string'], 0, 0, {'name': 'fileName', 'type': 'xs:string'}, None),
        'fileSize': MemberSpec_('fileSize', ['fileSizeType', 'xs:nonNegativeInteger'], 0, 1, {'minOccurs': '0', 'name': 'fileSize', 'type': 'xs:nonNegativeInteger'}, None),
        'docDescription': MemberSpec_('docDescription', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'docDescription', 'type': 'xs:string'}, None),
        'docDate': MemberSpec_('docDate', 'xs:dateTime', 0, 1, {'minOccurs': '0', 'name': 'docDate', 'type': 'xs:dateTime'}, None),
        'url': MemberSpec_('url', ['hrefType', 'xs:string'], 0, 0, {'name': 'url', 'type': 'xs:string'}, 1),
        'contentId': MemberSpec_('contentId', ['guidType', 'xs:string'], 0, 0, {'name': 'contentId', 'type': 'xs:string'}, 1),
        'content': MemberSpec_('content', ['content', 'xs:base64Binary'], 0, 0, {'name': 'content', 'type': 'xs:base64Binary'}, 1),
        'cryptoSigns': MemberSpec_('cryptoSigns', 'cryptoSigns', 0, 1, {'minOccurs': '0', 'name': 'cryptoSigns', 'type': 'cryptoSigns'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, publishedContentId=None, fileName=None, fileSize=None, docDescription=None, docDate=None, url=None, contentId=None, content=None, cryptoSigns=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publishedContentId = publishedContentId
        self.validate_guidType(self.publishedContentId)
        self.publishedContentId_nsprefix_ = None
        self.fileName = fileName
        self.validate_fileNameType(self.fileName)
        self.fileName_nsprefix_ = None
        self.fileSize = fileSize
        self.validate_fileSizeType(self.fileSize)
        self.fileSize_nsprefix_ = None
        self.docDescription = docDescription
        self.validate_text4000Type(self.docDescription)
        self.docDescription_nsprefix_ = None
        if isinstance(docDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(docDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = docDate
        self.docDate = initvalue_
        self.docDate_nsprefix_ = None
        self.url = url
        self.validate_hrefType(self.url)
        self.url_nsprefix_ = None
        self.contentId = contentId
        self.validate_guidType(self.contentId)
        self.contentId_nsprefix_ = None
        self.content = content
        self.content_nsprefix_ = None
        self.cryptoSigns = cryptoSigns
        self.cryptoSigns_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, attachmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if attachmentType.subclass:
            return attachmentType.subclass(*args_, **kwargs_)
        else:
            return attachmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_guidType(self, value):
        result = True
        # Validate type guidType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 36:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on guidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on guidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_fileNameType(self, value):
        result = True
        # Validate type fileNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1024:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on fileNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on fileNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_fileSizeType(self, value):
        result = True
        # Validate type fileSizeType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on fileSizeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_hrefType(self, value):
        result = True
        # Validate type hrefType, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (
            self.publishedContentId is not None or
            self.fileName is not None or
            self.fileSize is not None or
            self.docDescription is not None or
            self.docDate is not None or
            self.url is not None or
            self.contentId is not None or
            self.content is not None or
            self.cryptoSigns is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'publishedContentId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'publishedContentId')
            value_ = self.gds_validate_string(value_, node, 'publishedContentId')
            self.publishedContentId = value_
            self.publishedContentId_nsprefix_ = child_.prefix
            # validate type guidType
            self.validate_guidType(self.publishedContentId)
        elif nodeName_ == 'fileName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fileName')
            value_ = self.gds_validate_string(value_, node, 'fileName')
            self.fileName = value_
            self.fileName_nsprefix_ = child_.prefix
            # validate type fileNameType
            self.validate_fileNameType(self.fileName)
        elif nodeName_ == 'fileSize' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'fileSize')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'fileSize')
            self.fileSize = ival_
            self.fileSize_nsprefix_ = child_.prefix
            # validate type fileSizeType
            self.validate_fileSizeType(self.fileSize)
        elif nodeName_ == 'docDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'docDescription')
            value_ = self.gds_validate_string(value_, node, 'docDescription')
            self.docDescription = value_
            self.docDescription_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.docDescription)
        elif nodeName_ == 'docDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.docDate = dval_
            self.docDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type hrefType
            self.validate_hrefType(self.url)
        elif nodeName_ == 'contentId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contentId')
            value_ = self.gds_validate_string(value_, node, 'contentId')
            self.contentId = value_
            self.contentId_nsprefix_ = child_.prefix
            # validate type guidType
            self.validate_guidType(self.contentId)
        elif nodeName_ == 'content':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'content')
            else:
                bval_ = None
            self.content = bval_
            self.content_nsprefix_ = child_.prefix
        elif nodeName_ == 'cryptoSigns':
            obj_ = cryptoSigns.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cryptoSigns = obj_
            obj_.original_tagname_ = 'cryptoSigns'
# end class attachmentType


class content(GeneratedsSuper):
    """Содержимое файла"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, content)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if content.subclass:
            return content.subclass(*args_, **kwargs_)
        else:
            return content(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_content(self, value):
        result = True
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class content


class cryptoSigns(GeneratedsSuper):
    """Электронная подпись документа"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'signature': MemberSpec_('signature', ['signatureType', 'xs:string'], 1, 0, {'maxOccurs': 'unbounded', 'name': 'signature', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if signature is None:
            self.signature = []
        else:
            self.signature = signature
        self.signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, cryptoSigns)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if cryptoSigns.subclass:
            return cryptoSigns.subclass(*args_, **kwargs_)
        else:
            return cryptoSigns(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_signatureType(self, value):
        result = True
        # Validate type signatureType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CAdES-BES', 'CAdES-A']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on signatureType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.signature
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'signature':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'signature')
            value_ = self.gds_validate_string(value_, node, 'signature')
            self.signature.append(value_)
            self.signature_nsprefix_ = child_.prefix
            # validate type signatureType
            self.validate_signatureType(self.signature[-1])
# end class cryptoSigns


class attachmentWithKindType(GeneratedsSuper):
    """Тип: Прикрепленный документ, с указанием вида"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'publishedContentId': MemberSpec_('publishedContentId', ['guidType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'publishedContentId', 'type': 'xs:string'}, None),
        'fileName': MemberSpec_('fileName', ['fileNameType', 'xs:string'], 0, 0, {'name': 'fileName', 'type': 'xs:string'}, None),
        'fileSize': MemberSpec_('fileSize', ['fileSizeType', 'xs:nonNegativeInteger'], 0, 1, {'minOccurs': '0', 'name': 'fileSize', 'type': 'xs:nonNegativeInteger'}, None),
        'docDescription': MemberSpec_('docDescription', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'docDescription', 'type': 'xs:string'}, None),
        'docDate': MemberSpec_('docDate', 'xs:dateTime', 0, 1, {'minOccurs': '0', 'name': 'docDate', 'type': 'xs:dateTime'}, None),
        'url': MemberSpec_('url', ['hrefType', 'xs:string'], 0, 0, {'name': 'url', 'type': 'xs:string'}, 2),
        'contentId': MemberSpec_('contentId', ['guidType', 'xs:string'], 0, 0, {'name': 'contentId', 'type': 'xs:string'}, 2),
        'content': MemberSpec_('content', ['content', 'xs:base64Binary'], 0, 0, {'name': 'content', 'type': 'xs:base64Binary'}, 2),
        'docKindInfo': MemberSpec_('docKindInfo', 'documentKindRef', 0, 0, {'name': 'docKindInfo', 'type': 'documentKindRef'}, None),
        'cryptoSigns': MemberSpec_('cryptoSigns', 'cryptoSigns', 0, 1, {'minOccurs': '0', 'name': 'cryptoSigns', 'type': 'cryptoSigns'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, publishedContentId=None, fileName=None, fileSize=None, docDescription=None, docDate=None, url=None, contentId=None, content=None, docKindInfo=None, cryptoSigns=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publishedContentId = publishedContentId
        self.validate_guidType(self.publishedContentId)
        self.publishedContentId_nsprefix_ = None
        self.fileName = fileName
        self.validate_fileNameType(self.fileName)
        self.fileName_nsprefix_ = None
        self.fileSize = fileSize
        self.validate_fileSizeType(self.fileSize)
        self.fileSize_nsprefix_ = None
        self.docDescription = docDescription
        self.validate_text4000Type(self.docDescription)
        self.docDescription_nsprefix_ = None
        if isinstance(docDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(docDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = docDate
        self.docDate = initvalue_
        self.docDate_nsprefix_ = None
        self.url = url
        self.validate_hrefType(self.url)
        self.url_nsprefix_ = None
        self.contentId = contentId
        self.validate_guidType(self.contentId)
        self.contentId_nsprefix_ = None
        self.content = content
        self.content_nsprefix_ = None
        self.docKindInfo = docKindInfo
        self.docKindInfo_nsprefix_ = None
        self.cryptoSigns = cryptoSigns
        self.cryptoSigns_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, attachmentWithKindType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if attachmentWithKindType.subclass:
            return attachmentWithKindType.subclass(*args_, **kwargs_)
        else:
            return attachmentWithKindType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_guidType(self, value):
        result = True
        # Validate type guidType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 36:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on guidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on guidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_fileNameType(self, value):
        result = True
        # Validate type fileNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1024:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on fileNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on fileNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_fileSizeType(self, value):
        result = True
        # Validate type fileSizeType, a restriction on xs:nonNegativeInteger.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on fileSizeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_hrefType(self, value):
        result = True
        # Validate type hrefType, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (
            self.publishedContentId is not None or
            self.fileName is not None or
            self.fileSize is not None or
            self.docDescription is not None or
            self.docDate is not None or
            self.url is not None or
            self.contentId is not None or
            self.content is not None or
            self.docKindInfo is not None or
            self.cryptoSigns is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'publishedContentId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'publishedContentId')
            value_ = self.gds_validate_string(value_, node, 'publishedContentId')
            self.publishedContentId = value_
            self.publishedContentId_nsprefix_ = child_.prefix
            # validate type guidType
            self.validate_guidType(self.publishedContentId)
        elif nodeName_ == 'fileName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fileName')
            value_ = self.gds_validate_string(value_, node, 'fileName')
            self.fileName = value_
            self.fileName_nsprefix_ = child_.prefix
            # validate type fileNameType
            self.validate_fileNameType(self.fileName)
        elif nodeName_ == 'fileSize' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'fileSize')
            if ival_ < 0:
                raise_parse_error(child_, 'requires nonNegativeInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'fileSize')
            self.fileSize = ival_
            self.fileSize_nsprefix_ = child_.prefix
            # validate type fileSizeType
            self.validate_fileSizeType(self.fileSize)
        elif nodeName_ == 'docDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'docDescription')
            value_ = self.gds_validate_string(value_, node, 'docDescription')
            self.docDescription = value_
            self.docDescription_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.docDescription)
        elif nodeName_ == 'docDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.docDate = dval_
            self.docDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type hrefType
            self.validate_hrefType(self.url)
        elif nodeName_ == 'contentId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contentId')
            value_ = self.gds_validate_string(value_, node, 'contentId')
            self.contentId = value_
            self.contentId_nsprefix_ = child_.prefix
            # validate type guidType
            self.validate_guidType(self.contentId)
        elif nodeName_ == 'content':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'content')
            else:
                bval_ = None
            self.content = bval_
            self.content_nsprefix_ = child_.prefix
        elif nodeName_ == 'docKindInfo':
            obj_ = documentKindRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.docKindInfo = obj_
            obj_.original_tagname_ = 'docKindInfo'
        elif nodeName_ == 'cryptoSigns':
            obj_ = cryptoSigns.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cryptoSigns = obj_
            obj_.original_tagname_ = 'cryptoSigns'
# end class attachmentWithKindType


class appRejectedReasonType(GeneratedsSuper):
    """Тип: Причины отказа рассмотрения заявки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'rejectReason': MemberSpec_('rejectReason', 'rejectReasonRef', 0, 0, {'name': 'rejectReason', 'type': 'rejectReasonRef'}, None),
        'explanation': MemberSpec_('explanation', ['text2000Type', 'xs:string'], 0, 0, {'name': 'explanation', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, rejectReason=None, explanation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rejectReason = rejectReason
        self.rejectReason_nsprefix_ = None
        self.explanation = explanation
        self.validate_text2000Type(self.explanation)
        self.explanation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, appRejectedReasonType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if appRejectedReasonType.subclass:
            return appRejectedReasonType.subclass(*args_, **kwargs_)
        else:
            return appRejectedReasonType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.rejectReason is not None or
            self.explanation is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'rejectReason':
            obj_ = rejectReasonRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rejectReason = obj_
            obj_.original_tagname_ = 'rejectReason'
        elif nodeName_ == 'explanation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'explanation')
            value_ = self.gds_validate_string(value_, node, 'explanation')
            self.explanation = value_
            self.explanation_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.explanation)
# end class appRejectedReasonType


class commissionType(GeneratedsSuper):
    """Тип: Комиссии по размещению заказа (определению поставщика)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'commissionName': MemberSpec_('commissionName', ['text2000Type', 'xs:string'], 0, 0, {'name': 'commissionName', 'type': 'xs:string'}, None),
        'commissionMembers': MemberSpec_('commissionMembers', 'commissionMembers', 0, 0, {'name': 'commissionMembers', 'type': 'commissionMembers'}, None),
        'addInfo': MemberSpec_('addInfo', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'addInfo', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, commissionName=None, commissionMembers=None, addInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.commissionName = commissionName
        self.validate_text2000Type(self.commissionName)
        self.commissionName_nsprefix_ = None
        self.commissionMembers = commissionMembers
        self.commissionMembers_nsprefix_ = None
        self.addInfo = addInfo
        self.validate_text2000Type(self.addInfo)
        self.addInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, commissionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if commissionType.subclass:
            return commissionType.subclass(*args_, **kwargs_)
        else:
            return commissionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.commissionName is not None or
            self.commissionMembers is not None or
            self.addInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'commissionName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'commissionName')
            value_ = self.gds_validate_string(value_, node, 'commissionName')
            self.commissionName = value_
            self.commissionName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.commissionName)
        elif nodeName_ == 'commissionMembers':
            obj_ = commissionMembers.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.commissionMembers = obj_
            obj_.original_tagname_ = 'commissionMembers'
        elif nodeName_ == 'addInfo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'addInfo')
            value_ = self.gds_validate_string(value_, node, 'addInfo')
            self.addInfo = value_
            self.addInfo_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.addInfo)
# end class commissionType


class commissionMembers(GeneratedsSuper):
    """Участники комиссии"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'commissionMember': MemberSpec_('commissionMember', 'commissionMember', 1, 0, {'maxOccurs': 'unbounded', 'name': 'commissionMember', 'type': 'commissionMemberType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, commissionMember=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if commissionMember is None:
            self.commissionMember = []
        else:
            self.commissionMember = commissionMember
        self.commissionMember_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, commissionMembers)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if commissionMembers.subclass:
            return commissionMembers.subclass(*args_, **kwargs_)
        else:
            return commissionMembers(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.commissionMember
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'commissionMember':
            class_obj_ = self.get_class_obj_(child_, commissionMemberType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.commissionMember.append(obj_)
            obj_.original_tagname_ = 'commissionMember'
# end class commissionMembers


class commissionMemberType(GeneratedsSuper):
    """Тип: Член комиссии"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'memberNumber': MemberSpec_('memberNumber', 'xs:positiveInteger', 0, 0, {'name': 'memberNumber', 'type': 'xs:positiveInteger'}, None),
        'nameInfo': MemberSpec_('nameInfo', 'personType', 0, 0, {'name': 'nameInfo', 'type': 'personType'}, None),
        'role': MemberSpec_('role', 'role', 0, 0, {'name': 'role', 'type': 'commissionRoleType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, memberNumber=None, nameInfo=None, role=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.memberNumber = memberNumber
        self.memberNumber_nsprefix_ = None
        self.nameInfo = nameInfo
        self.nameInfo_nsprefix_ = None
        self.role = role
        self.role_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, commissionMemberType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if commissionMemberType.subclass:
            return commissionMemberType.subclass(*args_, **kwargs_)
        else:
            return commissionMemberType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.memberNumber is not None or
            self.nameInfo is not None or
            self.role is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'memberNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'memberNumber')
            if ival_ <= 0:
                raise_parse_error(child_, 'requires positiveInteger')
            ival_ = self.gds_validate_integer(ival_, node, 'memberNumber')
            self.memberNumber = ival_
            self.memberNumber_nsprefix_ = child_.prefix
        elif nodeName_ == 'nameInfo':
            obj_ = personType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameInfo = obj_
            obj_.original_tagname_ = 'nameInfo'
        elif nodeName_ == 'role':
            obj_ = commissionRoleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.role = obj_
            obj_.original_tagname_ = 'role'
# end class commissionMemberType


class commissionRoleType(GeneratedsSuper):
    """Тип: Роли членов комиссий"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['commissionRoleCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['nameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'rightVote': MemberSpec_('rightVote', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'rightVote', 'type': 'xs:boolean'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, rightVote=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_commissionRoleCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_nameType(self.name)
        self.name_nsprefix_ = None
        self.rightVote = rightVote
        self.rightVote_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, commissionRoleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if commissionRoleType.subclass:
            return commissionRoleType.subclass(*args_, **kwargs_)
        else:
            return commissionRoleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_commissionRoleCodeType(self, value):
        result = True
        # Validate type commissionRoleCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on commissionRoleCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on commissionRoleCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_nameType(self, value):
        result = True
        # Validate type nameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.name is not None or
            self.rightVote is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type commissionRoleCodeType
            self.validate_commissionRoleCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type nameType
            self.validate_nameType(self.name)
        elif nodeName_ == 'rightVote':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'rightVote')
            ival_ = self.gds_validate_boolean(ival_, node, 'rightVote')
            self.rightVote = ival_
            self.rightVote_nsprefix_ = child_.prefix
# end class commissionRoleType


class currencyRateType(GeneratedsSuper):
    """Тип: Курс валюты"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'rate': MemberSpec_('rate', ['rate', 'xs:decimal'], 0, 0, {'name': 'rate', 'type': 'xs:decimal'}, None),
        'raiting': MemberSpec_('raiting', 'xs:int', 0, 1, {'minOccurs': '0', 'name': 'raiting', 'type': 'xs:int'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, rate=None, raiting=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rate = rate
        self.rate_nsprefix_ = None
        self.raiting = raiting
        self.raiting_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, currencyRateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if currencyRateType.subclass:
            return currencyRateType.subclass(*args_, **kwargs_)
        else:
            return currencyRateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.rate is not None or
            self.raiting is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'rate' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'rate')
            fval_ = self.gds_validate_decimal(fval_, node, 'rate')
            self.rate = fval_
            self.rate_nsprefix_ = child_.prefix
        elif nodeName_ == 'raiting' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'raiting')
            ival_ = self.gds_validate_integer(ival_, node, 'raiting')
            self.raiting = ival_
            self.raiting_nsprefix_ = child_.prefix
# end class currencyRateType


class rate(GeneratedsSuper):
    """Курс валюты по отношению к рублю"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, rate)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if rate.subclass:
            return rate.subclass(*args_, **kwargs_)
        else:
            return rate(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_rate(self, value):
        result = True
        # Validate type rate, a restriction on xs:decimal.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class rate


class docPropertyType(GeneratedsSuper):
    """Тип: Реквизиты документа"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'docName': MemberSpec_('docName', ['docNameType', 'xs:string'], 0, 0, {'name': 'docName', 'type': 'xs:string'}, None),
        'docNumber': MemberSpec_('docNumber', ['docNumberType', 'xs:string'], 0, 0, {'name': 'docNumber', 'type': 'xs:string'}, None),
        'docDate': MemberSpec_('docDate', 'xs:date', 0, 0, {'name': 'docDate', 'type': 'xs:date'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, docName=None, docNumber=None, docDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.docName = docName
        self.validate_docNameType(self.docName)
        self.docName_nsprefix_ = None
        self.docNumber = docNumber
        self.validate_docNumberType(self.docNumber)
        self.docNumber_nsprefix_ = None
        if isinstance(docDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(docDate, '%Y-%m-%d').date()
        else:
            initvalue_ = docDate
        self.docDate = initvalue_
        self.docDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, docPropertyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if docPropertyType.subclass:
            return docPropertyType.subclass(*args_, **kwargs_)
        else:
            return docPropertyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_docNameType(self, value):
        result = True
        # Validate type docNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on docNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on docNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_docNumberType(self, value):
        result = True
        # Validate type docNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 350:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on docNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on docNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.docName is not None or
            self.docNumber is not None or
            self.docDate is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'docName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'docName')
            value_ = self.gds_validate_string(value_, node, 'docName')
            self.docName = value_
            self.docName_nsprefix_ = child_.prefix
            # validate type docNameType
            self.validate_docNameType(self.docName)
        elif nodeName_ == 'docNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'docNumber')
            value_ = self.gds_validate_string(value_, node, 'docNumber')
            self.docNumber = value_
            self.docNumber_nsprefix_ = child_.prefix
            # validate type docNumberType
            self.validate_docNumberType(self.docNumber)
        elif nodeName_ == 'docDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.docDate = dval_
            self.docDate_nsprefix_ = child_.prefix
# end class docPropertyType


class docType(GeneratedsSuper):
    """Тип: Тип документа в рамках закупки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['code', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['name', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, docType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if docType.subclass:
            return docType.subclass(*args_, **kwargs_)
        else:
            return docType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.code is not None or
            self.name is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
# end class docType


class code(GeneratedsSuper):
    """Кодовое наименование типа"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, code)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if code.subclass:
            return code.subclass(*args_, **kwargs_)
        else:
            return code(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_code(self, value):
        result = True
        # Validate type code, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class code


class name(GeneratedsSuper):
    """Наименование типа документа"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, name)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if name.subclass:
            return name.subclass(*args_, **kwargs_)
        else:
            return name(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_name(self, value):
        result = True
        # Validate type name, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class name


class errorInfoType(GeneratedsSuper):
    """Тип: Результат вызова сервиса в случае ошибки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', 'xs:int', 0, 0, {'name': 'code', 'type': 'xs:int'}, None),
        'message': MemberSpec_('message', ['text2000Type', 'xs:string'], 0, 0, {'name': 'message', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, message=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.code_nsprefix_ = None
        self.message = message
        self.validate_text2000Type(self.message)
        self.message_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, errorInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if errorInfoType.subclass:
            return errorInfoType.subclass(*args_, **kwargs_)
        else:
            return errorInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.message is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'code')
            ival_ = self.gds_validate_integer(ival_, node, 'code')
            self.code = ival_
            self.code_nsprefix_ = child_.prefix
        elif nodeName_ == 'message':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'message')
            value_ = self.gds_validate_string(value_, node, 'message')
            self.message = value_
            self.message_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.message)
# end class errorInfoType


class extPrintFormType(GeneratedsSuper):
    """Тип: Электронный документ, полученный из внешней системы"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'content': MemberSpec_('content', 'xs:base64Binary', 0, 0, {'name': 'content', 'type': 'xs:base64Binary'}, 3),
        'contentId': MemberSpec_('contentId', ['guidType', 'xs:string'], 0, 0, {'name': 'contentId', 'type': 'xs:string'}, 3),
        'url': MemberSpec_('url', ['hrefType', 'xs:string'], 0, 0, {'name': 'url', 'type': 'xs:string'}, 3),
        'signature': MemberSpec_('signature', 'xs:base64Binary', 0, 0, {'name': 'signature', 'type': 'signature'}, None),
        'fileType': MemberSpec_('fileType', ['printFormFileType', 'xs:string'], 0, 0, {'name': 'fileType', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, content=None, contentId=None, url=None, signature=None, fileType=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.content = content
        self.content_nsprefix_ = None
        self.contentId = contentId
        self.validate_guidType(self.contentId)
        self.contentId_nsprefix_ = None
        self.url = url
        self.validate_hrefType(self.url)
        self.url_nsprefix_ = None
        self.signature = signature
        self.signature_nsprefix_ = None
        self.fileType = fileType
        self.validate_printFormFileType(self.fileType)
        self.fileType_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, extPrintFormType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if extPrintFormType.subclass:
            return extPrintFormType.subclass(*args_, **kwargs_)
        else:
            return extPrintFormType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_guidType(self, value):
        result = True
        # Validate type guidType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 36:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on guidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on guidType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_hrefType(self, value):
        result = True
        # Validate type hrefType, a restriction on xs:string.
        pass
        return result
    def validate_printFormFileType(self, value):
        result = True
        # Validate type printFormFileType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['pdf', 'docx', 'doc', 'rtf', 'xls', 'xlsx', 'jpeg', 'jpg', 'bmp', 'tif', 'tiff', 'txt', 'zip', 'rar', 'gif', 'csv', 'odp', 'odf', 'ods', 'odt', 'sxc', 'sxw', 'xml']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on printFormFileType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.content is not None or
            self.contentId is not None or
            self.url is not None or
            self.signature is not None or
            self.fileType is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'content':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'content')
            else:
                bval_ = None
            self.content = bval_
            self.content_nsprefix_ = child_.prefix
        elif nodeName_ == 'contentId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contentId')
            value_ = self.gds_validate_string(value_, node, 'contentId')
            self.contentId = value_
            self.contentId_nsprefix_ = child_.prefix
            # validate type guidType
            self.validate_guidType(self.contentId)
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type hrefType
            self.validate_hrefType(self.url)
        elif nodeName_ == 'signature':
            obj_ = signature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.signature = obj_
            obj_.original_tagname_ = 'signature'
        elif nodeName_ == 'fileType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fileType')
            value_ = self.gds_validate_string(value_, node, 'fileType')
            self.fileType = value_
            self.fileType_nsprefix_ = child_.prefix
            # validate type printFormFileType
            self.validate_printFormFileType(self.fileType)
# end class extPrintFormType


class signature(GeneratedsSuper):
    """Электронная подпись электронного документаТип электронной подписи:
    CAdES-BES;
    CAdES-A"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'base:signatureType', 0, 1, {'use': 'optional'}),
        'valueOf_': MemberSpec_('valueOf_', 'xs:base64Binary', 0),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['valueOf_']
    subclass = None
    superclass = None
    def __init__(self, type_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, signature)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if signature.subclass:
            return signature.subclass(*args_, **kwargs_)
        else:
            return signature(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_signatureType(self, value):
        # Validate type base:signatureType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CAdES-BES', 'CAdES-A']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on signatureType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_signatureType(self.type_)    # validate type signatureType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class signature


class organizationType(GeneratedsSuper):
    """Тип: Данные организации"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'regNum': MemberSpec_('regNum', ['spzNumType', 'xs:string'], 0, 0, {'name': 'regNum', 'type': 'xs:string'}, None),
        'consRegistryNum': MemberSpec_('consRegistryNum', ['consRegistryNumType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'consRegistryNum', 'type': 'xs:string'}, None),
        'fullName': MemberSpec_('fullName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullName', 'type': 'xs:string'}, None),
        'shortName': MemberSpec_('shortName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'shortName', 'type': 'xs:string'}, None),
        'postAddress': MemberSpec_('postAddress', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'postAddress', 'type': 'xs:string'}, None),
        'factAddress': MemberSpec_('factAddress', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'factAddress', 'type': 'xs:string'}, None),
        'INN': MemberSpec_('INN', ['innOrganizationType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'INN', 'type': 'xs:string'}, None),
        'KPP': MemberSpec_('KPP', ['kppType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'KPP', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, regNum=None, consRegistryNum=None, fullName=None, shortName=None, postAddress=None, factAddress=None, INN=None, KPP=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.regNum = regNum
        self.validate_spzNumType(self.regNum)
        self.regNum_nsprefix_ = None
        self.consRegistryNum = consRegistryNum
        self.validate_consRegistryNumType(self.consRegistryNum)
        self.consRegistryNum_nsprefix_ = None
        self.fullName = fullName
        self.validate_text2000Type(self.fullName)
        self.fullName_nsprefix_ = None
        self.shortName = shortName
        self.validate_text2000Type(self.shortName)
        self.shortName_nsprefix_ = None
        self.postAddress = postAddress
        self.validate_text2000Type(self.postAddress)
        self.postAddress_nsprefix_ = None
        self.factAddress = factAddress
        self.validate_text2000Type(self.factAddress)
        self.factAddress_nsprefix_ = None
        self.INN = INN
        self.validate_innOrganizationType(self.INN)
        self.INN_nsprefix_ = None
        self.KPP = KPP
        self.validate_kppType(self.KPP)
        self.KPP_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, organizationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if organizationType.subclass:
            return organizationType.subclass(*args_, **kwargs_)
        else:
            return organizationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_spzNumType(self, value):
        result = True
        # Validate type spzNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_spzNumType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_spzNumType_patterns_, ))
                result = False
        return result
    validate_spzNumType_patterns_ = [['^(\\d{11})$']]
    def validate_consRegistryNumType(self, value):
        result = True
        # Validate type consRegistryNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on consRegistryNumType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_innOrganizationType(self, value):
        result = True
        # Validate type innOrganizationType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_innOrganizationType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_innOrganizationType_patterns_, ))
                result = False
        return result
    validate_innOrganizationType_patterns_ = [['^(\\d{10})$']]
    def validate_kppType(self, value):
        result = True
        # Validate type kppType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on kppType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.regNum is not None or
            self.consRegistryNum is not None or
            self.fullName is not None or
            self.shortName is not None or
            self.postAddress is not None or
            self.factAddress is not None or
            self.INN is not None or
            self.KPP is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'regNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'regNum')
            value_ = self.gds_validate_string(value_, node, 'regNum')
            self.regNum = value_
            self.regNum_nsprefix_ = child_.prefix
            # validate type spzNumType
            self.validate_spzNumType(self.regNum)
        elif nodeName_ == 'consRegistryNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'consRegistryNum')
            value_ = self.gds_validate_string(value_, node, 'consRegistryNum')
            self.consRegistryNum = value_
            self.consRegistryNum_nsprefix_ = child_.prefix
            # validate type consRegistryNumType
            self.validate_consRegistryNumType(self.consRegistryNum)
        elif nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.fullName)
        elif nodeName_ == 'shortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shortName')
            value_ = self.gds_validate_string(value_, node, 'shortName')
            self.shortName = value_
            self.shortName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.shortName)
        elif nodeName_ == 'postAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postAddress')
            value_ = self.gds_validate_string(value_, node, 'postAddress')
            self.postAddress = value_
            self.postAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.postAddress)
        elif nodeName_ == 'factAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'factAddress')
            value_ = self.gds_validate_string(value_, node, 'factAddress')
            self.factAddress = value_
            self.factAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.factAddress)
        elif nodeName_ == 'INN':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'INN')
            value_ = self.gds_validate_string(value_, node, 'INN')
            self.INN = value_
            self.INN_nsprefix_ = child_.prefix
            # validate type innOrganizationType
            self.validate_innOrganizationType(self.INN)
        elif nodeName_ == 'KPP':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'KPP')
            value_ = self.gds_validate_string(value_, node, 'KPP')
            self.KPP = value_
            self.KPP_nsprefix_ = child_.prefix
            # validate type kppType
            self.validate_kppType(self.KPP)
# end class organizationType


class paymentPropertysType(GeneratedsSuper):
    """Тип: Платежные реквизиты"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'bik': MemberSpec_('bik', ['bikType', 'xs:string'], 0, 0, {'name': 'bik', 'type': 'xs:string'}, None),
        'settlementAccount': MemberSpec_('settlementAccount', ['settlementAccountType', 'xs:string'], 0, 0, {'name': 'settlementAccount', 'type': 'xs:string'}, None),
        'personalAccount': MemberSpec_('personalAccount', ['personalAccountType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'personalAccount', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, bik=None, settlementAccount=None, personalAccount=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.bik = bik
        self.validate_bikType(self.bik)
        self.bik_nsprefix_ = None
        self.settlementAccount = settlementAccount
        self.validate_settlementAccountType(self.settlementAccount)
        self.settlementAccount_nsprefix_ = None
        self.personalAccount = personalAccount
        self.validate_personalAccountType(self.personalAccount)
        self.personalAccount_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, paymentPropertysType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if paymentPropertysType.subclass:
            return paymentPropertysType.subclass(*args_, **kwargs_)
        else:
            return paymentPropertysType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_bikType(self, value):
        result = True
        # Validate type bikType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_bikType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_bikType_patterns_, ))
                result = False
        return result
    validate_bikType_patterns_ = [['^(\\d{9})$']]
    def validate_settlementAccountType(self, value):
        result = True
        # Validate type settlementAccountType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_settlementAccountType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_settlementAccountType_patterns_, ))
                result = False
        return result
    validate_settlementAccountType_patterns_ = [['^(\\d{20})$']]
    def validate_personalAccountType(self, value):
        result = True
        # Validate type personalAccountType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on personalAccountType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on personalAccountType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.bik is not None or
            self.settlementAccount is not None or
            self.personalAccount is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'bik':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'bik')
            value_ = self.gds_validate_string(value_, node, 'bik')
            self.bik = value_
            self.bik_nsprefix_ = child_.prefix
            # validate type bikType
            self.validate_bikType(self.bik)
        elif nodeName_ == 'settlementAccount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'settlementAccount')
            value_ = self.gds_validate_string(value_, node, 'settlementAccount')
            self.settlementAccount = value_
            self.settlementAccount_nsprefix_ = child_.prefix
            # validate type settlementAccountType
            self.validate_settlementAccountType(self.settlementAccount)
        elif nodeName_ == 'personalAccount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'personalAccount')
            value_ = self.gds_validate_string(value_, node, 'personalAccount')
            self.personalAccount = value_
            self.personalAccount_nsprefix_ = child_.prefix
            # validate type personalAccountType
            self.validate_personalAccountType(self.personalAccount)
# end class paymentPropertysType


class participantType(GeneratedsSuper):
    """Тип: Поставщик для протоколов электронных процедур"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'legalEntityRFInfo': MemberSpec_('legalEntityRFInfo', 'legalEntityRFInfo', 0, 0, {'name': 'legalEntityRFInfo', 'type': 'legalEntityRFInfo'}, 4),
        'legalEntityForeignStateInfo': MemberSpec_('legalEntityForeignStateInfo', 'legalEntityForeignStateInfo', 0, 0, {'name': 'legalEntityForeignStateInfo', 'type': 'legalEntityForeignStateInfo'}, 4),
        'individualPersonRFInfo': MemberSpec_('individualPersonRFInfo', 'individualPersonRFInfo', 0, 0, {'name': 'individualPersonRFInfo', 'type': 'individualPersonRFInfo'}, 4),
        'individualPersonForeignStateInfo': MemberSpec_('individualPersonForeignStateInfo', 'individualPersonForeignStateInfo', 0, 0, {'name': 'individualPersonForeignStateInfo', 'type': 'individualPersonForeignStateInfo'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, legalEntityRFInfo=None, legalEntityForeignStateInfo=None, individualPersonRFInfo=None, individualPersonForeignStateInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.legalEntityRFInfo = legalEntityRFInfo
        self.legalEntityRFInfo_nsprefix_ = None
        self.legalEntityForeignStateInfo = legalEntityForeignStateInfo
        self.legalEntityForeignStateInfo_nsprefix_ = None
        self.individualPersonRFInfo = individualPersonRFInfo
        self.individualPersonRFInfo_nsprefix_ = None
        self.individualPersonForeignStateInfo = individualPersonForeignStateInfo
        self.individualPersonForeignStateInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, participantType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if participantType.subclass:
            return participantType.subclass(*args_, **kwargs_)
        else:
            return participantType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.legalEntityRFInfo is not None or
            self.legalEntityForeignStateInfo is not None or
            self.individualPersonRFInfo is not None or
            self.individualPersonForeignStateInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'legalEntityRFInfo':
            obj_ = legalEntityRFInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalEntityRFInfo = obj_
            obj_.original_tagname_ = 'legalEntityRFInfo'
        elif nodeName_ == 'legalEntityForeignStateInfo':
            obj_ = legalEntityForeignStateInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalEntityForeignStateInfo = obj_
            obj_.original_tagname_ = 'legalEntityForeignStateInfo'
        elif nodeName_ == 'individualPersonRFInfo':
            obj_ = individualPersonRFInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.individualPersonRFInfo = obj_
            obj_.original_tagname_ = 'individualPersonRFInfo'
        elif nodeName_ == 'individualPersonForeignStateInfo':
            obj_ = individualPersonForeignStateInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.individualPersonForeignStateInfo = obj_
            obj_.original_tagname_ = 'individualPersonForeignStateInfo'
# end class participantType


class legalEntityRFInfo(GeneratedsSuper):
    """Юридическое лицо РФ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'fullName': MemberSpec_('fullName', ['text2000Type', 'xs:string'], 0, 0, {'name': 'fullName', 'type': 'xs:string'}, 4),
        'shortName': MemberSpec_('shortName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'shortName', 'type': 'xs:string'}, 4),
        'firmName': MemberSpec_('firmName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'firmName', 'type': 'xs:string'}, 4),
        'INN': MemberSpec_('INN', ['innEntityType', 'xs:string'], 0, 0, {'name': 'INN', 'type': 'xs:string'}, 4),
        'KPP': MemberSpec_('KPP', ['kppType', 'xs:string'], 0, 0, {'name': 'KPP', 'type': 'xs:string'}, 4),
        'registrationDate': MemberSpec_('registrationDate', 'xs:date', 0, 1, {'minOccurs': '0', 'name': 'registrationDate', 'type': 'xs:date'}, 4),
        'ogrn': MemberSpec_('ogrn', ['ogrnCodeType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'ogrn', 'type': 'xs:string'}, 4),
        'legalForm': MemberSpec_('legalForm', 'OKOPFRef', 0, 1, {'minOccurs': '0', 'name': 'legalForm', 'type': 'OKOPFRef'}, 4),
        'contactInfo': MemberSpec_('contactInfo', 'contactInfo', 0, 0, {'name': 'contactInfo', 'type': 'contactInfo'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, fullName=None, shortName=None, firmName=None, INN=None, KPP=None, registrationDate=None, ogrn=None, legalForm=None, contactInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fullName = fullName
        self.validate_text2000Type(self.fullName)
        self.fullName_nsprefix_ = None
        self.shortName = shortName
        self.validate_text2000Type(self.shortName)
        self.shortName_nsprefix_ = None
        self.firmName = firmName
        self.validate_text2000Type(self.firmName)
        self.firmName_nsprefix_ = None
        self.INN = INN
        self.validate_innEntityType(self.INN)
        self.INN_nsprefix_ = None
        self.KPP = KPP
        self.validate_kppType(self.KPP)
        self.KPP_nsprefix_ = None
        if isinstance(registrationDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(registrationDate, '%Y-%m-%d').date()
        else:
            initvalue_ = registrationDate
        self.registrationDate = initvalue_
        self.registrationDate_nsprefix_ = None
        self.ogrn = ogrn
        self.validate_ogrnCodeType(self.ogrn)
        self.ogrn_nsprefix_ = None
        self.legalForm = legalForm
        self.legalForm_nsprefix_ = None
        self.contactInfo = contactInfo
        self.contactInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityRFInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityRFInfo.subclass:
            return legalEntityRFInfo.subclass(*args_, **kwargs_)
        else:
            return legalEntityRFInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_innEntityType(self, value):
        result = True
        # Validate type innEntityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_innEntityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_innEntityType_patterns_, ))
                result = False
        return result
    validate_innEntityType_patterns_ = [['^(\\d{10})$']]
    def validate_kppType(self, value):
        result = True
        # Validate type kppType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on kppType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ogrnCodeType(self, value):
        result = True
        # Validate type ogrnCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_ogrnCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ogrnCodeType_patterns_, ))
                result = False
        return result
    validate_ogrnCodeType_patterns_ = [['^(\\d{13}|\\d{15})$']]
    def hasContent_(self):
        if (
            self.fullName is not None or
            self.shortName is not None or
            self.firmName is not None or
            self.INN is not None or
            self.KPP is not None or
            self.registrationDate is not None or
            self.ogrn is not None or
            self.legalForm is not None or
            self.contactInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.fullName)
        elif nodeName_ == 'shortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shortName')
            value_ = self.gds_validate_string(value_, node, 'shortName')
            self.shortName = value_
            self.shortName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.shortName)
        elif nodeName_ == 'firmName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firmName')
            value_ = self.gds_validate_string(value_, node, 'firmName')
            self.firmName = value_
            self.firmName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.firmName)
        elif nodeName_ == 'INN':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'INN')
            value_ = self.gds_validate_string(value_, node, 'INN')
            self.INN = value_
            self.INN_nsprefix_ = child_.prefix
            # validate type innEntityType
            self.validate_innEntityType(self.INN)
        elif nodeName_ == 'KPP':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'KPP')
            value_ = self.gds_validate_string(value_, node, 'KPP')
            self.KPP = value_
            self.KPP_nsprefix_ = child_.prefix
            # validate type kppType
            self.validate_kppType(self.KPP)
        elif nodeName_ == 'registrationDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.registrationDate = dval_
            self.registrationDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'ogrn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ogrn')
            value_ = self.gds_validate_string(value_, node, 'ogrn')
            self.ogrn = value_
            self.ogrn_nsprefix_ = child_.prefix
            # validate type ogrnCodeType
            self.validate_ogrnCodeType(self.ogrn)
        elif nodeName_ == 'legalForm':
            obj_ = OKOPFRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalForm = obj_
            obj_.original_tagname_ = 'legalForm'
        elif nodeName_ == 'contactInfo':
            obj_ = contactInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contactInfo = obj_
            obj_.original_tagname_ = 'contactInfo'
# end class legalEntityRFInfo


class contactInfo(GeneratedsSuper):
    """Контактная информация"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'orgPostAddress': MemberSpec_('orgPostAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'orgPostAddress', 'type': 'xs:string'}, 4),
        'orgFactAddress': MemberSpec_('orgFactAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'orgFactAddress', 'type': 'xs:string'}, 4),
        'contactPersonInfo': MemberSpec_('contactPersonInfo', 'personType', 0, 1, {'minOccurs': '0', 'name': 'contactPersonInfo', 'type': 'personType'}, 4),
        'contactEMail': MemberSpec_('contactEMail', ['eMailType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'contactEMail', 'type': 'xs:string'}, 4),
        'contactPhone': MemberSpec_('contactPhone', ['phoneType', 'xs:string'], 0, 0, {'name': 'contactPhone', 'type': 'xs:string'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, orgPostAddress=None, orgFactAddress=None, contactPersonInfo=None, contactEMail=None, contactPhone=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.orgPostAddress = orgPostAddress
        self.validate_text2000Type(self.orgPostAddress)
        self.orgPostAddress_nsprefix_ = None
        self.orgFactAddress = orgFactAddress
        self.validate_text2000Type(self.orgFactAddress)
        self.orgFactAddress_nsprefix_ = None
        self.contactPersonInfo = contactPersonInfo
        self.contactPersonInfo_nsprefix_ = None
        self.contactEMail = contactEMail
        self.validate_eMailType(self.contactEMail)
        self.contactEMail_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_phoneType(self.contactPhone)
        self.contactPhone_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contactInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contactInfo.subclass:
            return contactInfo.subclass(*args_, **kwargs_)
        else:
            return contactInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_eMailType(self, value):
        result = True
        # Validate type eMailType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType(self, value):
        result = True
        # Validate type phoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.orgPostAddress is not None or
            self.orgFactAddress is not None or
            self.contactPersonInfo is not None or
            self.contactEMail is not None or
            self.contactPhone is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'orgPostAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orgPostAddress')
            value_ = self.gds_validate_string(value_, node, 'orgPostAddress')
            self.orgPostAddress = value_
            self.orgPostAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.orgPostAddress)
        elif nodeName_ == 'orgFactAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orgFactAddress')
            value_ = self.gds_validate_string(value_, node, 'orgFactAddress')
            self.orgFactAddress = value_
            self.orgFactAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.orgFactAddress)
        elif nodeName_ == 'contactPersonInfo':
            obj_ = personType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contactPersonInfo = obj_
            obj_.original_tagname_ = 'contactPersonInfo'
        elif nodeName_ == 'contactEMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactEMail')
            value_ = self.gds_validate_string(value_, node, 'contactEMail')
            self.contactEMail = value_
            self.contactEMail_nsprefix_ = child_.prefix
            # validate type eMailType
            self.validate_eMailType(self.contactEMail)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type phoneType
            self.validate_phoneType(self.contactPhone)
# end class contactInfo


class legalEntityForeignStateInfo(GeneratedsSuper):
    """Юридическое лицо иностранного государства"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'fullName': MemberSpec_('fullName', ['text2000Type', 'xs:string'], 0, 0, {'name': 'fullName', 'type': 'xs:string'}, 4),
        'shortName': MemberSpec_('shortName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'shortName', 'type': 'xs:string'}, 4),
        'firmName': MemberSpec_('firmName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'firmName', 'type': 'xs:string'}, 4),
        'fullNameLat': MemberSpec_('fullNameLat', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullNameLat', 'type': 'xs:string'}, 4),
        'taxPayerCode': MemberSpec_('taxPayerCode', ['taxPayerCode', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'taxPayerCode', 'type': 'xs:string'}, 4),
        'ogrn': MemberSpec_('ogrn', ['ogrnCodeType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'ogrn', 'type': 'xs:string'}, 4),
        'legalForm': MemberSpec_('legalForm', 'OKOPFRef', 0, 1, {'minOccurs': '0', 'name': 'legalForm', 'type': 'OKOPFRef'}, 4),
        'registerInRFTaxBodiesInfo': MemberSpec_('registerInRFTaxBodiesInfo', 'registerInRFTaxBodiesInfo', 0, 1, {'minOccurs': '0', 'name': 'registerInRFTaxBodiesInfo', 'type': 'registerInRFTaxBodiesInfo'}, 4),
        'placeOfStayInRegCountryInfo': MemberSpec_('placeOfStayInRegCountryInfo', 'placeOfStayInRegCountryInfo', 0, 0, {'name': 'placeOfStayInRegCountryInfo', 'type': 'placeOfStayInRegCountryInfo'}, 4),
        'placeOfStayInRFInfo': MemberSpec_('placeOfStayInRFInfo', 'placeOfStayInRFInfo', 0, 1, {'minOccurs': '0', 'name': 'placeOfStayInRFInfo', 'type': 'placeOfStayInRFInfo'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, fullName=None, shortName=None, firmName=None, fullNameLat=None, taxPayerCode=None, ogrn=None, legalForm=None, registerInRFTaxBodiesInfo=None, placeOfStayInRegCountryInfo=None, placeOfStayInRFInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fullName = fullName
        self.validate_text2000Type(self.fullName)
        self.fullName_nsprefix_ = None
        self.shortName = shortName
        self.validate_text2000Type(self.shortName)
        self.shortName_nsprefix_ = None
        self.firmName = firmName
        self.validate_text2000Type(self.firmName)
        self.firmName_nsprefix_ = None
        self.fullNameLat = fullNameLat
        self.validate_text2000Type(self.fullNameLat)
        self.fullNameLat_nsprefix_ = None
        self.taxPayerCode = taxPayerCode
        self.validate_taxPayerCode(self.taxPayerCode)
        self.taxPayerCode_nsprefix_ = None
        self.ogrn = ogrn
        self.validate_ogrnCodeType(self.ogrn)
        self.ogrn_nsprefix_ = None
        self.legalForm = legalForm
        self.legalForm_nsprefix_ = None
        self.registerInRFTaxBodiesInfo = registerInRFTaxBodiesInfo
        self.registerInRFTaxBodiesInfo_nsprefix_ = None
        self.placeOfStayInRegCountryInfo = placeOfStayInRegCountryInfo
        self.placeOfStayInRegCountryInfo_nsprefix_ = None
        self.placeOfStayInRFInfo = placeOfStayInRFInfo
        self.placeOfStayInRFInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, legalEntityForeignStateInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if legalEntityForeignStateInfo.subclass:
            return legalEntityForeignStateInfo.subclass(*args_, **kwargs_)
        else:
            return legalEntityForeignStateInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_taxPayerCode(self, value):
        result = True
        # Validate type taxPayerCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on taxPayerCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on taxPayerCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ogrnCodeType(self, value):
        result = True
        # Validate type ogrnCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_ogrnCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ogrnCodeType_patterns_, ))
                result = False
        return result
    validate_ogrnCodeType_patterns_ = [['^(\\d{13}|\\d{15})$']]
    def hasContent_(self):
        if (
            self.fullName is not None or
            self.shortName is not None or
            self.firmName is not None or
            self.fullNameLat is not None or
            self.taxPayerCode is not None or
            self.ogrn is not None or
            self.legalForm is not None or
            self.registerInRFTaxBodiesInfo is not None or
            self.placeOfStayInRegCountryInfo is not None or
            self.placeOfStayInRFInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.fullName)
        elif nodeName_ == 'shortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shortName')
            value_ = self.gds_validate_string(value_, node, 'shortName')
            self.shortName = value_
            self.shortName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.shortName)
        elif nodeName_ == 'firmName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firmName')
            value_ = self.gds_validate_string(value_, node, 'firmName')
            self.firmName = value_
            self.firmName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.firmName)
        elif nodeName_ == 'fullNameLat':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullNameLat')
            value_ = self.gds_validate_string(value_, node, 'fullNameLat')
            self.fullNameLat = value_
            self.fullNameLat_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.fullNameLat)
        elif nodeName_ == 'taxPayerCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxPayerCode')
            value_ = self.gds_validate_string(value_, node, 'taxPayerCode')
            self.taxPayerCode = value_
            self.taxPayerCode_nsprefix_ = child_.prefix
            # validate type taxPayerCode
            self.validate_taxPayerCode(self.taxPayerCode)
        elif nodeName_ == 'ogrn':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'ogrn')
            value_ = self.gds_validate_string(value_, node, 'ogrn')
            self.ogrn = value_
            self.ogrn_nsprefix_ = child_.prefix
            # validate type ogrnCodeType
            self.validate_ogrnCodeType(self.ogrn)
        elif nodeName_ == 'legalForm':
            obj_ = OKOPFRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.legalForm = obj_
            obj_.original_tagname_ = 'legalForm'
        elif nodeName_ == 'registerInRFTaxBodiesInfo':
            obj_ = registerInRFTaxBodiesInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.registerInRFTaxBodiesInfo = obj_
            obj_.original_tagname_ = 'registerInRFTaxBodiesInfo'
        elif nodeName_ == 'placeOfStayInRegCountryInfo':
            obj_ = placeOfStayInRegCountryInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.placeOfStayInRegCountryInfo = obj_
            obj_.original_tagname_ = 'placeOfStayInRegCountryInfo'
        elif nodeName_ == 'placeOfStayInRFInfo':
            obj_ = placeOfStayInRFInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.placeOfStayInRFInfo = obj_
            obj_.original_tagname_ = 'placeOfStayInRFInfo'
# end class legalEntityForeignStateInfo


class registerInRFTaxBodiesInfo(GeneratedsSuper):
    """Поставщик состоит на учете в налоговых органах на территории РФ.
    При приеме контролируется заполнение данного блока или/и поля "Код
    налогоплательщика в стране регистрации или его аналог"
    (legalEntityForeignStateInfo/taxPayerCode)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'INN': MemberSpec_('INN', ['innEntityType', 'xs:string'], 0, 0, {'name': 'INN', 'type': 'xs:string'}, 4),
        'KPP': MemberSpec_('KPP', ['kppType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'KPP', 'type': 'xs:string'}, 4),
        'registrationDate': MemberSpec_('registrationDate', 'xs:date', 0, 1, {'minOccurs': '0', 'name': 'registrationDate', 'type': 'xs:date'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, INN=None, KPP=None, registrationDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.INN = INN
        self.validate_innEntityType(self.INN)
        self.INN_nsprefix_ = None
        self.KPP = KPP
        self.validate_kppType(self.KPP)
        self.KPP_nsprefix_ = None
        if isinstance(registrationDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(registrationDate, '%Y-%m-%d').date()
        else:
            initvalue_ = registrationDate
        self.registrationDate = initvalue_
        self.registrationDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, registerInRFTaxBodiesInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if registerInRFTaxBodiesInfo.subclass:
            return registerInRFTaxBodiesInfo.subclass(*args_, **kwargs_)
        else:
            return registerInRFTaxBodiesInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_innEntityType(self, value):
        result = True
        # Validate type innEntityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_innEntityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_innEntityType_patterns_, ))
                result = False
        return result
    validate_innEntityType_patterns_ = [['^(\\d{10})$']]
    def validate_kppType(self, value):
        result = True
        # Validate type kppType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on kppType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.INN is not None or
            self.KPP is not None or
            self.registrationDate is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'INN':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'INN')
            value_ = self.gds_validate_string(value_, node, 'INN')
            self.INN = value_
            self.INN_nsprefix_ = child_.prefix
            # validate type innEntityType
            self.validate_innEntityType(self.INN)
        elif nodeName_ == 'KPP':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'KPP')
            value_ = self.gds_validate_string(value_, node, 'KPP')
            self.KPP = value_
            self.KPP_nsprefix_ = child_.prefix
            # validate type kppType
            self.validate_kppType(self.KPP)
        elif nodeName_ == 'registrationDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.registrationDate = dval_
            self.registrationDate_nsprefix_ = child_.prefix
# end class registerInRFTaxBodiesInfo


class placeOfStayInRegCountryInfo(GeneratedsSuper):
    """Место нахождения в стране регистрации"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'country': MemberSpec_('country', 'OKSMRef', 0, 0, {'name': 'country', 'type': 'OKSMRef'}, 4),
        'orgPostAddress': MemberSpec_('orgPostAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'orgPostAddress', 'type': 'xs:string'}, 4),
        'orgFactAddress': MemberSpec_('orgFactAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'orgFactAddress', 'type': 'xs:string'}, 4),
        'contactEMail': MemberSpec_('contactEMail', ['eMailType', 'xs:string'], 0, 0, {'name': 'contactEMail', 'type': 'xs:string'}, 4),
        'contactPhone': MemberSpec_('contactPhone', ['phoneType', 'xs:string'], 0, 0, {'name': 'contactPhone', 'type': 'xs:string'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, country=None, orgPostAddress=None, orgFactAddress=None, contactEMail=None, contactPhone=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.country = country
        self.country_nsprefix_ = None
        self.orgPostAddress = orgPostAddress
        self.validate_text2000Type(self.orgPostAddress)
        self.orgPostAddress_nsprefix_ = None
        self.orgFactAddress = orgFactAddress
        self.validate_text2000Type(self.orgFactAddress)
        self.orgFactAddress_nsprefix_ = None
        self.contactEMail = contactEMail
        self.validate_eMailType(self.contactEMail)
        self.contactEMail_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_phoneType(self.contactPhone)
        self.contactPhone_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, placeOfStayInRegCountryInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if placeOfStayInRegCountryInfo.subclass:
            return placeOfStayInRegCountryInfo.subclass(*args_, **kwargs_)
        else:
            return placeOfStayInRegCountryInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_eMailType(self, value):
        result = True
        # Validate type eMailType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType(self, value):
        result = True
        # Validate type phoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.country is not None or
            self.orgPostAddress is not None or
            self.orgFactAddress is not None or
            self.contactEMail is not None or
            self.contactPhone is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'country':
            obj_ = OKSMRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.country = obj_
            obj_.original_tagname_ = 'country'
        elif nodeName_ == 'orgPostAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orgPostAddress')
            value_ = self.gds_validate_string(value_, node, 'orgPostAddress')
            self.orgPostAddress = value_
            self.orgPostAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.orgPostAddress)
        elif nodeName_ == 'orgFactAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orgFactAddress')
            value_ = self.gds_validate_string(value_, node, 'orgFactAddress')
            self.orgFactAddress = value_
            self.orgFactAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.orgFactAddress)
        elif nodeName_ == 'contactEMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactEMail')
            value_ = self.gds_validate_string(value_, node, 'contactEMail')
            self.contactEMail = value_
            self.contactEMail_nsprefix_ = child_.prefix
            # validate type eMailType
            self.validate_eMailType(self.contactEMail)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type phoneType
            self.validate_phoneType(self.contactPhone)
# end class placeOfStayInRegCountryInfo


class placeOfStayInRFInfo(GeneratedsSuper):
    """Наличие у поставщика места пребывания на территории РФ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'orgPostAddress': MemberSpec_('orgPostAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'orgPostAddress', 'type': 'xs:string'}, 4),
        'orgFactAddress': MemberSpec_('orgFactAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'orgFactAddress', 'type': 'xs:string'}, 4),
        'contactEMail': MemberSpec_('contactEMail', ['eMailType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'contactEMail', 'type': 'xs:string'}, 4),
        'contactPhone': MemberSpec_('contactPhone', ['phoneType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'contactPhone', 'type': 'xs:string'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, orgPostAddress=None, orgFactAddress=None, contactEMail=None, contactPhone=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.orgPostAddress = orgPostAddress
        self.validate_text2000Type(self.orgPostAddress)
        self.orgPostAddress_nsprefix_ = None
        self.orgFactAddress = orgFactAddress
        self.validate_text2000Type(self.orgFactAddress)
        self.orgFactAddress_nsprefix_ = None
        self.contactEMail = contactEMail
        self.validate_eMailType(self.contactEMail)
        self.contactEMail_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_phoneType(self.contactPhone)
        self.contactPhone_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, placeOfStayInRFInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if placeOfStayInRFInfo.subclass:
            return placeOfStayInRFInfo.subclass(*args_, **kwargs_)
        else:
            return placeOfStayInRFInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_eMailType(self, value):
        result = True
        # Validate type eMailType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType(self, value):
        result = True
        # Validate type phoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.orgPostAddress is not None or
            self.orgFactAddress is not None or
            self.contactEMail is not None or
            self.contactPhone is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'orgPostAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orgPostAddress')
            value_ = self.gds_validate_string(value_, node, 'orgPostAddress')
            self.orgPostAddress = value_
            self.orgPostAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.orgPostAddress)
        elif nodeName_ == 'orgFactAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'orgFactAddress')
            value_ = self.gds_validate_string(value_, node, 'orgFactAddress')
            self.orgFactAddress = value_
            self.orgFactAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.orgFactAddress)
        elif nodeName_ == 'contactEMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactEMail')
            value_ = self.gds_validate_string(value_, node, 'contactEMail')
            self.contactEMail = value_
            self.contactEMail_nsprefix_ = child_.prefix
            # validate type eMailType
            self.validate_eMailType(self.contactEMail)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type phoneType
            self.validate_phoneType(self.contactPhone)
# end class placeOfStayInRFInfo


class individualPersonRFInfo(GeneratedsSuper):
    """Физическое лицо РФ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'nameInfo': MemberSpec_('nameInfo', 'personType', 0, 0, {'name': 'nameInfo', 'type': 'personType'}, 4),
        'INN': MemberSpec_('INN', ['innIndividualType', 'xs:string'], 0, 0, {'name': 'INN', 'type': 'xs:string'}, 4),
        'registrationDate': MemberSpec_('registrationDate', 'xs:date', 0, 1, {'minOccurs': '0', 'name': 'registrationDate', 'type': 'xs:date'}, 4),
        'postAddress': MemberSpec_('postAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'postAddress', 'type': 'xs:string'}, 4),
        'factAddress': MemberSpec_('factAddress', ['text2000Type', 'xs:string'], 0, 0, {'name': 'factAddress', 'type': 'xs:string'}, 4),
        'contactEMail': MemberSpec_('contactEMail', ['eMailType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'contactEMail', 'type': 'xs:string'}, 4),
        'contactPhone': MemberSpec_('contactPhone', ['phoneType', 'xs:string'], 0, 0, {'name': 'contactPhone', 'type': 'xs:string'}, 4),
        'isIP': MemberSpec_('isIP', 'xs:boolean', 0, 0, {'name': 'isIP', 'type': 'xs:boolean'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, nameInfo=None, INN=None, registrationDate=None, postAddress=None, factAddress=None, contactEMail=None, contactPhone=None, isIP=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.nameInfo = nameInfo
        self.nameInfo_nsprefix_ = None
        self.INN = INN
        self.validate_innIndividualType(self.INN)
        self.INN_nsprefix_ = None
        if isinstance(registrationDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(registrationDate, '%Y-%m-%d').date()
        else:
            initvalue_ = registrationDate
        self.registrationDate = initvalue_
        self.registrationDate_nsprefix_ = None
        self.postAddress = postAddress
        self.validate_text2000Type(self.postAddress)
        self.postAddress_nsprefix_ = None
        self.factAddress = factAddress
        self.validate_text2000Type(self.factAddress)
        self.factAddress_nsprefix_ = None
        self.contactEMail = contactEMail
        self.validate_eMailType(self.contactEMail)
        self.contactEMail_nsprefix_ = None
        self.contactPhone = contactPhone
        self.validate_phoneType(self.contactPhone)
        self.contactPhone_nsprefix_ = None
        self.isIP = isIP
        self.isIP_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, individualPersonRFInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if individualPersonRFInfo.subclass:
            return individualPersonRFInfo.subclass(*args_, **kwargs_)
        else:
            return individualPersonRFInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_innIndividualType(self, value):
        result = True
        # Validate type innIndividualType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_innIndividualType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_innIndividualType_patterns_, ))
                result = False
        return result
    validate_innIndividualType_patterns_ = [['^(\\d{12})$']]
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_eMailType(self, value):
        result = True
        # Validate type eMailType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType(self, value):
        result = True
        # Validate type phoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.nameInfo is not None or
            self.INN is not None or
            self.registrationDate is not None or
            self.postAddress is not None or
            self.factAddress is not None or
            self.contactEMail is not None or
            self.contactPhone is not None or
            self.isIP is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'nameInfo':
            obj_ = personType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameInfo = obj_
            obj_.original_tagname_ = 'nameInfo'
        elif nodeName_ == 'INN':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'INN')
            value_ = self.gds_validate_string(value_, node, 'INN')
            self.INN = value_
            self.INN_nsprefix_ = child_.prefix
            # validate type innIndividualType
            self.validate_innIndividualType(self.INN)
        elif nodeName_ == 'registrationDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.registrationDate = dval_
            self.registrationDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'postAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postAddress')
            value_ = self.gds_validate_string(value_, node, 'postAddress')
            self.postAddress = value_
            self.postAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.postAddress)
        elif nodeName_ == 'factAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'factAddress')
            value_ = self.gds_validate_string(value_, node, 'factAddress')
            self.factAddress = value_
            self.factAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.factAddress)
        elif nodeName_ == 'contactEMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactEMail')
            value_ = self.gds_validate_string(value_, node, 'contactEMail')
            self.contactEMail = value_
            self.contactEMail_nsprefix_ = child_.prefix
            # validate type eMailType
            self.validate_eMailType(self.contactEMail)
        elif nodeName_ == 'contactPhone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'contactPhone')
            value_ = self.gds_validate_string(value_, node, 'contactPhone')
            self.contactPhone = value_
            self.contactPhone_nsprefix_ = child_.prefix
            # validate type phoneType
            self.validate_phoneType(self.contactPhone)
        elif nodeName_ == 'isIP':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isIP')
            ival_ = self.gds_validate_boolean(ival_, node, 'isIP')
            self.isIP = ival_
            self.isIP_nsprefix_ = child_.prefix
# end class individualPersonRFInfo


class individualPersonForeignStateInfo(GeneratedsSuper):
    """Физическое лицо иностранного государства"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'nameInfo': MemberSpec_('nameInfo', 'personType', 0, 0, {'name': 'nameInfo', 'type': 'personType'}, 4),
        'nameLatInfo': MemberSpec_('nameLatInfo', 'personType', 0, 1, {'minOccurs': '0', 'name': 'nameLatInfo', 'type': 'personType'}, 4),
        'taxPayerCode': MemberSpec_('taxPayerCode', ['taxPayerCode', 'xs:string'], 0, 0, {'name': 'taxPayerCode', 'type': 'xs:string'}, 4),
        'registerInRFTaxBodiesInfo': MemberSpec_('registerInRFTaxBodiesInfo', 'registerInRFTaxBodiesInfo', 0, 1, {'minOccurs': '0', 'name': 'registerInRFTaxBodiesInfo', 'type': 'registerInRFTaxBodiesInfo'}, 4),
        'placeOfStayInRegCountryInfo': MemberSpec_('placeOfStayInRegCountryInfo', 'placeOfStayInRegCountryInfo', 0, 0, {'name': 'placeOfStayInRegCountryInfo', 'type': 'placeOfStayInRegCountryInfo'}, 4),
        'placeOfStayInRFInfo': MemberSpec_('placeOfStayInRFInfo', 'placeOfStayInRFInfo', 0, 1, {'minOccurs': '0', 'name': 'placeOfStayInRFInfo', 'type': 'placeOfStayInRFInfo'}, 4),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, nameInfo=None, nameLatInfo=None, taxPayerCode=None, registerInRFTaxBodiesInfo=None, placeOfStayInRegCountryInfo=None, placeOfStayInRFInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.nameInfo = nameInfo
        self.nameInfo_nsprefix_ = None
        self.nameLatInfo = nameLatInfo
        self.nameLatInfo_nsprefix_ = None
        self.taxPayerCode = taxPayerCode
        self.validate_taxPayerCode(self.taxPayerCode)
        self.taxPayerCode_nsprefix_ = None
        self.registerInRFTaxBodiesInfo = registerInRFTaxBodiesInfo
        self.registerInRFTaxBodiesInfo_nsprefix_ = None
        self.placeOfStayInRegCountryInfo = placeOfStayInRegCountryInfo
        self.placeOfStayInRegCountryInfo_nsprefix_ = None
        self.placeOfStayInRFInfo = placeOfStayInRFInfo
        self.placeOfStayInRFInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, individualPersonForeignStateInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if individualPersonForeignStateInfo.subclass:
            return individualPersonForeignStateInfo.subclass(*args_, **kwargs_)
        else:
            return individualPersonForeignStateInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_taxPayerCode(self, value):
        result = True
        # Validate type taxPayerCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on taxPayerCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on taxPayerCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.nameInfo is not None or
            self.nameLatInfo is not None or
            self.taxPayerCode is not None or
            self.registerInRFTaxBodiesInfo is not None or
            self.placeOfStayInRegCountryInfo is not None or
            self.placeOfStayInRFInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'nameInfo':
            obj_ = personType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameInfo = obj_
            obj_.original_tagname_ = 'nameInfo'
        elif nodeName_ == 'nameLatInfo':
            obj_ = personType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.nameLatInfo = obj_
            obj_.original_tagname_ = 'nameLatInfo'
        elif nodeName_ == 'taxPayerCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'taxPayerCode')
            value_ = self.gds_validate_string(value_, node, 'taxPayerCode')
            self.taxPayerCode = value_
            self.taxPayerCode_nsprefix_ = child_.prefix
            # validate type taxPayerCode
            self.validate_taxPayerCode(self.taxPayerCode)
        elif nodeName_ == 'registerInRFTaxBodiesInfo':
            obj_ = registerInRFTaxBodiesInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.registerInRFTaxBodiesInfo = obj_
            obj_.original_tagname_ = 'registerInRFTaxBodiesInfo'
        elif nodeName_ == 'placeOfStayInRegCountryInfo':
            obj_ = placeOfStayInRegCountryInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.placeOfStayInRegCountryInfo = obj_
            obj_.original_tagname_ = 'placeOfStayInRegCountryInfo'
        elif nodeName_ == 'placeOfStayInRFInfo':
            obj_ = placeOfStayInRFInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.placeOfStayInRFInfo = obj_
            obj_.original_tagname_ = 'placeOfStayInRFInfo'
# end class individualPersonForeignStateInfo


class printFormType(GeneratedsSuper):
    """Тип: Печатная форма"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'url': MemberSpec_('url', ['hrefType', 'xs:string'], 0, 0, {'name': 'url', 'type': 'xs:string'}, None),
        'signature': MemberSpec_('signature', 'xs:base64Binary', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'signature', 'type': 'signature'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, url=None, signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.url = url
        self.validate_hrefType(self.url)
        self.url_nsprefix_ = None
        if signature is None:
            self.signature = []
        else:
            self.signature = signature
        self.signature_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, printFormType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if printFormType.subclass:
            return printFormType.subclass(*args_, **kwargs_)
        else:
            return printFormType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_hrefType(self, value):
        result = True
        # Validate type hrefType, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (
            self.url is not None or
            self.signature
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type hrefType
            self.validate_hrefType(self.url)
        elif nodeName_ == 'signature':
            obj_ = signature.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.signature.append(obj_)
            obj_.original_tagname_ = 'signature'
# end class printFormType


class purchaseObjectsType(GeneratedsSuper):
    """Тип: Информация по объектам закупки, не являющимся лекарственными
    препаратами"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'purchaseObject': MemberSpec_('purchaseObject', 'purchaseObject', 1, 0, {'maxOccurs': 'unbounded', 'name': 'purchaseObject', 'type': 'purchaseObject'}, None),
        'totalSum': MemberSpec_('totalSum', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'totalSum', 'type': 'xs:string'}, None),
        'totalSumCurrency': MemberSpec_('totalSumCurrency', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'totalSumCurrency', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, purchaseObject=None, totalSum=None, totalSumCurrency=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if purchaseObject is None:
            self.purchaseObject = []
        else:
            self.purchaseObject = purchaseObject
        self.purchaseObject_nsprefix_ = None
        self.totalSum = totalSum
        self.validate_moneyType(self.totalSum)
        self.totalSum_nsprefix_ = None
        self.totalSumCurrency = totalSumCurrency
        self.validate_moneyType(self.totalSumCurrency)
        self.totalSumCurrency_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, purchaseObjectsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if purchaseObjectsType.subclass:
            return purchaseObjectsType.subclass(*args_, **kwargs_)
        else:
            return purchaseObjectsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.purchaseObject or
            self.totalSum is not None or
            self.totalSumCurrency is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'purchaseObject':
            obj_ = purchaseObject.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.purchaseObject.append(obj_)
            obj_.original_tagname_ = 'purchaseObject'
        elif nodeName_ == 'totalSum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'totalSum')
            value_ = self.gds_validate_string(value_, node, 'totalSum')
            self.totalSum = value_
            self.totalSum_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.totalSum)
        elif nodeName_ == 'totalSumCurrency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'totalSumCurrency')
            value_ = self.gds_validate_string(value_, node, 'totalSumCurrency')
            self.totalSumCurrency = value_
            self.totalSumCurrency_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.totalSumCurrency)
# end class purchaseObjectsType


class purchaseObject(GeneratedsSuper):
    """Объект закупки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'sid': MemberSpec_('sid', ['sid', 'xs:long'], 0, 1, {'minOccurs': '0', 'name': 'sid', 'type': 'xs:long'}, None),
        'externalSid': MemberSpec_('externalSid', ['externalIdType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'externalSid', 'type': 'xs:string'}, None),
        'OKPD2': MemberSpec_('OKPD2', 'OKPD2Ref', 0, 0, {'name': 'OKPD2', 'type': 'OKPD2'}, 5),
        'KTRU': MemberSpec_('KTRU', 'KTRURef', 0, 0, {'name': 'KTRU', 'type': 'KTRU'}, 5),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'OKEI': MemberSpec_('OKEI', 'OKEIRef', 0, 1, {'minOccurs': '0', 'name': 'OKEI', 'type': 'OKEIRef'}, None),
        'customerQuantities': MemberSpec_('customerQuantities', 'customerQuantities', 0, 1, {'minOccurs': '0', 'name': 'customerQuantities', 'type': 'customerQuantities'}, None),
        'price': MemberSpec_('price', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'price', 'type': 'xs:string'}, None),
        'quantity': MemberSpec_('quantity', ['quantity', 'xs:decimal'], 0, 0, {'name': 'quantity', 'type': 'xs:decimal'}, None),
        'sum': MemberSpec_('sum', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'sum', 'type': 'xs:string'}, None),
        'isMedicalProduct': MemberSpec_('isMedicalProduct', 'xs:boolean', 0, 1, {'fixed': 'true', 'minOccurs': '0', 'name': 'isMedicalProduct', 'type': 'xs:boolean'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, sid=None, externalSid=None, OKPD2=None, KTRU=None, name=None, OKEI=None, customerQuantities=None, price=None, quantity=None, sum=None, isMedicalProduct=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.sid = sid
        self.sid_nsprefix_ = None
        self.externalSid = externalSid
        self.validate_externalIdType(self.externalSid)
        self.externalSid_nsprefix_ = None
        self.OKPD2 = OKPD2
        self.OKPD2_nsprefix_ = None
        self.KTRU = KTRU
        self.KTRU_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        self.OKEI = OKEI
        self.OKEI_nsprefix_ = None
        self.customerQuantities = customerQuantities
        self.customerQuantities_nsprefix_ = None
        self.price = price
        self.validate_moneyType(self.price)
        self.price_nsprefix_ = None
        self.quantity = quantity
        self.quantity_nsprefix_ = None
        self.sum = sum
        self.validate_moneyType(self.sum)
        self.sum_nsprefix_ = None
        self.isMedicalProduct = isMedicalProduct
        self.isMedicalProduct_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, purchaseObject)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if purchaseObject.subclass:
            return purchaseObject.subclass(*args_, **kwargs_)
        else:
            return purchaseObject(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_externalIdType(self, value):
        result = True
        # Validate type externalIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on externalIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on externalIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.sid is not None or
            self.externalSid is not None or
            self.OKPD2 is not None or
            self.KTRU is not None or
            self.name is not None or
            self.OKEI is not None or
            self.customerQuantities is not None or
            self.price is not None or
            self.quantity is not None or
            self.sum is not None or
            self.isMedicalProduct is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'sid' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'sid')
            ival_ = self.gds_validate_integer(ival_, node, 'sid')
            self.sid = ival_
            self.sid_nsprefix_ = child_.prefix
        elif nodeName_ == 'externalSid':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'externalSid')
            value_ = self.gds_validate_string(value_, node, 'externalSid')
            self.externalSid = value_
            self.externalSid_nsprefix_ = child_.prefix
            # validate type externalIdType
            self.validate_externalIdType(self.externalSid)
        elif nodeName_ == 'OKPD2':
            obj_ = OKPD2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKPD2 = obj_
            obj_.original_tagname_ = 'OKPD2'
        elif nodeName_ == 'KTRU':
            obj_ = KTRU.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KTRU = obj_
            obj_.original_tagname_ = 'KTRU'
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'OKEI':
            obj_ = OKEIRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKEI = obj_
            obj_.original_tagname_ = 'OKEI'
        elif nodeName_ == 'customerQuantities':
            obj_ = customerQuantities.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerQuantities = obj_
            obj_.original_tagname_ = 'customerQuantities'
        elif nodeName_ == 'price':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'price')
            value_ = self.gds_validate_string(value_, node, 'price')
            self.price = value_
            self.price_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.price)
        elif nodeName_ == 'quantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'quantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'quantity')
            self.quantity = fval_
            self.quantity_nsprefix_ = child_.prefix
        elif nodeName_ == 'sum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'sum')
            value_ = self.gds_validate_string(value_, node, 'sum')
            self.sum = value_
            self.sum_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.sum)
        elif nodeName_ == 'isMedicalProduct':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isMedicalProduct')
            ival_ = self.gds_validate_boolean(ival_, node, 'isMedicalProduct')
            self.isMedicalProduct = ival_
            self.isMedicalProduct_nsprefix_ = child_.prefix
# end class purchaseObject


class sid(GeneratedsSuper):
    """Уникальный идентификатор в ЕИС. Элемент игнорируется при приёме.
    Заполняется при передаче идентификатором объекта закупки, присвоенным в
    ЕИС"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, sid)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if sid.subclass:
            return sid.subclass(*args_, **kwargs_)
        else:
            return sid(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_sid(self, value):
        result = True
        # Validate type sid, a restriction on xs:long.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class sid


class OKPD2(OKPD2Ref):
    """Классификация по ОКПД2.
    В случае, если извещение сформировано на основании позиции плана-графика
    закупок с 01.01.2020, то контролируется на соответствие коду ОКПД2 в
    соответствующей позиции ПГ.
    Допускается указание кода-потомка расширенной разрядности"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'addCharacteristics': MemberSpec_('addCharacteristics', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'addCharacteristics', 'type': 'xs:string'}, 5),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = OKPD2Ref
    def __init__(self, OKPDCode=None, OKPDName=None, addCharacteristics=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(OKPD2, self).__init__(OKPDCode, OKPDName,  **kwargs_)
        self.addCharacteristics = addCharacteristics
        self.validate_text4000Type(self.addCharacteristics)
        self.addCharacteristics_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKPD2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKPD2.subclass:
            return OKPD2.subclass(*args_, **kwargs_)
        else:
            return OKPD2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.addCharacteristics is not None or
            super(OKPD2, self).hasContent_()
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(OKPD2, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'addCharacteristics':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'addCharacteristics')
            value_ = self.gds_validate_string(value_, node, 'addCharacteristics')
            self.addCharacteristics = value_
            self.addCharacteristics_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.addCharacteristics)
        super(OKPD2, self).buildChildren(child_, node, nodeName_, True)
# end class OKPD2


class KTRU(KTRURef):
    """Классификация по КТРУ.
    В случае, если извещение сформировано на основании позиции плана-графика
    закупок с 01.01.2020, то контролируется указание кода КТРУ,
    расширяющего код ОКПД2 из позиции ПГ.
    Поле "Номер версии позиции" (versionNumber) игнорируется при приеме первой
    версии извещения, заполняется при передаче актуальным номером позиции
    КТРУ. При приеме последующих версий извещения допустимо указание:
    -версии позиции КТРУ из предыдущей версии размещенного извещения
    -актуальной версии позиции КТРУ (если при приеме поле не заполнено, то при
    передаче заполнится значением версии позиции КТРУ из последней
    размещенной версии извещения)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'characteristics': MemberSpec_('characteristics', 'characteristics', 0, 1, {'minOccurs': '0', 'name': 'characteristics', 'type': 'characteristics'}, 5),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = KTRURef
    def __init__(self, code=None, name=None, versionId=None, versionNumber=None, characteristics=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(KTRU, self).__init__(code, name, versionId, versionNumber,  **kwargs_)
        self.characteristics = characteristics
        self.characteristics_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KTRU)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KTRU.subclass:
            return KTRU.subclass(*args_, **kwargs_)
        else:
            return KTRU(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.characteristics is not None or
            super(KTRU, self).hasContent_()
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(KTRU, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'characteristics':
            obj_ = characteristics.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.characteristics = obj_
            obj_.original_tagname_ = 'characteristics'
        super(KTRU, self).buildChildren(child_, node, nodeName_, True)
# end class KTRU


class characteristics(GeneratedsSuper):
    """Характеристики товара, работы, услуги позиции КТРУ.
    Если извещение создано на основании позиции плана-графика (ППГ) и в ППГ
    заполнен код по КТРУ, указанный в поле «Код товара, работы или услуги в
    справочнике Каталог товаров, работ, услуг (КТРУ) (nsiKTRU)»
    (KTRU/code), то значение блока игнорируется и заполняется
    соответствующим значением характеристик для позиции КТРУ из связанной
    ППГ.
    В других случаях блок принимается и сохраняется, если заполнен, и при этом
    контролируется обязательное заполнение хотя бы одного из дочерних
    блоков characteristicsUsingReferenceInfo и/или
    characteristicsUsingTextForm.
    Также контролируется принадлежность набора характеристик и их значений
    версии позиции КТРУ, которая была указана в предыдущей размещенной
    версии извещения или к актуальной версии позиции КТРУ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'characteristicsUsingReferenceInfo': MemberSpec_('characteristicsUsingReferenceInfo', 'refKTRUCharacteristicType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'characteristicsUsingReferenceInfo', 'type': 'refKTRUCharacteristicType'}, 5),
        'characteristicsUsingTextForm': MemberSpec_('characteristicsUsingTextForm', 'manualKTRUCharacteristicType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'characteristicsUsingTextForm', 'type': 'manualKTRUCharacteristicType'}, 5),
        'addCharacteristicInfoReason': MemberSpec_('addCharacteristicInfoReason', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'addCharacteristicInfoReason', 'type': 'xs:string'}, 5),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, characteristicsUsingReferenceInfo=None, characteristicsUsingTextForm=None, addCharacteristicInfoReason=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if characteristicsUsingReferenceInfo is None:
            self.characteristicsUsingReferenceInfo = []
        else:
            self.characteristicsUsingReferenceInfo = characteristicsUsingReferenceInfo
        self.characteristicsUsingReferenceInfo_nsprefix_ = None
        if characteristicsUsingTextForm is None:
            self.characteristicsUsingTextForm = []
        else:
            self.characteristicsUsingTextForm = characteristicsUsingTextForm
        self.characteristicsUsingTextForm_nsprefix_ = None
        self.addCharacteristicInfoReason = addCharacteristicInfoReason
        self.validate_text2000Type(self.addCharacteristicInfoReason)
        self.addCharacteristicInfoReason_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, characteristics)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if characteristics.subclass:
            return characteristics.subclass(*args_, **kwargs_)
        else:
            return characteristics(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.characteristicsUsingReferenceInfo or
            self.characteristicsUsingTextForm or
            self.addCharacteristicInfoReason is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'characteristicsUsingReferenceInfo':
            obj_ = refKTRUCharacteristicType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.characteristicsUsingReferenceInfo.append(obj_)
            obj_.original_tagname_ = 'characteristicsUsingReferenceInfo'
        elif nodeName_ == 'characteristicsUsingTextForm':
            obj_ = manualKTRUCharacteristicType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.characteristicsUsingTextForm.append(obj_)
            obj_.original_tagname_ = 'characteristicsUsingTextForm'
        elif nodeName_ == 'addCharacteristicInfoReason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'addCharacteristicInfoReason')
            value_ = self.gds_validate_string(value_, node, 'addCharacteristicInfoReason')
            self.addCharacteristicInfoReason = value_
            self.addCharacteristicInfoReason_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.addCharacteristicInfoReason)
# end class characteristics


class customerQuantities(GeneratedsSuper):
    """Количество по заказчикам"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'customerQuantity': MemberSpec_('customerQuantity', 'customerQuantity', 1, 0, {'maxOccurs': 'unbounded', 'name': 'customerQuantity', 'type': 'customerQuantity'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, customerQuantity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if customerQuantity is None:
            self.customerQuantity = []
        else:
            self.customerQuantity = customerQuantity
        self.customerQuantity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, customerQuantities)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if customerQuantities.subclass:
            return customerQuantities.subclass(*args_, **kwargs_)
        else:
            return customerQuantities(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.customerQuantity
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'customerQuantity':
            obj_ = customerQuantity.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerQuantity.append(obj_)
            obj_.original_tagname_ = 'customerQuantity'
# end class customerQuantities


class customerQuantity(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'customer': MemberSpec_('customer', 'customer', 0, 0, {'name': 'customer', 'type': 'organizationRef'}, None),
        'quantity': MemberSpec_('quantity', ['quantity18p11Type', 'xs:decimal'], 0, 0, {'name': 'quantity', 'type': 'xs:decimal'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, customer=None, quantity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer = customer
        self.customer_nsprefix_ = None
        self.quantity = quantity
        self.validate_quantity18p11Type(self.quantity)
        self.quantity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, customerQuantity)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if customerQuantity.subclass:
            return customerQuantity.subclass(*args_, **kwargs_)
        else:
            return customerQuantity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_quantity18p11Type(self, value):
        result = True
        # Validate type quantity18p11Type, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 29:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on quantity18p11Type' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_quantity18p11Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_quantity18p11Type_patterns_, ))
                result = False
        return result
    validate_quantity18p11Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,11})?)$']]
    def hasContent_(self):
        if (
            self.customer is not None or
            self.quantity is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'customer':
            class_obj_ = self.get_class_obj_(child_, organizationRef)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customer = obj_
            obj_.original_tagname_ = 'customer'
        elif nodeName_ == 'quantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'quantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'quantity')
            self.quantity = fval_
            self.quantity_nsprefix_ = child_.prefix
            # validate type quantity18p11Type
            self.validate_quantity18p11Type(self.quantity)
# end class customerQuantity


class quantity(GeneratedsSuper):
    """Общее количество по объекту закупки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'value': MemberSpec_('value', ['quantity18p11Type', 'xs:decimal'], 0, 0, {'name': 'value', 'type': 'xs:decimal'}, 6),
        'undefined': MemberSpec_('undefined', 'undefined', 0, 0, {'fixed': 'true', 'name': 'undefined', 'type': 'xs:boolean'}, 6),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, value=None, undefined=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.validate_quantity18p11Type(self.value)
        self.value_nsprefix_ = None
        self.undefined = undefined
        self.undefined_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, quantity)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if quantity.subclass:
            return quantity.subclass(*args_, **kwargs_)
        else:
            return quantity(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_quantity18p11Type(self, value):
        result = True
        # Validate type quantity18p11Type, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 29:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on quantity18p11Type' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_quantity18p11Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_quantity18p11Type_patterns_, ))
                result = False
        return result
    validate_quantity18p11Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,11})?)$']]
    def hasContent_(self):
        if (
            self.value is not None or
            self.undefined is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'value')
            fval_ = self.gds_validate_decimal(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type quantity18p11Type
            self.validate_quantity18p11Type(self.value)
        elif nodeName_ == 'undefined':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'undefined')
            ival_ = self.gds_validate_boolean(ival_, node, 'undefined')
            self.undefined = ival_
            self.undefined_nsprefix_ = child_.prefix
# end class quantity


class purchaseIsMaxPriceCurrencyType(GeneratedsSuper):
    """Тип: НМЦК в валюте контракта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'maxPriceCurrency': MemberSpec_('maxPriceCurrency', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'maxPriceCurrency', 'type': 'xs:string'}, None),
        'currency': MemberSpec_('currency', 'currencyCBRFRef', 0, 0, {'name': 'currency', 'type': 'currencyCBRFRef'}, None),
        'currencyRate': MemberSpec_('currencyRate', 'currencyRateType', 0, 1, {'minOccurs': '0', 'name': 'currencyRate', 'type': 'currencyRateType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, maxPriceCurrency=None, currency=None, currencyRate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.maxPriceCurrency = maxPriceCurrency
        self.validate_moneyType(self.maxPriceCurrency)
        self.maxPriceCurrency_nsprefix_ = None
        self.currency = currency
        self.currency_nsprefix_ = None
        self.currencyRate = currencyRate
        self.currencyRate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, purchaseIsMaxPriceCurrencyType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if purchaseIsMaxPriceCurrencyType.subclass:
            return purchaseIsMaxPriceCurrencyType.subclass(*args_, **kwargs_)
        else:
            return purchaseIsMaxPriceCurrencyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.maxPriceCurrency is not None or
            self.currency is not None or
            self.currencyRate is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'maxPriceCurrency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'maxPriceCurrency')
            value_ = self.gds_validate_string(value_, node, 'maxPriceCurrency')
            self.maxPriceCurrency = value_
            self.maxPriceCurrency_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.maxPriceCurrency)
        elif nodeName_ == 'currency':
            obj_ = currencyCBRFRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.currency = obj_
            obj_.original_tagname_ = 'currency'
        elif nodeName_ == 'currencyRate':
            obj_ = currencyRateType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.currencyRate = obj_
            obj_.original_tagname_ = 'currencyRate'
# end class purchaseIsMaxPriceCurrencyType


class preferenseType(GeneratedsSuper):
    """Тип: Преимущество для участников"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'preferenseRequirementInfo': MemberSpec_('preferenseRequirementInfo', 'prefsReqsRef', 0, 0, {'name': 'preferenseRequirementInfo', 'type': 'prefsReqsRef'}, None),
        'prefValue': MemberSpec_('prefValue', ['percentRestr0100Type', 'xs:double'], 0, 1, {'minOccurs': '0', 'name': 'prefValue', 'type': 'xs:double'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, preferenseRequirementInfo=None, prefValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.preferenseRequirementInfo = preferenseRequirementInfo
        self.preferenseRequirementInfo_nsprefix_ = None
        self.prefValue = prefValue
        self.validate_percentRestr0100Type(self.prefValue)
        self.prefValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, preferenseType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if preferenseType.subclass:
            return preferenseType.subclass(*args_, **kwargs_)
        else:
            return preferenseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_percentRestr0100Type(self, value):
        result = True
        # Validate type percentRestr0100Type, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on percentRestr0100Type' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on percentRestr0100Type' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.preferenseRequirementInfo is not None or
            self.prefValue is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'preferenseRequirementInfo':
            obj_ = prefsReqsRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferenseRequirementInfo = obj_
            obj_.original_tagname_ = 'preferenseRequirementInfo'
        elif nodeName_ == 'prefValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'prefValue')
            fval_ = self.gds_validate_double(fval_, node, 'prefValue')
            self.prefValue = fval_
            self.prefValue_nsprefix_ = child_.prefix
            # validate type percentRestr0100Type
            self.validate_percentRestr0100Type(self.prefValue)
# end class preferenseType


class requirement2020Type(GeneratedsSuper):
    """Тип: Требование к участникам с 01.10.2020"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'preferenseRequirementInfo': MemberSpec_('preferenseRequirementInfo', 'prefsReqsRef', 0, 0, {'name': 'preferenseRequirementInfo', 'type': 'prefsReqsRef'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, None),
        'reqValue': MemberSpec_('reqValue', ['percentRestr0100Type', 'xs:double'], 0, 1, {'minOccurs': '0', 'name': 'reqValue', 'type': 'xs:double'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, preferenseRequirementInfo=None, content=None, reqValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.preferenseRequirementInfo = preferenseRequirementInfo
        self.preferenseRequirementInfo_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
        self.reqValue = reqValue
        self.validate_percentRestr0100Type(self.reqValue)
        self.reqValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, requirement2020Type)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if requirement2020Type.subclass:
            return requirement2020Type.subclass(*args_, **kwargs_)
        else:
            return requirement2020Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_percentRestr0100Type(self, value):
        result = True
        # Validate type percentRestr0100Type, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on percentRestr0100Type' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on percentRestr0100Type' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.preferenseRequirementInfo is not None or
            self.content is not None or
            self.reqValue is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'preferenseRequirementInfo':
            obj_ = prefsReqsRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferenseRequirementInfo = obj_
            obj_.original_tagname_ = 'preferenseRequirementInfo'
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
        elif nodeName_ == 'reqValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'reqValue')
            fval_ = self.gds_validate_double(fval_, node, 'reqValue')
            self.reqValue = fval_
            self.reqValue_nsprefix_ = child_.prefix
            # validate type percentRestr0100Type
            self.validate_percentRestr0100Type(self.reqValue)
# end class requirement2020Type


class requirementRestrictionType(GeneratedsSuper):
    """Тип: Требование (ограничение) к участникам"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'preferenseRequirementInfo': MemberSpec_('preferenseRequirementInfo', 'prefsReqsRef', 0, 0, {'name': 'preferenseRequirementInfo', 'type': 'prefsReqsRef'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, preferenseRequirementInfo=None, content=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.preferenseRequirementInfo = preferenseRequirementInfo
        self.preferenseRequirementInfo_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, requirementRestrictionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if requirementRestrictionType.subclass:
            return requirementRestrictionType.subclass(*args_, **kwargs_)
        else:
            return requirementRestrictionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.preferenseRequirementInfo is not None or
            self.content is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'preferenseRequirementInfo':
            obj_ = prefsReqsRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferenseRequirementInfo = obj_
            obj_.original_tagname_ = 'preferenseRequirementInfo'
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
# end class requirementRestrictionType


class requirementWithAddReqsType(GeneratedsSuper):
    """Тип: Требование (ограничение) к участникам (с дополнительными
    требованиями)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'preferenseRequirementInfo': MemberSpec_('preferenseRequirementInfo', 'prefsReqsRef', 0, 0, {'name': 'preferenseRequirementInfo', 'type': 'prefsReqsRef'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, None),
        'addRequirements': MemberSpec_('addRequirements', 'addRequirements', 0, 1, {'minOccurs': '0', 'name': 'addRequirements', 'type': 'addRequirements'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, preferenseRequirementInfo=None, content=None, addRequirements=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.preferenseRequirementInfo = preferenseRequirementInfo
        self.preferenseRequirementInfo_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
        self.addRequirements = addRequirements
        self.addRequirements_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, requirementWithAddReqsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if requirementWithAddReqsType.subclass:
            return requirementWithAddReqsType.subclass(*args_, **kwargs_)
        else:
            return requirementWithAddReqsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.preferenseRequirementInfo is not None or
            self.content is not None or
            self.addRequirements is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'preferenseRequirementInfo':
            obj_ = prefsReqsRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferenseRequirementInfo = obj_
            obj_.original_tagname_ = 'preferenseRequirementInfo'
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
        elif nodeName_ == 'addRequirements':
            obj_ = addRequirements.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.addRequirements = obj_
            obj_.original_tagname_ = 'addRequirements'
# end class requirementWithAddReqsType


class addRequirements(GeneratedsSuper):
    """Дополнительные требования.
    При приеме бизнес-контролем контролируется обязательность заполнения блока
    при заполнения в блоке requirement значений «Требования к участникам
    закупок в соответствии с частью 2 статьи 31 Федерального закона № 44-ФЗ
    (TU44)» или "Требования к участникам закупок в соответствии с частью
    2.1 статьи 31 Федерального закона № 44-ФЗ (ET44312)" """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'addRequirement': MemberSpec_('addRequirement', 'addRequirement', 1, 0, {'maxOccurs': 'unbounded', 'name': 'addRequirement', 'type': 'addRequirement'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, addRequirement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if addRequirement is None:
            self.addRequirement = []
        else:
            self.addRequirement = addRequirement
        self.addRequirement_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, addRequirements)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if addRequirements.subclass:
            return addRequirements.subclass(*args_, **kwargs_)
        else:
            return addRequirements(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.addRequirement
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'addRequirement':
            obj_ = addRequirement.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.addRequirement.append(obj_)
            obj_.original_tagname_ = 'addRequirement'
# end class addRequirements


class addRequirement(GeneratedsSuper):
    """Дополнительное требование (перечень пунктов приложений ПП РФ № 99).
    Может быть указана только ссылка запись справочника "Требования
    (преимущества, ограничения)" (nsiPurchasePreferences) в поле type
    которой указано значение "D" - "Дополнительное требование" и заполнено
    поле parentShortName"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'shortName': MemberSpec_('shortName', ['prefsReqsShortNameType', 'xs:string'], 0, 0, {'name': 'shortName', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, shortName=None, name=None, content=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.shortName = shortName
        self.validate_prefsReqsShortNameType(self.shortName)
        self.shortName_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, addRequirement)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if addRequirement.subclass:
            return addRequirement.subclass(*args_, **kwargs_)
        else:
            return addRequirement(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_prefsReqsShortNameType(self, value):
        result = True
        # Validate type prefsReqsShortNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on prefsReqsShortNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on prefsReqsShortNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.shortName is not None or
            self.name is not None or
            self.content is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'shortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shortName')
            value_ = self.gds_validate_string(value_, node, 'shortName')
            self.shortName = value_
            self.shortName_nsprefix_ = child_.prefix
            # validate type prefsReqsShortNameType
            self.validate_prefsReqsShortNameType(self.shortName)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
# end class addRequirement


class requirement2020WithAddReqsType(GeneratedsSuper):
    """Тип: Требование (ограничение) к участникам (с дополнительными
    требованиями) с 01.10.2020"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'preferenseRequirementInfo': MemberSpec_('preferenseRequirementInfo', 'prefsReqsRef', 0, 0, {'name': 'preferenseRequirementInfo', 'type': 'prefsReqsRef'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, None),
        'reqValue': MemberSpec_('reqValue', ['reqValue', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'reqValue', 'type': 'xs:string'}, None),
        'addRequirements': MemberSpec_('addRequirements', 'addRequirements', 0, 1, {'minOccurs': '0', 'name': 'addRequirements', 'type': 'addRequirements'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, preferenseRequirementInfo=None, content=None, reqValue=None, addRequirements=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.preferenseRequirementInfo = preferenseRequirementInfo
        self.preferenseRequirementInfo_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
        self.reqValue = reqValue
        self.reqValue_nsprefix_ = None
        self.addRequirements = addRequirements
        self.addRequirements_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, requirement2020WithAddReqsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if requirement2020WithAddReqsType.subclass:
            return requirement2020WithAddReqsType.subclass(*args_, **kwargs_)
        else:
            return requirement2020WithAddReqsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.preferenseRequirementInfo is not None or
            self.content is not None or
            self.reqValue is not None or
            self.addRequirements is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'preferenseRequirementInfo':
            obj_ = prefsReqsRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferenseRequirementInfo = obj_
            obj_.original_tagname_ = 'preferenseRequirementInfo'
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
        elif nodeName_ == 'reqValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'reqValue')
            value_ = self.gds_validate_string(value_, node, 'reqValue')
            self.reqValue = value_
            self.reqValue_nsprefix_ = child_.prefix
        elif nodeName_ == 'addRequirements':
            obj_ = addRequirements.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.addRequirements = obj_
            obj_.original_tagname_ = 'addRequirements'
# end class requirement2020WithAddReqsType


class reqValue(GeneratedsSuper):
    """Объём требования (в %)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, reqValue)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if reqValue.subclass:
            return reqValue.subclass(*args_, **kwargs_)
        else:
            return reqValue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_reqValue(self, value):
        result = True
        # Validate type reqValue, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class reqValue


class addRequirementType(GeneratedsSuper):
    """Тип: Дополнительное требование к участникам"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'shortName': MemberSpec_('shortName', ['prefsReqsShortNameType', 'xs:string'], 0, 0, {'name': 'shortName', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, shortName=None, name=None, content=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.shortName = shortName
        self.validate_prefsReqsShortNameType(self.shortName)
        self.shortName_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, addRequirementType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if addRequirementType.subclass:
            return addRequirementType.subclass(*args_, **kwargs_)
        else:
            return addRequirementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_prefsReqsShortNameType(self, value):
        result = True
        # Validate type prefsReqsShortNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on prefsReqsShortNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on prefsReqsShortNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.shortName is not None or
            self.name is not None or
            self.content is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'shortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shortName')
            value_ = self.gds_validate_string(value_, node, 'shortName')
            self.shortName = value_
            self.shortName_nsprefix_ = child_.prefix
            # validate type prefsReqsShortNameType
            self.validate_prefsReqsShortNameType(self.shortName)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
# end class addRequirementType


class personType(GeneratedsSuper):
    """Тип: ФИО"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'lastName': MemberSpec_('lastName', ['nameType', 'xs:string'], 0, 0, {'name': 'lastName', 'type': 'xs:string'}, None),
        'firstName': MemberSpec_('firstName', ['nameType', 'xs:string'], 0, 0, {'name': 'firstName', 'type': 'xs:string'}, None),
        'middleName': MemberSpec_('middleName', ['nameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'middleName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, lastName=None, firstName=None, middleName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.lastName = lastName
        self.validate_nameType(self.lastName)
        self.lastName_nsprefix_ = None
        self.firstName = firstName
        self.validate_nameType(self.firstName)
        self.firstName_nsprefix_ = None
        self.middleName = middleName
        self.validate_nameType(self.middleName)
        self.middleName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, personType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if personType.subclass:
            return personType.subclass(*args_, **kwargs_)
        else:
            return personType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_nameType(self, value):
        result = True
        # Validate type nameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.lastName is not None or
            self.firstName is not None or
            self.middleName is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'lastName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'lastName')
            value_ = self.gds_validate_string(value_, node, 'lastName')
            self.lastName = value_
            self.lastName_nsprefix_ = child_.prefix
            # validate type nameType
            self.validate_nameType(self.lastName)
        elif nodeName_ == 'firstName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstName')
            value_ = self.gds_validate_string(value_, node, 'firstName')
            self.firstName = value_
            self.firstName_nsprefix_ = child_.prefix
            # validate type nameType
            self.validate_nameType(self.firstName)
        elif nodeName_ == 'middleName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'middleName')
            value_ = self.gds_validate_string(value_, node, 'middleName')
            self.middleName = value_
            self.middleName_nsprefix_ = child_.prefix
            # validate type nameType
            self.validate_nameType(self.middleName)
# end class personType


class restrictionType(GeneratedsSuper):
    """Тип: Ограничение для участников"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'preferenseRequirementInfo': MemberSpec_('preferenseRequirementInfo', 'prefsReqsRef', 0, 0, {'name': 'preferenseRequirementInfo', 'type': 'prefsReqsRef'}, None),
        'content': MemberSpec_('content', ['text4000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'content', 'type': 'xs:string'}, 7),
        'restrictionsSt14': MemberSpec_('restrictionsSt14', 'restrictionSt14Type', 0, 1, {'minOccurs': '0', 'name': 'restrictionsSt14', 'type': 'restrictionSt14Type'}, 7),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, preferenseRequirementInfo=None, content=None, restrictionsSt14=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.preferenseRequirementInfo = preferenseRequirementInfo
        self.preferenseRequirementInfo_nsprefix_ = None
        self.content = content
        self.validate_text4000Type(self.content)
        self.content_nsprefix_ = None
        self.restrictionsSt14 = restrictionsSt14
        self.restrictionsSt14_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, restrictionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if restrictionType.subclass:
            return restrictionType.subclass(*args_, **kwargs_)
        else:
            return restrictionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.preferenseRequirementInfo is not None or
            self.content is not None or
            self.restrictionsSt14 is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'preferenseRequirementInfo':
            obj_ = prefsReqsRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.preferenseRequirementInfo = obj_
            obj_.original_tagname_ = 'preferenseRequirementInfo'
        elif nodeName_ == 'content':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'content')
            value_ = self.gds_validate_string(value_, node, 'content')
            self.content = value_
            self.content_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.content)
        elif nodeName_ == 'restrictionsSt14':
            obj_ = restrictionSt14Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.restrictionsSt14 = obj_
            obj_.original_tagname_ = 'restrictionsSt14'
# end class restrictionType


class restrictionSt14Type(GeneratedsSuper):
    """Тип: Сведения по запрету, ограничению участия, условию допуска"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'restrictionSt14': MemberSpec_('restrictionSt14', 'restrictionSt14', 1, 0, {'maxOccurs': 'unbounded', 'name': 'restrictionSt14', 'type': 'restrictionSt14'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, restrictionSt14=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if restrictionSt14 is None:
            self.restrictionSt14 = []
        else:
            self.restrictionSt14 = restrictionSt14
        self.restrictionSt14_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, restrictionSt14Type)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if restrictionSt14Type.subclass:
            return restrictionSt14Type.subclass(*args_, **kwargs_)
        else:
            return restrictionSt14Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.restrictionSt14
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'restrictionSt14':
            obj_ = restrictionSt14.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.restrictionSt14.append(obj_)
            obj_.original_tagname_ = 'restrictionSt14'
# end class restrictionSt14Type


class restrictionSt14(GeneratedsSuper):
    """Сведения по запрету, ограничению участия, условию допуска"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'requirementsType': MemberSpec_('requirementsType', 'requirementsType', 0, 0, {'name': 'requirementsType', 'type': 'requirementsType'}, None),
        'NPAInfo': MemberSpec_('NPAInfo', 'NPASt14Ref', 0, 0, {'name': 'NPAInfo', 'type': 'NPASt14Ref'}, None),
        'exception': MemberSpec_('exception', 'exception', 0, 1, {'minOccurs': '0', 'name': 'exception', 'type': 'exception'}, None),
        'note': MemberSpec_('note', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'note', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, requirementsType=None, NPAInfo=None, exception=None, note=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.requirementsType = requirementsType
        self.requirementsType_nsprefix_ = None
        self.NPAInfo = NPAInfo
        self.NPAInfo_nsprefix_ = None
        self.exception = exception
        self.exception_nsprefix_ = None
        self.note = note
        self.validate_text2000Type(self.note)
        self.note_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, restrictionSt14)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if restrictionSt14.subclass:
            return restrictionSt14.subclass(*args_, **kwargs_)
        else:
            return restrictionSt14(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.requirementsType is not None or
            self.NPAInfo is not None or
            self.exception is not None or
            self.note is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'requirementsType':
            obj_ = requirementsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.requirementsType = obj_
            obj_.original_tagname_ = 'requirementsType'
        elif nodeName_ == 'NPAInfo':
            obj_ = NPASt14Ref.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.NPAInfo = obj_
            obj_.original_tagname_ = 'NPAInfo'
        elif nodeName_ == 'exception':
            obj_ = exception.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.exception = obj_
            obj_.original_tagname_ = 'exception'
        elif nodeName_ == 'note':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'note')
            value_ = self.gds_validate_string(value_, node, 'note')
            self.note = value_
            self.note_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.note)
# end class restrictionSt14


class requirementsType(GeneratedsSuper):
    """Виды требований"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'requirementType': MemberSpec_('requirementType', 'requirementType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'requirementType', 'type': 'requirementType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, requirementType=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if requirementType is None:
            self.requirementType = []
        else:
            self.requirementType = requirementType
        self.requirementType_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, requirementsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if requirementsType.subclass:
            return requirementsType.subclass(*args_, **kwargs_)
        else:
            return requirementsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.requirementType
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'requirementType':
            obj_ = requirementType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.requirementType.append(obj_)
            obj_.original_tagname_ = 'requirementType'
# end class requirementsType


class requirementType(GeneratedsSuper):
    """Вид требования"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', ['type', 'xs:string'], 0, 0, {'name': 'type', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, type_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = type_
        self.type__nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, requirementType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if requirementType.subclass:
            return requirementType.subclass(*args_, **kwargs_)
        else:
            return requirementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.type_ is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'type')
            value_ = self.gds_validate_string(value_, node, 'type')
            self.type_ = value_
            self.type_nsprefix_ = child_.prefix
# end class requirementType


class type_(GeneratedsSuper):
    """Вид требования:
    AC - условия допуска;
    RA - ограничение допуска;
    BAN - запрет."""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, type_)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if type_.subclass:
            return type_.subclass(*args_, **kwargs_)
        else:
            return type_(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_type(self, value):
        result = True
        # Validate type type, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class type_


class exception(GeneratedsSuper):
    """Присутствуют обстоятельства, допускающие исключение, влекущее
    неприменение запрета, ограничения допуска"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'imposibilityBan': MemberSpec_('imposibilityBan', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'imposibilityBan', 'type': 'xs:boolean'}, None),
        'imposibilityBanReason': MemberSpec_('imposibilityBanReason', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'imposibilityBanReason', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, imposibilityBan=None, imposibilityBanReason=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.imposibilityBan = imposibilityBan
        self.imposibilityBan_nsprefix_ = None
        self.imposibilityBanReason = imposibilityBanReason
        self.validate_text2000Type(self.imposibilityBanReason)
        self.imposibilityBanReason_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, exception)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if exception.subclass:
            return exception.subclass(*args_, **kwargs_)
        else:
            return exception(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.imposibilityBan is not None or
            self.imposibilityBanReason is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'imposibilityBan':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'imposibilityBan')
            ival_ = self.gds_validate_boolean(ival_, node, 'imposibilityBan')
            self.imposibilityBan = ival_
            self.imposibilityBan_nsprefix_ = child_.prefix
        elif nodeName_ == 'imposibilityBanReason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'imposibilityBanReason')
            value_ = self.gds_validate_string(value_, node, 'imposibilityBanReason')
            self.imposibilityBanReason = value_
            self.imposibilityBanReason_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.imposibilityBanReason)
# end class exception


class signatureType(GeneratedsSuper):
    """Тип: Электронная подписьТип электронной подписи:
    CAdES-BES;
    CAdES-A"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'type_': MemberSpec_('type_', 'base:signatureType', 0, 1, {'use': 'optional'}),
        'valueOf_': MemberSpec_('valueOf_', ['xs:base64Binary', 'signatureType'], 0),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['valueOf_']
    subclass = None
    superclass = None
    def __init__(self, type_=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, signatureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if signatureType.subclass:
            return signatureType.subclass(*args_, **kwargs_)
        else:
            return signatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_signatureType(self, value):
        # Validate type base:signatureType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CAdES-BES', 'CAdES-A']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on signatureType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.add('type')
            self.type_ = value
            self.validate_signatureType(self.type_)    # validate type signatureType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class signatureType


class violationType(GeneratedsSuper):
    """Тип: Нарушение приема"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'errCode': MemberSpec_('errCode', ['errorCodeType', 'xs:string'], 0, 0, {'name': 'errCode', 'type': 'xs:string'}, None),
        'level': MemberSpec_('level', ['violationLevelType', 'xs:string'], 0, 0, {'name': 'level', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text200Type', 'xs:string'], 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'description': MemberSpec_('description', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'description', 'type': 'xs:string'}, None),
        'fullErrorLog': MemberSpec_('fullErrorLog', 'xs:base64Binary', 0, 1, {'minOccurs': '0', 'name': 'fullErrorLog', 'type': 'xs:base64Binary'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, errCode=None, level=None, name=None, description=None, fullErrorLog=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.errCode = errCode
        self.validate_errorCodeType(self.errCode)
        self.errCode_nsprefix_ = None
        self.level = level
        self.validate_violationLevelType(self.level)
        self.level_nsprefix_ = None
        self.name = name
        self.validate_text200Type(self.name)
        self.name_nsprefix_ = None
        self.description = description
        self.validate_text2000Type(self.description)
        self.description_nsprefix_ = None
        self.fullErrorLog = fullErrorLog
        self.fullErrorLog_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, violationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if violationType.subclass:
            return violationType.subclass(*args_, **kwargs_)
        else:
            return violationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_errorCodeType(self, value):
        result = True
        # Validate type errorCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on errorCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on errorCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_violationLevelType(self, value):
        result = True
        # Validate type violationLevelType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['error', 'warning']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on violationLevelType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text200Type(self, value):
        result = True
        # Validate type text200Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 200:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text200Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text200Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.errCode is not None or
            self.level is not None or
            self.name is not None or
            self.description is not None or
            self.fullErrorLog is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'errCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'errCode')
            value_ = self.gds_validate_string(value_, node, 'errCode')
            self.errCode = value_
            self.errCode_nsprefix_ = child_.prefix
            # validate type errorCodeType
            self.validate_errorCodeType(self.errCode)
        elif nodeName_ == 'level':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'level')
            value_ = self.gds_validate_string(value_, node, 'level')
            self.level = value_
            self.level_nsprefix_ = child_.prefix
            # validate type violationLevelType
            self.validate_violationLevelType(self.level)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text200Type
            self.validate_text200Type(self.name)
        elif nodeName_ == 'description':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'description')
            value_ = self.gds_validate_string(value_, node, 'description')
            self.description = value_
            self.description_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.description)
        elif nodeName_ == 'fullErrorLog':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'fullErrorLog')
            else:
                bval_ = None
            self.fullErrorLog = bval_
            self.fullErrorLog_nsprefix_ = child_.prefix
# end class violationType


class financeResourcesType(GeneratedsSuper):
    """Тип: Финансовое обеспечение закупки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'total': MemberSpec_('total', ['moneyMaxLengthToPoint18Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'total', 'type': 'xs:string'}, None),
        'currentYear': MemberSpec_('currentYear', ['moneyMaxLengthToPoint18Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'currentYear', 'type': 'xs:string'}, None),
        'firstYear': MemberSpec_('firstYear', ['moneyMaxLengthToPoint18Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'firstYear', 'type': 'xs:string'}, None),
        'secondYear': MemberSpec_('secondYear', ['moneyMaxLengthToPoint18Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'secondYear', 'type': 'xs:string'}, None),
        'subsecYears': MemberSpec_('subsecYears', ['moneyMaxLengthToPoint18Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'subsecYears', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, total=None, currentYear=None, firstYear=None, secondYear=None, subsecYears=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.total = total
        self.validate_moneyMaxLengthToPoint18Type(self.total)
        self.total_nsprefix_ = None
        self.currentYear = currentYear
        self.validate_moneyMaxLengthToPoint18Type(self.currentYear)
        self.currentYear_nsprefix_ = None
        self.firstYear = firstYear
        self.validate_moneyMaxLengthToPoint18Type(self.firstYear)
        self.firstYear_nsprefix_ = None
        self.secondYear = secondYear
        self.validate_moneyMaxLengthToPoint18Type(self.secondYear)
        self.secondYear_nsprefix_ = None
        self.subsecYears = subsecYears
        self.validate_moneyMaxLengthToPoint18Type(self.subsecYears)
        self.subsecYears_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, financeResourcesType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if financeResourcesType.subclass:
            return financeResourcesType.subclass(*args_, **kwargs_)
        else:
            return financeResourcesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_moneyMaxLengthToPoint18Type(self, value):
        result = True
        # Validate type moneyMaxLengthToPoint18Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyMaxLengthToPoint18Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyMaxLengthToPoint18Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyMaxLengthToPoint18Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyMaxLengthToPoint18Type_patterns_, ))
                result = False
        return result
    validate_moneyMaxLengthToPoint18Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.total is not None or
            self.currentYear is not None or
            self.firstYear is not None or
            self.secondYear is not None or
            self.subsecYears is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'total':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'total')
            value_ = self.gds_validate_string(value_, node, 'total')
            self.total = value_
            self.total_nsprefix_ = child_.prefix
            # validate type moneyMaxLengthToPoint18Type
            self.validate_moneyMaxLengthToPoint18Type(self.total)
        elif nodeName_ == 'currentYear':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'currentYear')
            value_ = self.gds_validate_string(value_, node, 'currentYear')
            self.currentYear = value_
            self.currentYear_nsprefix_ = child_.prefix
            # validate type moneyMaxLengthToPoint18Type
            self.validate_moneyMaxLengthToPoint18Type(self.currentYear)
        elif nodeName_ == 'firstYear':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'firstYear')
            value_ = self.gds_validate_string(value_, node, 'firstYear')
            self.firstYear = value_
            self.firstYear_nsprefix_ = child_.prefix
            # validate type moneyMaxLengthToPoint18Type
            self.validate_moneyMaxLengthToPoint18Type(self.firstYear)
        elif nodeName_ == 'secondYear':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'secondYear')
            value_ = self.gds_validate_string(value_, node, 'secondYear')
            self.secondYear = value_
            self.secondYear_nsprefix_ = child_.prefix
            # validate type moneyMaxLengthToPoint18Type
            self.validate_moneyMaxLengthToPoint18Type(self.secondYear)
        elif nodeName_ == 'subsecYears':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'subsecYears')
            value_ = self.gds_validate_string(value_, node, 'subsecYears')
            self.subsecYears = value_
            self.subsecYears_nsprefix_ = child_.prefix
            # validate type moneyMaxLengthToPoint18Type
            self.validate_moneyMaxLengthToPoint18Type(self.subsecYears)
# end class financeResourcesType


class KVRFinancingType(GeneratedsSuper):
    """Тип: Детализация по коду КВР"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'KVR': MemberSpec_('KVR', 'KVR', 0, 0, {'name': 'KVR', 'type': 'KVRRef'}, None),
        'KVRYearsInfo': MemberSpec_('KVRYearsInfo', 'financeResourcesType', 0, 0, {'name': 'KVRYearsInfo', 'type': 'financeResourcesType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, KVR=None, KVRYearsInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.KVR = KVR
        self.KVR_nsprefix_ = None
        self.KVRYearsInfo = KVRYearsInfo
        self.KVRYearsInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KVRFinancingType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KVRFinancingType.subclass:
            return KVRFinancingType.subclass(*args_, **kwargs_)
        else:
            return KVRFinancingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.KVR is not None or
            self.KVRYearsInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KVR':
            obj_ = KVRRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KVR = obj_
            obj_.original_tagname_ = 'KVR'
        elif nodeName_ == 'KVRYearsInfo':
            obj_ = financeResourcesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KVRYearsInfo = obj_
            obj_.original_tagname_ = 'KVRYearsInfo'
# end class KVRFinancingType


class KVRFinancingsType(GeneratedsSuper):
    """Тип: Детализация по кодам КВР"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'currentYear': MemberSpec_('currentYear', ['yearType', 'xs:int'], 0, 1, {'minOccurs': '0', 'name': 'currentYear', 'type': 'xs:int'}, None),
        'KVRInfo': MemberSpec_('KVRInfo', 'KVRFinancingType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'KVRInfo', 'type': 'KVRFinancingType'}, None),
        'totalSum': MemberSpec_('totalSum', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'totalSum', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, currentYear=None, KVRInfo=None, totalSum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.currentYear = currentYear
        self.validate_yearType(self.currentYear)
        self.currentYear_nsprefix_ = None
        if KVRInfo is None:
            self.KVRInfo = []
        else:
            self.KVRInfo = KVRInfo
        self.KVRInfo_nsprefix_ = None
        self.totalSum = totalSum
        self.validate_moneyType(self.totalSum)
        self.totalSum_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KVRFinancingsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KVRFinancingsType.subclass:
            return KVRFinancingsType.subclass(*args_, **kwargs_)
        else:
            return KVRFinancingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_yearType(self, value):
        result = True
        # Validate type yearType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_yearType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_yearType_patterns_, ))
                result = False
        return result
    validate_yearType_patterns_ = [['^(\\d{4})$']]
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.currentYear is not None or
            self.KVRInfo or
            self.totalSum is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'currentYear' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'currentYear')
            ival_ = self.gds_validate_integer(ival_, node, 'currentYear')
            self.currentYear = ival_
            self.currentYear_nsprefix_ = child_.prefix
            # validate type yearType
            self.validate_yearType(self.currentYear)
        elif nodeName_ == 'KVRInfo':
            obj_ = KVRFinancingType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KVRInfo.append(obj_)
            obj_.original_tagname_ = 'KVRInfo'
        elif nodeName_ == 'totalSum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'totalSum')
            value_ = self.gds_validate_string(value_, node, 'totalSum')
            self.totalSum = value_
            self.totalSum_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.totalSum)
# end class KVRFinancingsType


class targetArticleFinancingType(GeneratedsSuper):
    """Тип: Детализация по целевой статье"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'targetArticle': MemberSpec_('targetArticle', ['targetArticleType', 'xs:string'], 0, 0, {'name': 'targetArticle', 'type': 'xs:string'}, None),
        'targetArticleYearsInfo': MemberSpec_('targetArticleYearsInfo', 'financeResourcesType', 0, 0, {'name': 'targetArticleYearsInfo', 'type': 'financeResourcesType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, targetArticle=None, targetArticleYearsInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.targetArticle = targetArticle
        self.validate_targetArticleType(self.targetArticle)
        self.targetArticle_nsprefix_ = None
        self.targetArticleYearsInfo = targetArticleYearsInfo
        self.targetArticleYearsInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, targetArticleFinancingType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if targetArticleFinancingType.subclass:
            return targetArticleFinancingType.subclass(*args_, **kwargs_)
        else:
            return targetArticleFinancingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_targetArticleType(self, value):
        result = True
        # Validate type targetArticleType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on targetArticleType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.targetArticle is not None or
            self.targetArticleYearsInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'targetArticle':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'targetArticle')
            value_ = self.gds_validate_string(value_, node, 'targetArticle')
            self.targetArticle = value_
            self.targetArticle_nsprefix_ = child_.prefix
            # validate type targetArticleType
            self.validate_targetArticleType(self.targetArticle)
        elif nodeName_ == 'targetArticleYearsInfo':
            obj_ = financeResourcesType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.targetArticleYearsInfo = obj_
            obj_.original_tagname_ = 'targetArticleYearsInfo'
# end class targetArticleFinancingType


class targetArticleFinancingsType(GeneratedsSuper):
    """Тип: Детализация по целевым статьям"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'currentYear': MemberSpec_('currentYear', ['yearType', 'xs:int'], 0, 1, {'minOccurs': '0', 'name': 'currentYear', 'type': 'xs:int'}, None),
        'targetArticleInfo': MemberSpec_('targetArticleInfo', 'targetArticleFinancingType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'targetArticleInfo', 'type': 'targetArticleFinancingType'}, None),
        'totalSum': MemberSpec_('totalSum', ['moneyType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'totalSum', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, currentYear=None, targetArticleInfo=None, totalSum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.currentYear = currentYear
        self.validate_yearType(self.currentYear)
        self.currentYear_nsprefix_ = None
        if targetArticleInfo is None:
            self.targetArticleInfo = []
        else:
            self.targetArticleInfo = targetArticleInfo
        self.targetArticleInfo_nsprefix_ = None
        self.totalSum = totalSum
        self.validate_moneyType(self.totalSum)
        self.totalSum_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, targetArticleFinancingsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if targetArticleFinancingsType.subclass:
            return targetArticleFinancingsType.subclass(*args_, **kwargs_)
        else:
            return targetArticleFinancingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_yearType(self, value):
        result = True
        # Validate type yearType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_yearType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_yearType_patterns_, ))
                result = False
        return result
    validate_yearType_patterns_ = [['^(\\d{4})$']]
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.currentYear is not None or
            self.targetArticleInfo or
            self.totalSum is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'currentYear' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'currentYear')
            ival_ = self.gds_validate_integer(ival_, node, 'currentYear')
            self.currentYear = ival_
            self.currentYear_nsprefix_ = child_.prefix
            # validate type yearType
            self.validate_yearType(self.currentYear)
        elif nodeName_ == 'targetArticleInfo':
            obj_ = targetArticleFinancingType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.targetArticleInfo.append(obj_)
            obj_.original_tagname_ = 'targetArticleInfo'
        elif nodeName_ == 'totalSum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'totalSum')
            value_ = self.gds_validate_string(value_, node, 'totalSum')
            self.totalSum = value_
            self.totalSum_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.totalSum)
# end class targetArticleFinancingsType


class control99CustomerInfoType(GeneratedsSuper):
    """Тип: Сведения о заказчике в ПЗ/ПГ для контроля по 99 статье"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'regNum': MemberSpec_('regNum', ['spzNumType', 'xs:string'], 0, 0, {'name': 'regNum', 'type': 'xs:string'}, None),
        'consRegistryNum': MemberSpec_('consRegistryNum', ['consRegistryNumType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'consRegistryNum', 'type': 'xs:string'}, None),
        'fullName': MemberSpec_('fullName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullName', 'type': 'xs:string'}, None),
        'INN': MemberSpec_('INN', ['innType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'INN', 'type': 'xs:string'}, None),
        'KPP': MemberSpec_('KPP', ['kppType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'KPP', 'type': 'xs:string'}, None),
        'OKFS': MemberSpec_('OKFS', 'OKFSRef', 0, 1, {'minOccurs': '0', 'name': 'OKFS', 'type': 'OKFSRef'}, None),
        'orgBudget': MemberSpec_('orgBudget', 'budgetFundsContractRef', 0, 1, {'minOccurs': '0', 'name': 'orgBudget', 'type': 'budgetFundsContractRef'}, None),
        'factAddress': MemberSpec_('factAddress', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'factAddress', 'type': 'xs:string'}, None),
        'phone': MemberSpec_('phone', ['phoneType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'phone', 'type': 'xs:string'}, None),
        'eMail': MemberSpec_('eMail', ['eMailType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'eMail', 'type': 'xs:string'}, None),
        'OKOPF': MemberSpec_('OKOPF', 'OKOPF', 0, 1, {'minOccurs': '0', 'name': 'OKOPF', 'type': 'OKOPFRef'}, None),
        'OKTMO': MemberSpec_('OKTMO', 'OKTMORef', 0, 1, {'minOccurs': '0', 'name': 'OKTMO', 'type': 'OKTMORef'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, regNum=None, consRegistryNum=None, fullName=None, INN=None, KPP=None, OKFS=None, orgBudget=None, factAddress=None, phone=None, eMail=None, OKOPF=None, OKTMO=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.regNum = regNum
        self.validate_spzNumType(self.regNum)
        self.regNum_nsprefix_ = None
        self.consRegistryNum = consRegistryNum
        self.validate_consRegistryNumType(self.consRegistryNum)
        self.consRegistryNum_nsprefix_ = None
        self.fullName = fullName
        self.validate_text2000Type(self.fullName)
        self.fullName_nsprefix_ = None
        self.INN = INN
        self.validate_innType(self.INN)
        self.INN_nsprefix_ = None
        self.KPP = KPP
        self.validate_kppType(self.KPP)
        self.KPP_nsprefix_ = None
        self.OKFS = OKFS
        self.OKFS_nsprefix_ = None
        self.orgBudget = orgBudget
        self.orgBudget_nsprefix_ = None
        self.factAddress = factAddress
        self.validate_text2000Type(self.factAddress)
        self.factAddress_nsprefix_ = None
        self.phone = phone
        self.validate_phoneType(self.phone)
        self.phone_nsprefix_ = None
        self.eMail = eMail
        self.validate_eMailType(self.eMail)
        self.eMail_nsprefix_ = None
        self.OKOPF = OKOPF
        self.OKOPF_nsprefix_ = None
        self.OKTMO = OKTMO
        self.OKTMO_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, control99CustomerInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if control99CustomerInfoType.subclass:
            return control99CustomerInfoType.subclass(*args_, **kwargs_)
        else:
            return control99CustomerInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_spzNumType(self, value):
        result = True
        # Validate type spzNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_spzNumType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_spzNumType_patterns_, ))
                result = False
        return result
    validate_spzNumType_patterns_ = [['^(\\d{11})$']]
    def validate_consRegistryNumType(self, value):
        result = True
        # Validate type consRegistryNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on consRegistryNumType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_innType(self, value):
        result = True
        # Validate type innType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on innType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_innType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_innType_patterns_, ))
                result = False
        return result
    validate_innType_patterns_ = [['^(\\d{1,12})$']]
    def validate_kppType(self, value):
        result = True
        # Validate type kppType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on kppType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_phoneType(self, value):
        result = True
        # Validate type phoneType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on phoneType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_eMailType(self, value):
        result = True
        # Validate type eMailType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on eMailType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.regNum is not None or
            self.consRegistryNum is not None or
            self.fullName is not None or
            self.INN is not None or
            self.KPP is not None or
            self.OKFS is not None or
            self.orgBudget is not None or
            self.factAddress is not None or
            self.phone is not None or
            self.eMail is not None or
            self.OKOPF is not None or
            self.OKTMO is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'regNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'regNum')
            value_ = self.gds_validate_string(value_, node, 'regNum')
            self.regNum = value_
            self.regNum_nsprefix_ = child_.prefix
            # validate type spzNumType
            self.validate_spzNumType(self.regNum)
        elif nodeName_ == 'consRegistryNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'consRegistryNum')
            value_ = self.gds_validate_string(value_, node, 'consRegistryNum')
            self.consRegistryNum = value_
            self.consRegistryNum_nsprefix_ = child_.prefix
            # validate type consRegistryNumType
            self.validate_consRegistryNumType(self.consRegistryNum)
        elif nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.fullName)
        elif nodeName_ == 'INN':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'INN')
            value_ = self.gds_validate_string(value_, node, 'INN')
            self.INN = value_
            self.INN_nsprefix_ = child_.prefix
            # validate type innType
            self.validate_innType(self.INN)
        elif nodeName_ == 'KPP':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'KPP')
            value_ = self.gds_validate_string(value_, node, 'KPP')
            self.KPP = value_
            self.KPP_nsprefix_ = child_.prefix
            # validate type kppType
            self.validate_kppType(self.KPP)
        elif nodeName_ == 'OKFS':
            obj_ = OKFSRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKFS = obj_
            obj_.original_tagname_ = 'OKFS'
        elif nodeName_ == 'orgBudget':
            obj_ = budgetFundsContractRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.orgBudget = obj_
            obj_.original_tagname_ = 'orgBudget'
        elif nodeName_ == 'factAddress':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'factAddress')
            value_ = self.gds_validate_string(value_, node, 'factAddress')
            self.factAddress = value_
            self.factAddress_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.factAddress)
        elif nodeName_ == 'phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone')
            value_ = self.gds_validate_string(value_, node, 'phone')
            self.phone = value_
            self.phone_nsprefix_ = child_.prefix
            # validate type phoneType
            self.validate_phoneType(self.phone)
        elif nodeName_ == 'eMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eMail')
            value_ = self.gds_validate_string(value_, node, 'eMail')
            self.eMail = value_
            self.eMail_nsprefix_ = child_.prefix
            # validate type eMailType
            self.validate_eMailType(self.eMail)
        elif nodeName_ == 'OKOPF':
            obj_ = OKOPFRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKOPF = obj_
            obj_.original_tagname_ = 'OKOPF'
        elif nodeName_ == 'OKTMO':
            obj_ = OKTMORef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKTMO = obj_
            obj_.original_tagname_ = 'OKTMO'
# end class control99CustomerInfoType


class control99ControlAuthorityInfoType(GeneratedsSuper):
    """Тип: Сведения об органе контроля для контроля по 99 статье"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'regNum': MemberSpec_('regNum', ['spzNumType', 'xs:string'], 0, 0, {'name': 'regNum', 'type': 'xs:string'}, None),
        'consRegistryNum': MemberSpec_('consRegistryNum', ['consRegistryNumType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'consRegistryNum', 'type': 'xs:string'}, None),
        'fullName': MemberSpec_('fullName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullName', 'type': 'xs:string'}, None),
        'INN': MemberSpec_('INN', ['innType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'INN', 'type': 'xs:string'}, None),
        'KPP': MemberSpec_('KPP', ['kppType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'KPP', 'type': 'xs:string'}, None),
        'IKU': MemberSpec_('IKU', ['ikuType', 'xs:string'], 0, 0, {'name': 'IKU', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, regNum=None, consRegistryNum=None, fullName=None, INN=None, KPP=None, IKU=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.regNum = regNum
        self.validate_spzNumType(self.regNum)
        self.regNum_nsprefix_ = None
        self.consRegistryNum = consRegistryNum
        self.validate_consRegistryNumType(self.consRegistryNum)
        self.consRegistryNum_nsprefix_ = None
        self.fullName = fullName
        self.validate_text2000Type(self.fullName)
        self.fullName_nsprefix_ = None
        self.INN = INN
        self.validate_innType(self.INN)
        self.INN_nsprefix_ = None
        self.KPP = KPP
        self.validate_kppType(self.KPP)
        self.KPP_nsprefix_ = None
        self.IKU = IKU
        self.validate_ikuType(self.IKU)
        self.IKU_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, control99ControlAuthorityInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if control99ControlAuthorityInfoType.subclass:
            return control99ControlAuthorityInfoType.subclass(*args_, **kwargs_)
        else:
            return control99ControlAuthorityInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_spzNumType(self, value):
        result = True
        # Validate type spzNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_spzNumType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_spzNumType_patterns_, ))
                result = False
        return result
    validate_spzNumType_patterns_ = [['^(\\d{11})$']]
    def validate_consRegistryNumType(self, value):
        result = True
        # Validate type consRegistryNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on consRegistryNumType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_innType(self, value):
        result = True
        # Validate type innType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on innType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_innType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_innType_patterns_, ))
                result = False
        return result
    validate_innType_patterns_ = [['^(\\d{1,12})$']]
    def validate_kppType(self, value):
        result = True
        # Validate type kppType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 9:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on kppType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ikuType(self, value):
        result = True
        # Validate type ikuType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_ikuType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ikuType_patterns_, ))
                result = False
        return result
    validate_ikuType_patterns_ = [['^(\\d{20})$']]
    def hasContent_(self):
        if (
            self.regNum is not None or
            self.consRegistryNum is not None or
            self.fullName is not None or
            self.INN is not None or
            self.KPP is not None or
            self.IKU is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'regNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'regNum')
            value_ = self.gds_validate_string(value_, node, 'regNum')
            self.regNum = value_
            self.regNum_nsprefix_ = child_.prefix
            # validate type spzNumType
            self.validate_spzNumType(self.regNum)
        elif nodeName_ == 'consRegistryNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'consRegistryNum')
            value_ = self.gds_validate_string(value_, node, 'consRegistryNum')
            self.consRegistryNum = value_
            self.consRegistryNum_nsprefix_ = child_.prefix
            # validate type consRegistryNumType
            self.validate_consRegistryNumType(self.consRegistryNum)
        elif nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.fullName)
        elif nodeName_ == 'INN':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'INN')
            value_ = self.gds_validate_string(value_, node, 'INN')
            self.INN = value_
            self.INN_nsprefix_ = child_.prefix
            # validate type innType
            self.validate_innType(self.INN)
        elif nodeName_ == 'KPP':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'KPP')
            value_ = self.gds_validate_string(value_, node, 'KPP')
            self.KPP = value_
            self.KPP_nsprefix_ = child_.prefix
            # validate type kppType
            self.validate_kppType(self.KPP)
        elif nodeName_ == 'IKU':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IKU')
            value_ = self.gds_validate_string(value_, node, 'IKU')
            self.IKU = value_
            self.IKU_nsprefix_ = child_.prefix
            # validate type ikuType
            self.validate_ikuType(self.IKU)
# end class control99ControlAuthorityInfoType


class controlDocumentsInfo(GeneratedsSuper):
    """Сведения о документах, содержащих информацию для осуществления
    контроля"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'controlDocumentInfo': MemberSpec_('controlDocumentInfo', 'control99DocumentObjectType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'controlDocumentInfo', 'type': 'control99DocumentObjectType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, controlDocumentInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if controlDocumentInfo is None:
            self.controlDocumentInfo = []
        else:
            self.controlDocumentInfo = controlDocumentInfo
        self.controlDocumentInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, controlDocumentsInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if controlDocumentsInfo.subclass:
            return controlDocumentsInfo.subclass(*args_, **kwargs_)
        else:
            return controlDocumentsInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.controlDocumentInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'controlDocumentInfo':
            class_obj_ = self.get_class_obj_(child_, control99DocumentObjectType)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.controlDocumentInfo.append(obj_)
            obj_.original_tagname_ = 'controlDocumentInfo'
# end class controlDocumentsInfo


class control99DocumentObjectType(GeneratedsSuper):
    """Тип: Документ, содержащий информацию об объекте контроля по 99 статье"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'date': MemberSpec_('date', 'xs:dateTime', 0, 1, {'minOccurs': '0', 'name': 'date', 'type': 'xs:dateTime'}, None),
        'number': MemberSpec_('number', ['control99ControlDocNumberType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'number', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, name=None, date=None, number=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        if isinstance(date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = date
        self.date = initvalue_
        self.date_nsprefix_ = None
        self.number = number
        self.validate_control99ControlDocNumberType(self.number)
        self.number_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, control99DocumentObjectType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if control99DocumentObjectType.subclass:
            return control99DocumentObjectType.subclass(*args_, **kwargs_)
        else:
            return control99DocumentObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_control99ControlDocNumberType(self, value):
        result = True
        # Validate type control99ControlDocNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on control99ControlDocNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on control99ControlDocNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.name is not None or
            self.date is not None or
            self.number is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'date':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.date = dval_
            self.date_nsprefix_ = child_.prefix
        elif nodeName_ == 'number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'number')
            value_ = self.gds_validate_string(value_, node, 'number')
            self.number = value_
            self.number_nsprefix_ = child_.prefix
            # validate type control99ControlDocNumberType
            self.validate_control99ControlDocNumberType(self.number)
# end class control99DocumentObjectType


class control99ResponsibleType(GeneratedsSuper):
    """Тип: Ответственный исполнитель для контроля по 99 статье"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', ['control99HeadNameType', 'xs:string'], 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'position': MemberSpec_('position', ['positionType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'position', 'type': 'xs:string'}, None),
        'signDate': MemberSpec_('signDate', 'xs:dateTime', 0, 1, {'minOccurs': '0', 'name': 'signDate', 'type': 'xs:dateTime'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, name=None, position=None, signDate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_control99HeadNameType(self.name)
        self.name_nsprefix_ = None
        self.position = position
        self.validate_positionType(self.position)
        self.position_nsprefix_ = None
        if isinstance(signDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(signDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = signDate
        self.signDate = initvalue_
        self.signDate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, control99ResponsibleType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if control99ResponsibleType.subclass:
            return control99ResponsibleType.subclass(*args_, **kwargs_)
        else:
            return control99ResponsibleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_control99HeadNameType(self, value):
        result = True
        # Validate type control99HeadNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 180:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on control99HeadNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on control99HeadNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_positionType(self, value):
        result = True
        # Validate type positionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 256:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on positionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on positionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.name is not None or
            self.position is not None or
            self.signDate is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type control99HeadNameType
            self.validate_control99HeadNameType(self.name)
        elif nodeName_ == 'position':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'position')
            value_ = self.gds_validate_string(value_, node, 'position')
            self.position = value_
            self.position_nsprefix_ = child_.prefix
            # validate type positionType
            self.validate_positionType(self.position)
        elif nodeName_ == 'signDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.signDate = dval_
            self.signDate_nsprefix_ = child_.prefix
# end class control99ResponsibleType


class control99NoticeComplianceWithDocType(GeneratedsSuper):
    """Тип: Уведомление о соответствии контролируемой информации, принятое
    вместе с контролируемым документом"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'refExternalId': MemberSpec_('refExternalId', ['externalIdType', 'xs:string'], 0, 0, {'name': 'refExternalId', 'type': 'xs:string'}, None),
        'documentType': MemberSpec_('documentType', ['control99DocumentTypeEnum', 'xs:string'], 0, 0, {'name': 'documentType', 'type': 'xs:string'}, None),
        'refVersionNumber': MemberSpec_('refVersionNumber', ['versionNumberType', 'xs:int'], 0, 1, {'minOccurs': '0', 'name': 'refVersionNumber', 'type': 'xs:int'}, None),
        'docNumber': MemberSpec_('docNumber', ['control99DocNumberType', 'xs:string'], 0, 0, {'name': 'docNumber', 'type': 'xs:string'}, None),
        'docDate': MemberSpec_('docDate', 'xs:dateTime', 0, 0, {'name': 'docDate', 'type': 'xs:dateTime'}, None),
        'signDate': MemberSpec_('signDate', 'xs:dateTime', 0, 0, {'name': 'signDate', 'type': 'xs:dateTime'}, None),
        'controlAuthorityInfo': MemberSpec_('controlAuthorityInfo', 'control99ControlAuthorityInfoType', 0, 0, {'name': 'controlAuthorityInfo', 'type': 'control99ControlAuthorityInfoType'}, None),
        'customerInfo': MemberSpec_('customerInfo', 'control99CustomerInfoType', 0, 0, {'name': 'customerInfo', 'type': 'customerInfo'}, None),
        'controlObjectsInfo': MemberSpec_('controlObjectsInfo', 'controlObjectsInfo', 0, 0, {'name': 'controlObjectsInfo', 'type': 'controlObjectsInfo'}, None),
        'responsibleInfo': MemberSpec_('responsibleInfo', 'responsibleInfo', 0, 0, {'name': 'responsibleInfo', 'type': 'control99ResponsibleType'}, None),
        'extPrintForm': MemberSpec_('extPrintForm', 'extPrintFormType', 0, 1, {'minOccurs': '0', 'name': 'extPrintForm', 'type': 'extPrintFormType'}, None),
        'bNeedGIISPURCheck': MemberSpec_('bNeedGIISPURCheck', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'bNeedGIISPURCheck', 'type': 'xs:boolean'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, refExternalId=None, documentType=None, refVersionNumber=None, docNumber=None, docDate=None, signDate=None, controlAuthorityInfo=None, customerInfo=None, controlObjectsInfo=None, responsibleInfo=None, extPrintForm=None, bNeedGIISPURCheck=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.refExternalId = refExternalId
        self.validate_externalIdType(self.refExternalId)
        self.refExternalId_nsprefix_ = None
        self.documentType = documentType
        self.validate_control99DocumentTypeEnum(self.documentType)
        self.documentType_nsprefix_ = None
        self.refVersionNumber = refVersionNumber
        self.validate_versionNumberType(self.refVersionNumber)
        self.refVersionNumber_nsprefix_ = None
        self.docNumber = docNumber
        self.validate_control99DocNumberType(self.docNumber)
        self.docNumber_nsprefix_ = None
        if isinstance(docDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(docDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = docDate
        self.docDate = initvalue_
        self.docDate_nsprefix_ = None
        if isinstance(signDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(signDate, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = signDate
        self.signDate = initvalue_
        self.signDate_nsprefix_ = None
        self.controlAuthorityInfo = controlAuthorityInfo
        self.controlAuthorityInfo_nsprefix_ = None
        self.customerInfo = customerInfo
        self.customerInfo_nsprefix_ = None
        self.controlObjectsInfo = controlObjectsInfo
        self.controlObjectsInfo_nsprefix_ = None
        self.responsibleInfo = responsibleInfo
        self.responsibleInfo_nsprefix_ = None
        self.extPrintForm = extPrintForm
        self.extPrintForm_nsprefix_ = None
        self.bNeedGIISPURCheck = bNeedGIISPURCheck
        self.bNeedGIISPURCheck_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, control99NoticeComplianceWithDocType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if control99NoticeComplianceWithDocType.subclass:
            return control99NoticeComplianceWithDocType.subclass(*args_, **kwargs_)
        else:
            return control99NoticeComplianceWithDocType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_externalIdType(self, value):
        result = True
        # Validate type externalIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on externalIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on externalIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_control99DocumentTypeEnum(self, value):
        result = True
        # Validate type control99DocumentTypeEnum, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['contract', 'contractProcedure', 'purchasePlan', 'tenderPlan2017', 'notification', 'protocol', 'contractProject', 'contractProjectChange', 'tenderPlan2020']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on control99DocumentTypeEnum' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_versionNumberType(self, value):
        result = True
        # Validate type versionNumberType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on versionNumberType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_control99DocNumberType(self, value):
        result = True
        # Validate type control99DocNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on control99DocNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on control99DocNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.refExternalId is not None or
            self.documentType is not None or
            self.refVersionNumber is not None or
            self.docNumber is not None or
            self.docDate is not None or
            self.signDate is not None or
            self.controlAuthorityInfo is not None or
            self.customerInfo is not None or
            self.controlObjectsInfo is not None or
            self.responsibleInfo is not None or
            self.extPrintForm is not None or
            self.bNeedGIISPURCheck is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'refExternalId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'refExternalId')
            value_ = self.gds_validate_string(value_, node, 'refExternalId')
            self.refExternalId = value_
            self.refExternalId_nsprefix_ = child_.prefix
            # validate type externalIdType
            self.validate_externalIdType(self.refExternalId)
        elif nodeName_ == 'documentType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'documentType')
            value_ = self.gds_validate_string(value_, node, 'documentType')
            self.documentType = value_
            self.documentType_nsprefix_ = child_.prefix
            # validate type control99DocumentTypeEnum
            self.validate_control99DocumentTypeEnum(self.documentType)
        elif nodeName_ == 'refVersionNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'refVersionNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'refVersionNumber')
            self.refVersionNumber = ival_
            self.refVersionNumber_nsprefix_ = child_.prefix
            # validate type versionNumberType
            self.validate_versionNumberType(self.refVersionNumber)
        elif nodeName_ == 'docNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'docNumber')
            value_ = self.gds_validate_string(value_, node, 'docNumber')
            self.docNumber = value_
            self.docNumber_nsprefix_ = child_.prefix
            # validate type control99DocNumberType
            self.validate_control99DocNumberType(self.docNumber)
        elif nodeName_ == 'docDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.docDate = dval_
            self.docDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'signDate':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.signDate = dval_
            self.signDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'controlAuthorityInfo':
            obj_ = control99ControlAuthorityInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.controlAuthorityInfo = obj_
            obj_.original_tagname_ = 'controlAuthorityInfo'
        elif nodeName_ == 'customerInfo':
            obj_ = customerInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customerInfo = obj_
            obj_.original_tagname_ = 'customerInfo'
        elif nodeName_ == 'controlObjectsInfo':
            obj_ = controlObjectsInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.controlObjectsInfo = obj_
            obj_.original_tagname_ = 'controlObjectsInfo'
        elif nodeName_ == 'responsibleInfo':
            obj_ = control99ResponsibleType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.responsibleInfo = obj_
            obj_.original_tagname_ = 'responsibleInfo'
        elif nodeName_ == 'extPrintForm':
            obj_ = extPrintFormType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.extPrintForm = obj_
            obj_.original_tagname_ = 'extPrintForm'
        elif nodeName_ == 'bNeedGIISPURCheck':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'bNeedGIISPURCheck')
            ival_ = self.gds_validate_boolean(ival_, node, 'bNeedGIISPURCheck')
            self.bNeedGIISPURCheck = ival_
            self.bNeedGIISPURCheck_nsprefix_ = child_.prefix
# end class control99NoticeComplianceWithDocType


class customerInfo(control99CustomerInfoType):
    """Сведения о заказчике (организации, размещающей закупку)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'OKTMOPPO': MemberSpec_('OKTMOPPO', 'OKTMOPPORef', 0, 1, {'minOccurs': '0', 'name': 'OKTMOPPO', 'type': 'OKTMOPPORef'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = control99CustomerInfoType
    def __init__(self, regNum=None, consRegistryNum=None, fullName=None, INN=None, KPP=None, OKFS=None, orgBudget=None, factAddress=None, phone=None, eMail=None, OKOPF=None, OKTMO=None, OKTMOPPO=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(customerInfo, self).__init__(regNum, consRegistryNum, fullName, INN, KPP, OKFS, orgBudget, factAddress, phone, eMail, OKOPF, OKTMO,  **kwargs_)
        self.OKTMOPPO = OKTMOPPO
        self.OKTMOPPO_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, customerInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if customerInfo.subclass:
            return customerInfo.subclass(*args_, **kwargs_)
        else:
            return customerInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.OKTMOPPO is not None or
            super(customerInfo, self).hasContent_()
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(customerInfo, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OKTMOPPO':
            obj_ = OKTMOPPORef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKTMOPPO = obj_
            obj_.original_tagname_ = 'OKTMOPPO'
        super(customerInfo, self).buildChildren(child_, node, nodeName_, True)
# end class customerInfo


class controlObjectsInfo(GeneratedsSuper):
    """Сведения об объектах контроля"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'controlObjectInfo': MemberSpec_('controlObjectInfo', 'control99ControlObjectWithMandatoryDocsInfoType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'controlObjectInfo', 'type': 'control99ControlObjectWithMandatoryDocsInfoType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, controlObjectInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if controlObjectInfo is None:
            self.controlObjectInfo = []
        else:
            self.controlObjectInfo = controlObjectInfo
        self.controlObjectInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, controlObjectsInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if controlObjectsInfo.subclass:
            return controlObjectsInfo.subclass(*args_, **kwargs_)
        else:
            return controlObjectsInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.controlObjectInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'controlObjectInfo':
            obj_ = control99ControlObjectWithMandatoryDocsInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.controlObjectInfo.append(obj_)
            obj_.original_tagname_ = 'controlObjectInfo'
# end class controlObjectsInfo


class drugInfoType(GeneratedsSuper):
    """Тип: Сведения о МНН, ТН, лекарственной форме и дозировке"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'MNNInfo': MemberSpec_('MNNInfo', 'MNNInfo', 0, 0, {'name': 'MNNInfo', 'type': 'MNNInfoType'}, None),
        'tradeInfo': MemberSpec_('tradeInfo', 'tradeInfo', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'tradeInfo', 'type': 'tradeInfoType'}, None),
        'medicamentalFormInfo': MemberSpec_('medicamentalFormInfo', 'medicamentalFormInfo', 0, 1, {'minOccurs': '0', 'name': 'medicamentalFormInfo', 'type': 'medicamentalFormInfo'}, None),
        'dosageInfo': MemberSpec_('dosageInfo', 'dosageInfo', 0, 1, {'minOccurs': '0', 'name': 'dosageInfo', 'type': 'dosageInfo'}, None),
        'packagingInfo': MemberSpec_('packagingInfo', 'packagingInfo', 0, 1, {'minOccurs': '0', 'name': 'packagingInfo', 'type': 'packagingInfo'}, None),
        'manualUserOKEI': MemberSpec_('manualUserOKEI', 'OKEIRef', 0, 1, {'minOccurs': '0', 'name': 'manualUserOKEI', 'type': 'OKEIRef'}, None),
        'basicUnit': MemberSpec_('basicUnit', 'xs:boolean', 0, 1, {'fixed': 'true', 'minOccurs': '0', 'name': 'basicUnit', 'type': 'xs:boolean'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, MNNInfo=None, tradeInfo=None, medicamentalFormInfo=None, dosageInfo=None, packagingInfo=None, manualUserOKEI=None, basicUnit=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MNNInfo = MNNInfo
        self.MNNInfo_nsprefix_ = None
        if tradeInfo is None:
            self.tradeInfo = []
        else:
            self.tradeInfo = tradeInfo
        self.tradeInfo_nsprefix_ = None
        self.medicamentalFormInfo = medicamentalFormInfo
        self.medicamentalFormInfo_nsprefix_ = None
        self.dosageInfo = dosageInfo
        self.dosageInfo_nsprefix_ = None
        self.packagingInfo = packagingInfo
        self.packagingInfo_nsprefix_ = None
        self.manualUserOKEI = manualUserOKEI
        self.manualUserOKEI_nsprefix_ = None
        self.basicUnit = basicUnit
        self.basicUnit_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInfoType.subclass:
            return drugInfoType.subclass(*args_, **kwargs_)
        else:
            return drugInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.MNNInfo is not None or
            self.tradeInfo or
            self.medicamentalFormInfo is not None or
            self.dosageInfo is not None or
            self.packagingInfo is not None or
            self.manualUserOKEI is not None or
            self.basicUnit is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MNNInfo':
            obj_ = MNNInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MNNInfo = obj_
            obj_.original_tagname_ = 'MNNInfo'
        elif nodeName_ == 'tradeInfo':
            obj_ = tradeInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.tradeInfo.append(obj_)
            obj_.original_tagname_ = 'tradeInfo'
        elif nodeName_ == 'medicamentalFormInfo':
            obj_ = medicamentalFormInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.medicamentalFormInfo = obj_
            obj_.original_tagname_ = 'medicamentalFormInfo'
        elif nodeName_ == 'dosageInfo':
            obj_ = dosageInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dosageInfo = obj_
            obj_.original_tagname_ = 'dosageInfo'
        elif nodeName_ == 'packagingInfo':
            obj_ = packagingInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.packagingInfo = obj_
            obj_.original_tagname_ = 'packagingInfo'
        elif nodeName_ == 'manualUserOKEI':
            obj_ = OKEIRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manualUserOKEI = obj_
            obj_.original_tagname_ = 'manualUserOKEI'
        elif nodeName_ == 'basicUnit':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'basicUnit')
            ival_ = self.gds_validate_boolean(ival_, node, 'basicUnit')
            self.basicUnit = ival_
            self.basicUnit_nsprefix_ = child_.prefix
# end class drugInfoType


class medicamentalFormInfo(GeneratedsSuper):
    """Лекарственная форма. Игнорируется при приеме, автоматически заполняется
    при передаче по справочнику "Лекарственные препараты" """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'medicamentalFormName': MemberSpec_('medicamentalFormName', ['drugNameType', 'xs:string'], 0, 0, {'name': 'medicamentalFormName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, medicamentalFormName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.medicamentalFormName = medicamentalFormName
        self.validate_drugNameType(self.medicamentalFormName)
        self.medicamentalFormName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, medicamentalFormInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if medicamentalFormInfo.subclass:
            return medicamentalFormInfo.subclass(*args_, **kwargs_)
        else:
            return medicamentalFormInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugNameType(self, value):
        result = True
        # Validate type drugNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.medicamentalFormName is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'medicamentalFormName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'medicamentalFormName')
            value_ = self.gds_validate_string(value_, node, 'medicamentalFormName')
            self.medicamentalFormName = value_
            self.medicamentalFormName_nsprefix_ = child_.prefix
            # validate type drugNameType
            self.validate_drugNameType(self.medicamentalFormName)
# end class medicamentalFormInfo


class dosageInfo(GeneratedsSuper):
    """Дозировка. Игнорируется при приеме, автоматически заполняется при
    передаче по справочнику "Лекарственные препараты" """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'dosageGRLSValue': MemberSpec_('dosageGRLSValue', ['drugNameType', 'xs:string'], 0, 0, {'name': 'dosageGRLSValue', 'type': 'xs:string'}, None),
        'dosageUserOKEI': MemberSpec_('dosageUserOKEI', 'OKEIRef', 0, 0, {'name': 'dosageUserOKEI', 'type': 'OKEIRef'}, None),
        'dosageUserName': MemberSpec_('dosageUserName', ['drugNameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'dosageUserName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, dosageGRLSValue=None, dosageUserOKEI=None, dosageUserName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.dosageGRLSValue = dosageGRLSValue
        self.validate_drugNameType(self.dosageGRLSValue)
        self.dosageGRLSValue_nsprefix_ = None
        self.dosageUserOKEI = dosageUserOKEI
        self.dosageUserOKEI_nsprefix_ = None
        self.dosageUserName = dosageUserName
        self.validate_drugNameType(self.dosageUserName)
        self.dosageUserName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dosageInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dosageInfo.subclass:
            return dosageInfo.subclass(*args_, **kwargs_)
        else:
            return dosageInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugNameType(self, value):
        result = True
        # Validate type drugNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.dosageGRLSValue is not None or
            self.dosageUserOKEI is not None or
            self.dosageUserName is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'dosageGRLSValue':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dosageGRLSValue')
            value_ = self.gds_validate_string(value_, node, 'dosageGRLSValue')
            self.dosageGRLSValue = value_
            self.dosageGRLSValue_nsprefix_ = child_.prefix
            # validate type drugNameType
            self.validate_drugNameType(self.dosageGRLSValue)
        elif nodeName_ == 'dosageUserOKEI':
            obj_ = OKEIRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dosageUserOKEI = obj_
            obj_.original_tagname_ = 'dosageUserOKEI'
        elif nodeName_ == 'dosageUserName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dosageUserName')
            value_ = self.gds_validate_string(value_, node, 'dosageUserName')
            self.dosageUserName = value_
            self.dosageUserName_nsprefix_ = child_.prefix
            # validate type drugNameType
            self.validate_drugNameType(self.dosageUserName)
# end class dosageInfo


class packagingInfo(GeneratedsSuper):
    """Сведения об упаковке. В случае заполнения блока mustSpecifyDrugPackage
    при приеме контролируется заполненность блока packagingInfo во всех
    вариантах поставки лекарственных препаратовю. Для групп
    взаимозаменяемости (блок drugInterchangeInfo) всегда игнорируется при
    приеме, автоматически заполняется при передаче по справочнику
    "Лекарственные препараты" за исключением поля sumaryPackagingQuantity
    для извещений, первая версия которых размещена до выхода версии 10.3,
    независимо от разрешения ручного ввода"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'packaging1Quantity': MemberSpec_('packaging1Quantity', ['drugPackaging1QuantityType', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'packaging1Quantity', 'type': 'xs:decimal'}, None),
        'packaging2Quantity': MemberSpec_('packaging2Quantity', ['drugPackaging2QuantityType', 'xs:int'], 0, 1, {'minOccurs': '0', 'name': 'packaging2Quantity', 'type': 'xs:int'}, None),
        'sumaryPackagingQuantity': MemberSpec_('sumaryPackagingQuantity', ['drugSumaryPackagingQuantityType', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'sumaryPackagingQuantity', 'type': 'xs:decimal'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, packaging1Quantity=None, packaging2Quantity=None, sumaryPackagingQuantity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.packaging1Quantity = packaging1Quantity
        self.validate_drugPackaging1QuantityType(self.packaging1Quantity)
        self.packaging1Quantity_nsprefix_ = None
        self.packaging2Quantity = packaging2Quantity
        self.validate_drugPackaging2QuantityType(self.packaging2Quantity)
        self.packaging2Quantity_nsprefix_ = None
        self.sumaryPackagingQuantity = sumaryPackagingQuantity
        self.validate_drugSumaryPackagingQuantityType(self.sumaryPackagingQuantity)
        self.sumaryPackagingQuantity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, packagingInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if packagingInfo.subclass:
            return packagingInfo.subclass(*args_, **kwargs_)
        else:
            return packagingInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugPackaging1QuantityType(self, value):
        result = True
        # Validate type drugPackaging1QuantityType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on drugPackaging1QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_drugPackaging2QuantityType(self, value):
        result = True
        # Validate type drugPackaging2QuantityType, a restriction on xs:int.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on drugPackaging2QuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_drugSumaryPackagingQuantityType(self, value):
        result = True
        # Validate type drugSumaryPackagingQuantityType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 22:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on drugSumaryPackagingQuantityType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.packaging1Quantity is not None or
            self.packaging2Quantity is not None or
            self.sumaryPackagingQuantity is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'packaging1Quantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'packaging1Quantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'packaging1Quantity')
            self.packaging1Quantity = fval_
            self.packaging1Quantity_nsprefix_ = child_.prefix
            # validate type drugPackaging1QuantityType
            self.validate_drugPackaging1QuantityType(self.packaging1Quantity)
        elif nodeName_ == 'packaging2Quantity' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'packaging2Quantity')
            ival_ = self.gds_validate_integer(ival_, node, 'packaging2Quantity')
            self.packaging2Quantity = ival_
            self.packaging2Quantity_nsprefix_ = child_.prefix
            # validate type drugPackaging2QuantityType
            self.validate_drugPackaging2QuantityType(self.packaging2Quantity)
        elif nodeName_ == 'sumaryPackagingQuantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'sumaryPackagingQuantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'sumaryPackagingQuantity')
            self.sumaryPackagingQuantity = fval_
            self.sumaryPackagingQuantity_nsprefix_ = child_.prefix
            # validate type drugSumaryPackagingQuantityType
            self.validate_drugSumaryPackagingQuantityType(self.sumaryPackagingQuantity)
# end class packagingInfo


class drugInfoUsingTextFormType(GeneratedsSuper):
    """Тип: Сведения о МНН, ТН, лекарственной форме и дозировке в случае когда
    информация о лекарственных препаратах формируется в текстовой форме"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'MNNInfo': MemberSpec_('MNNInfo', 'MNNInfo', 0, 0, {'name': 'MNNInfo', 'type': 'MNNInfo'}, None),
        'tradeInfo': MemberSpec_('tradeInfo', 'tradeInfo', 0, 1, {'minOccurs': '0', 'name': 'tradeInfo', 'type': 'tradeInfo'}, None),
        'medicamentalFormInfo': MemberSpec_('medicamentalFormInfo', 'medicamentalFormInfo', 0, 0, {'name': 'medicamentalFormInfo', 'type': 'medicamentalFormInfo'}, None),
        'dosageInfo': MemberSpec_('dosageInfo', 'dosageInfo', 0, 0, {'name': 'dosageInfo', 'type': 'dosageInfo'}, None),
        'packagingInfo': MemberSpec_('packagingInfo', 'packagingInfo', 0, 1, {'minOccurs': '0', 'name': 'packagingInfo', 'type': 'packagingInfo'}, None),
        'manualUserOKEI': MemberSpec_('manualUserOKEI', 'OKEIRef', 0, 0, {'name': 'manualUserOKEI', 'type': 'OKEIRef'}, None),
        'drugChangeInfo': MemberSpec_('drugChangeInfo', 'drugChangeInfoType', 0, 1, {'minOccurs': '0', 'name': 'drugChangeInfo', 'type': 'drugChangeInfoType'}, None),
        'basicUnit': MemberSpec_('basicUnit', 'xs:boolean', 0, 1, {'fixed': 'true', 'minOccurs': '0', 'name': 'basicUnit', 'type': 'xs:boolean'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, MNNInfo=None, tradeInfo=None, medicamentalFormInfo=None, dosageInfo=None, packagingInfo=None, manualUserOKEI=None, drugChangeInfo=None, basicUnit=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MNNInfo = MNNInfo
        self.MNNInfo_nsprefix_ = None
        self.tradeInfo = tradeInfo
        self.tradeInfo_nsprefix_ = None
        self.medicamentalFormInfo = medicamentalFormInfo
        self.medicamentalFormInfo_nsprefix_ = None
        self.dosageInfo = dosageInfo
        self.dosageInfo_nsprefix_ = None
        self.packagingInfo = packagingInfo
        self.packagingInfo_nsprefix_ = None
        self.manualUserOKEI = manualUserOKEI
        self.manualUserOKEI_nsprefix_ = None
        self.drugChangeInfo = drugChangeInfo
        self.drugChangeInfo_nsprefix_ = None
        self.basicUnit = basicUnit
        self.basicUnit_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInfoUsingTextFormType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInfoUsingTextFormType.subclass:
            return drugInfoUsingTextFormType.subclass(*args_, **kwargs_)
        else:
            return drugInfoUsingTextFormType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.MNNInfo is not None or
            self.tradeInfo is not None or
            self.medicamentalFormInfo is not None or
            self.dosageInfo is not None or
            self.packagingInfo is not None or
            self.manualUserOKEI is not None or
            self.drugChangeInfo is not None or
            self.basicUnit is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MNNInfo':
            obj_ = MNNInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MNNInfo = obj_
            obj_.original_tagname_ = 'MNNInfo'
        elif nodeName_ == 'tradeInfo':
            obj_ = tradeInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.tradeInfo = obj_
            obj_.original_tagname_ = 'tradeInfo'
        elif nodeName_ == 'medicamentalFormInfo':
            obj_ = medicamentalFormInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.medicamentalFormInfo = obj_
            obj_.original_tagname_ = 'medicamentalFormInfo'
        elif nodeName_ == 'dosageInfo':
            obj_ = dosageInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dosageInfo = obj_
            obj_.original_tagname_ = 'dosageInfo'
        elif nodeName_ == 'packagingInfo':
            obj_ = packagingInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.packagingInfo = obj_
            obj_.original_tagname_ = 'packagingInfo'
        elif nodeName_ == 'manualUserOKEI':
            obj_ = OKEIRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manualUserOKEI = obj_
            obj_.original_tagname_ = 'manualUserOKEI'
        elif nodeName_ == 'drugChangeInfo':
            obj_ = drugChangeInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugChangeInfo = obj_
            obj_.original_tagname_ = 'drugChangeInfo'
        elif nodeName_ == 'basicUnit':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'basicUnit')
            ival_ = self.gds_validate_boolean(ival_, node, 'basicUnit')
            self.basicUnit = ival_
            self.basicUnit_nsprefix_ = child_.prefix
# end class drugInfoUsingTextFormType


class MNNInfo(GeneratedsSuper):
    """Международное, группировочное или химическое наименование лекарственного
    препарата (МНН). При приеме контрролируется, что МНН в списке
    лекарственных препаратов должны иметь одни и те же наименования"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'MNNName': MemberSpec_('MNNName', ['drugName2000Type', 'xs:string'], 0, 0, {'name': 'MNNName', 'type': 'xs:string'}, None),
        'drugChangeInfo': MemberSpec_('drugChangeInfo', 'drugChangeInfoType', 0, 1, {'minOccurs': '0', 'name': 'drugChangeInfo', 'type': 'drugChangeInfoType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, MNNName=None, drugChangeInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MNNName = MNNName
        self.validate_drugName2000Type(self.MNNName)
        self.MNNName_nsprefix_ = None
        self.drugChangeInfo = drugChangeInfo
        self.drugChangeInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MNNInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MNNInfo.subclass:
            return MNNInfo.subclass(*args_, **kwargs_)
        else:
            return MNNInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugName2000Type(self, value):
        result = True
        # Validate type drugName2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugName2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugName2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.MNNName is not None or
            self.drugChangeInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MNNName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MNNName')
            value_ = self.gds_validate_string(value_, node, 'MNNName')
            self.MNNName = value_
            self.MNNName_nsprefix_ = child_.prefix
            # validate type drugName2000Type
            self.validate_drugName2000Type(self.MNNName)
        elif nodeName_ == 'drugChangeInfo':
            obj_ = drugChangeInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugChangeInfo = obj_
            obj_.original_tagname_ = 'drugChangeInfo'
# end class MNNInfo


class tradeInfo(GeneratedsSuper):
    """Торговое наименование (ТН) лекарственного препарата. Бизнес-контролем
    проверяется, что блок может быть заполнен только в случае если способ
    определения поставщика по закупке - «Закупка у единственного поставщика
    (подрядчика, исполнителя)»"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'tradeName': MemberSpec_('tradeName', ['drugNameType', 'xs:string'], 0, 0, {'name': 'tradeName', 'type': 'xs:string'}, None),
        'drugChangeInfo': MemberSpec_('drugChangeInfo', 'drugChangeInfoType', 0, 1, {'minOccurs': '0', 'name': 'drugChangeInfo', 'type': 'drugChangeInfoType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, tradeName=None, drugChangeInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tradeName = tradeName
        self.validate_drugNameType(self.tradeName)
        self.tradeName_nsprefix_ = None
        self.drugChangeInfo = drugChangeInfo
        self.drugChangeInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tradeInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tradeInfo.subclass:
            return tradeInfo.subclass(*args_, **kwargs_)
        else:
            return tradeInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugNameType(self, value):
        result = True
        # Validate type drugNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.tradeName is not None or
            self.drugChangeInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tradeName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tradeName')
            value_ = self.gds_validate_string(value_, node, 'tradeName')
            self.tradeName = value_
            self.tradeName_nsprefix_ = child_.prefix
            # validate type drugNameType
            self.validate_drugNameType(self.tradeName)
        elif nodeName_ == 'drugChangeInfo':
            obj_ = drugChangeInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugChangeInfo = obj_
            obj_.original_tagname_ = 'drugChangeInfo'
# end class tradeInfo


class purchaseDrugObjectsInfoType(GeneratedsSuper):
    """Тип: Сведения об объектах закупки в том случае, когда объектами закупки
    являются лекарственные препараты (ПРИЗ)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugPurchaseObjectInfo': MemberSpec_('drugPurchaseObjectInfo', 'drugPurchaseObjectInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'drugPurchaseObjectInfo', 'type': 'drugPurchaseObjectInfo'}, None),
        'total': MemberSpec_('total', ['moneyLongType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'total', 'type': 'xs:string'}, None),
        'totalSumCurrency': MemberSpec_('totalSumCurrency', ['moneyLongType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'totalSumCurrency', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugPurchaseObjectInfo=None, total=None, totalSumCurrency=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if drugPurchaseObjectInfo is None:
            self.drugPurchaseObjectInfo = []
        else:
            self.drugPurchaseObjectInfo = drugPurchaseObjectInfo
        self.drugPurchaseObjectInfo_nsprefix_ = None
        self.total = total
        self.validate_moneyLongType(self.total)
        self.total_nsprefix_ = None
        self.totalSumCurrency = totalSumCurrency
        self.validate_moneyLongType(self.totalSumCurrency)
        self.totalSumCurrency_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, purchaseDrugObjectsInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if purchaseDrugObjectsInfoType.subclass:
            return purchaseDrugObjectsInfoType.subclass(*args_, **kwargs_)
        else:
            return purchaseDrugObjectsInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_moneyLongType(self, value):
        result = True
        # Validate type moneyLongType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyLongType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyLongType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyLongType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyLongType_patterns_, ))
                result = False
        return result
    validate_moneyLongType_patterns_ = [['^((-)?\\d+(\\.\\d{1,11})?)$']]
    def hasContent_(self):
        if (
            self.drugPurchaseObjectInfo or
            self.total is not None or
            self.totalSumCurrency is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugPurchaseObjectInfo':
            obj_ = drugPurchaseObjectInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugPurchaseObjectInfo.append(obj_)
            obj_.original_tagname_ = 'drugPurchaseObjectInfo'
        elif nodeName_ == 'total':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'total')
            value_ = self.gds_validate_string(value_, node, 'total')
            self.total = value_
            self.total_nsprefix_ = child_.prefix
            # validate type moneyLongType
            self.validate_moneyLongType(self.total)
        elif nodeName_ == 'totalSumCurrency':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'totalSumCurrency')
            value_ = self.gds_validate_string(value_, node, 'totalSumCurrency')
            self.totalSumCurrency = value_
            self.totalSumCurrency_nsprefix_ = child_.prefix
            # validate type moneyLongType
            self.validate_moneyLongType(self.totalSumCurrency)
# end class purchaseDrugObjectsInfoType


class drugPurchaseObjectInfo(GeneratedsSuper):
    """Сведения об объекте закупки в том случае, когда объектом закупки
    является лекарственный препарат"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'sid': MemberSpec_('sid', ['sid', 'xs:long'], 0, 1, {'minOccurs': '0', 'name': 'sid', 'type': 'xs:long'}, None),
        'externalSid': MemberSpec_('externalSid', ['externalIdType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'externalSid', 'type': 'xs:string'}, None),
        'objectInfoUsingReferenceInfo': MemberSpec_('objectInfoUsingReferenceInfo', 'objectInfoUsingReferenceInfo', 0, 0, {'name': 'objectInfoUsingReferenceInfo', 'type': 'objectInfoUsingReferenceInfo'}, 8),
        'objectInfoUsingTextForm': MemberSpec_('objectInfoUsingTextForm', 'objectInfoUsingTextForm', 0, 0, {'name': 'objectInfoUsingTextForm', 'type': 'objectInfoUsingTextForm'}, None),
        'isZNVLP': MemberSpec_('isZNVLP', 'xs:boolean', 0, 1, {'minOccurs': '0', 'name': 'isZNVLP', 'type': 'xs:boolean'}, None),
        'drugQuantityCustomersInfo': MemberSpec_('drugQuantityCustomersInfo', 'drugQuantityCustomersInfo', 0, 0, {'name': 'drugQuantityCustomersInfo', 'type': 'drugQuantityCustomersInfo'}, 12),
        'pricePerUnit': MemberSpec_('pricePerUnit', ['moneyLongType', 'xs:string'], 0, 0, {'name': 'pricePerUnit', 'type': 'xs:string'}, 12),
        'positionPrice': MemberSpec_('positionPrice', ['moneyType', 'xs:string'], 0, 0, {'name': 'positionPrice', 'type': 'xs:string'}, 12),
        'quantityUndefined': MemberSpec_('quantityUndefined', 'quantityUndefined', 0, 0, {'name': 'quantityUndefined', 'type': 'quantityUndefined'}, 12),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, sid=None, externalSid=None, objectInfoUsingReferenceInfo=None, objectInfoUsingTextForm=None, isZNVLP=None, drugQuantityCustomersInfo=None, pricePerUnit=None, positionPrice=None, quantityUndefined=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.sid = sid
        self.sid_nsprefix_ = None
        self.externalSid = externalSid
        self.validate_externalIdType(self.externalSid)
        self.externalSid_nsprefix_ = None
        self.objectInfoUsingReferenceInfo = objectInfoUsingReferenceInfo
        self.objectInfoUsingReferenceInfo_nsprefix_ = None
        self.objectInfoUsingTextForm = objectInfoUsingTextForm
        self.objectInfoUsingTextForm_nsprefix_ = None
        self.isZNVLP = isZNVLP
        self.isZNVLP_nsprefix_ = None
        self.drugQuantityCustomersInfo = drugQuantityCustomersInfo
        self.drugQuantityCustomersInfo_nsprefix_ = None
        self.pricePerUnit = pricePerUnit
        self.validate_moneyLongType(self.pricePerUnit)
        self.pricePerUnit_nsprefix_ = None
        self.positionPrice = positionPrice
        self.validate_moneyType(self.positionPrice)
        self.positionPrice_nsprefix_ = None
        self.quantityUndefined = quantityUndefined
        self.quantityUndefined_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugPurchaseObjectInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugPurchaseObjectInfo.subclass:
            return drugPurchaseObjectInfo.subclass(*args_, **kwargs_)
        else:
            return drugPurchaseObjectInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_externalIdType(self, value):
        result = True
        # Validate type externalIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on externalIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on externalIdType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_moneyLongType(self, value):
        result = True
        # Validate type moneyLongType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyLongType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyLongType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyLongType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyLongType_patterns_, ))
                result = False
        return result
    validate_moneyLongType_patterns_ = [['^((-)?\\d+(\\.\\d{1,11})?)$']]
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.sid is not None or
            self.externalSid is not None or
            self.objectInfoUsingReferenceInfo is not None or
            self.objectInfoUsingTextForm is not None or
            self.isZNVLP is not None or
            self.drugQuantityCustomersInfo is not None or
            self.pricePerUnit is not None or
            self.positionPrice is not None or
            self.quantityUndefined is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'sid' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'sid')
            ival_ = self.gds_validate_integer(ival_, node, 'sid')
            self.sid = ival_
            self.sid_nsprefix_ = child_.prefix
        elif nodeName_ == 'externalSid':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'externalSid')
            value_ = self.gds_validate_string(value_, node, 'externalSid')
            self.externalSid = value_
            self.externalSid_nsprefix_ = child_.prefix
            # validate type externalIdType
            self.validate_externalIdType(self.externalSid)
        elif nodeName_ == 'objectInfoUsingReferenceInfo':
            obj_ = objectInfoUsingReferenceInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.objectInfoUsingReferenceInfo = obj_
            obj_.original_tagname_ = 'objectInfoUsingReferenceInfo'
        elif nodeName_ == 'objectInfoUsingTextForm':
            obj_ = objectInfoUsingTextForm.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.objectInfoUsingTextForm = obj_
            obj_.original_tagname_ = 'objectInfoUsingTextForm'
        elif nodeName_ == 'isZNVLP':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isZNVLP')
            ival_ = self.gds_validate_boolean(ival_, node, 'isZNVLP')
            self.isZNVLP = ival_
            self.isZNVLP_nsprefix_ = child_.prefix
        elif nodeName_ == 'drugQuantityCustomersInfo':
            obj_ = drugQuantityCustomersInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugQuantityCustomersInfo = obj_
            obj_.original_tagname_ = 'drugQuantityCustomersInfo'
        elif nodeName_ == 'pricePerUnit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'pricePerUnit')
            value_ = self.gds_validate_string(value_, node, 'pricePerUnit')
            self.pricePerUnit = value_
            self.pricePerUnit_nsprefix_ = child_.prefix
            # validate type moneyLongType
            self.validate_moneyLongType(self.pricePerUnit)
        elif nodeName_ == 'positionPrice':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'positionPrice')
            value_ = self.gds_validate_string(value_, node, 'positionPrice')
            self.positionPrice = value_
            self.positionPrice_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.positionPrice)
        elif nodeName_ == 'quantityUndefined':
            obj_ = quantityUndefined.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.quantityUndefined = obj_
            obj_.original_tagname_ = 'quantityUndefined'
# end class drugPurchaseObjectInfo


class objectInfoUsingReferenceInfo(GeneratedsSuper):
    """Информация о вариантах поставки лекарственных препаратов формируется с
    использованием справочной информации (не в текстовой форме)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugsInfo': MemberSpec_('drugsInfo', 'drugsInfo', 0, 0, {'name': 'drugsInfo', 'type': 'drugsInfo'}, 8),
        'mustSpecifyDrugPackage': MemberSpec_('mustSpecifyDrugPackage', 'mustSpecifyDrugPackage', 0, 1, {'minOccurs': '0', 'name': 'mustSpecifyDrugPackage', 'type': 'mustSpecifyDrugPackage'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugsInfo=None, mustSpecifyDrugPackage=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.drugsInfo = drugsInfo
        self.drugsInfo_nsprefix_ = None
        self.mustSpecifyDrugPackage = mustSpecifyDrugPackage
        self.mustSpecifyDrugPackage_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, objectInfoUsingReferenceInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if objectInfoUsingReferenceInfo.subclass:
            return objectInfoUsingReferenceInfo.subclass(*args_, **kwargs_)
        else:
            return objectInfoUsingReferenceInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.drugsInfo is not None or
            self.mustSpecifyDrugPackage is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugsInfo':
            obj_ = drugsInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugsInfo = obj_
            obj_.original_tagname_ = 'drugsInfo'
        elif nodeName_ == 'mustSpecifyDrugPackage':
            obj_ = mustSpecifyDrugPackage.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.mustSpecifyDrugPackage = obj_
            obj_.original_tagname_ = 'mustSpecifyDrugPackage'
# end class objectInfoUsingReferenceInfo


class drugsInfo(GeneratedsSuper):
    """Сведения о вариантах поставки лекарственных препаратов"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugInfo': MemberSpec_('drugInfo', 'drugInfoType', 1, 0, {'maxOccurs': 'unbounded', 'name': 'drugInfo', 'type': 'drugInfo'}, 9),
        'drugInterchangeInfo': MemberSpec_('drugInterchangeInfo', 'drugInterchangeInfo', 0, 0, {'name': 'drugInterchangeInfo', 'type': 'drugInterchangeInfo'}, 9),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugInfo=None, drugInterchangeInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if drugInfo is None:
            self.drugInfo = []
        else:
            self.drugInfo = drugInfo
        self.drugInfo_nsprefix_ = None
        self.drugInterchangeInfo = drugInterchangeInfo
        self.drugInterchangeInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugsInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugsInfo.subclass:
            return drugsInfo.subclass(*args_, **kwargs_)
        else:
            return drugsInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.drugInfo or
            self.drugInterchangeInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugInfo':
            obj_ = drugInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInfo.append(obj_)
            obj_.original_tagname_ = 'drugInfo'
        elif nodeName_ == 'drugInterchangeInfo':
            obj_ = drugInterchangeInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInterchangeInfo = obj_
            obj_.original_tagname_ = 'drugInterchangeInfo'
# end class drugsInfo


class drugInfo(drugInfoType):
    """Сведения о варианте поставки лекарственного препарата"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugQuantity': MemberSpec_('drugQuantity', ['quantity18p11Type', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'drugQuantity', 'type': 'xs:decimal'}, 9),
        'averagePriceValue': MemberSpec_('averagePriceValue', ['drugDecimalCodeType', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'averagePriceValue', 'type': 'xs:decimal'}, 9),
        'averagePriceTotal': MemberSpec_('averagePriceTotal', ['moneyMaxLengthToPoint18Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'averagePriceTotal', 'type': 'xs:string'}, 9),
        'limPriceValuePerUnit': MemberSpec_('limPriceValuePerUnit', ['drugDecimalCodeType', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'limPriceValuePerUnit', 'type': 'xs:decimal'}, 9),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = drugInfoType
    def __init__(self, MNNInfo=None, tradeInfo=None, medicamentalFormInfo=None, dosageInfo=None, packagingInfo=None, manualUserOKEI=None, basicUnit=None, drugQuantity=None, averagePriceValue=None, averagePriceTotal=None, limPriceValuePerUnit=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(drugInfo, self).__init__(MNNInfo, tradeInfo, medicamentalFormInfo, dosageInfo, packagingInfo, manualUserOKEI, basicUnit,  **kwargs_)
        self.drugQuantity = drugQuantity
        self.validate_quantity18p11Type(self.drugQuantity)
        self.drugQuantity_nsprefix_ = None
        self.averagePriceValue = averagePriceValue
        self.validate_drugDecimalCodeType(self.averagePriceValue)
        self.averagePriceValue_nsprefix_ = None
        self.averagePriceTotal = averagePriceTotal
        self.validate_moneyMaxLengthToPoint18Type(self.averagePriceTotal)
        self.averagePriceTotal_nsprefix_ = None
        self.limPriceValuePerUnit = limPriceValuePerUnit
        self.validate_drugDecimalCodeType(self.limPriceValuePerUnit)
        self.limPriceValuePerUnit_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInfo.subclass:
            return drugInfo.subclass(*args_, **kwargs_)
        else:
            return drugInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_quantity18p11Type(self, value):
        result = True
        # Validate type quantity18p11Type, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 29:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on quantity18p11Type' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_quantity18p11Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_quantity18p11Type_patterns_, ))
                result = False
        return result
    validate_quantity18p11Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,11})?)$']]
    def validate_drugDecimalCodeType(self, value):
        result = True
        # Validate type drugDecimalCodeType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on drugDecimalCodeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_moneyMaxLengthToPoint18Type(self, value):
        result = True
        # Validate type moneyMaxLengthToPoint18Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyMaxLengthToPoint18Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyMaxLengthToPoint18Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyMaxLengthToPoint18Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyMaxLengthToPoint18Type_patterns_, ))
                result = False
        return result
    validate_moneyMaxLengthToPoint18Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,2})?)$']]
    def hasContent_(self):
        if (
            self.drugQuantity is not None or
            self.averagePriceValue is not None or
            self.averagePriceTotal is not None or
            self.limPriceValuePerUnit is not None or
            super(drugInfo, self).hasContent_()
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(drugInfo, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugQuantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'drugQuantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'drugQuantity')
            self.drugQuantity = fval_
            self.drugQuantity_nsprefix_ = child_.prefix
            # validate type quantity18p11Type
            self.validate_quantity18p11Type(self.drugQuantity)
        elif nodeName_ == 'averagePriceValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'averagePriceValue')
            fval_ = self.gds_validate_decimal(fval_, node, 'averagePriceValue')
            self.averagePriceValue = fval_
            self.averagePriceValue_nsprefix_ = child_.prefix
            # validate type drugDecimalCodeType
            self.validate_drugDecimalCodeType(self.averagePriceValue)
        elif nodeName_ == 'averagePriceTotal':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'averagePriceTotal')
            value_ = self.gds_validate_string(value_, node, 'averagePriceTotal')
            self.averagePriceTotal = value_
            self.averagePriceTotal_nsprefix_ = child_.prefix
            # validate type moneyMaxLengthToPoint18Type
            self.validate_moneyMaxLengthToPoint18Type(self.averagePriceTotal)
        elif nodeName_ == 'limPriceValuePerUnit' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'limPriceValuePerUnit')
            fval_ = self.gds_validate_decimal(fval_, node, 'limPriceValuePerUnit')
            self.limPriceValuePerUnit = fval_
            self.limPriceValuePerUnit_nsprefix_ = child_.prefix
            # validate type drugDecimalCodeType
            self.validate_drugDecimalCodeType(self.limPriceValuePerUnit)
        super(drugInfo, self).buildChildren(child_, node, nodeName_, True)
# end class drugInfo


class drugInterchangeInfo(GeneratedsSuper):
    """Сведения о лекарственных препаратах с учетом взаимозаменяемости"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugInterchangeReferenceInfo': MemberSpec_('drugInterchangeReferenceInfo', 'drugInterchangeReferenceInfoType', 0, 0, {'name': 'drugInterchangeReferenceInfo', 'type': 'drugInterchangeReferenceInfoType'}, 10),
        'drugInterchangeManualInfo': MemberSpec_('drugInterchangeManualInfo', 'drugInterchangeManualInfoType', 0, 0, {'name': 'drugInterchangeManualInfo', 'type': 'drugInterchangeManualInfoType'}, 10),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugInterchangeReferenceInfo=None, drugInterchangeManualInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.drugInterchangeReferenceInfo = drugInterchangeReferenceInfo
        self.drugInterchangeReferenceInfo_nsprefix_ = None
        self.drugInterchangeManualInfo = drugInterchangeManualInfo
        self.drugInterchangeManualInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInterchangeInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInterchangeInfo.subclass:
            return drugInterchangeInfo.subclass(*args_, **kwargs_)
        else:
            return drugInterchangeInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.drugInterchangeReferenceInfo is not None or
            self.drugInterchangeManualInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugInterchangeReferenceInfo':
            obj_ = drugInterchangeReferenceInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInterchangeReferenceInfo = obj_
            obj_.original_tagname_ = 'drugInterchangeReferenceInfo'
        elif nodeName_ == 'drugInterchangeManualInfo':
            obj_ = drugInterchangeManualInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInterchangeManualInfo = obj_
            obj_.original_tagname_ = 'drugInterchangeManualInfo'
# end class drugInterchangeInfo


class mustSpecifyDrugPackage(GeneratedsSuper):
    """Необходимо указание сведений об упаковке закупаемого лекарственного
    препарата. В случае указания блока контролируется заполненность блока
    packagingInfo во всех вариантах поставки лекарственных препаратов"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'specifyDrugPackageReason': MemberSpec_('specifyDrugPackageReason', ['text4000Type', 'xs:string'], 0, 0, {'name': 'specifyDrugPackageReason', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, specifyDrugPackageReason=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.specifyDrugPackageReason = specifyDrugPackageReason
        self.validate_text4000Type(self.specifyDrugPackageReason)
        self.specifyDrugPackageReason_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, mustSpecifyDrugPackage)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if mustSpecifyDrugPackage.subclass:
            return mustSpecifyDrugPackage.subclass(*args_, **kwargs_)
        else:
            return mustSpecifyDrugPackage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text4000Type(self, value):
        result = True
        # Validate type text4000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text4000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.specifyDrugPackageReason is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'specifyDrugPackageReason':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'specifyDrugPackageReason')
            value_ = self.gds_validate_string(value_, node, 'specifyDrugPackageReason')
            self.specifyDrugPackageReason = value_
            self.specifyDrugPackageReason_nsprefix_ = child_.prefix
            # validate type text4000Type
            self.validate_text4000Type(self.specifyDrugPackageReason)
# end class mustSpecifyDrugPackage


class objectInfoUsingTextForm(GeneratedsSuper):
    """Информация о вариантах поставки лекарственных препаратов формируется в
    текстовой форме.
    Начиная с версии 10.1, не допускается указание лекарственных препаратов в
    текстовой форме. Запрет не учитывается при приеме изменений, если в
    исходном размещенном извещении присутствует лекарственный препарат,
    реквизиты которого заполнены вручную"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugsInfo': MemberSpec_('drugsInfo', 'drugsInfo', 0, 0, {'name': 'drugsInfo', 'type': 'drugsInfo'}, None),
        'mustSpecifyDrugPackage': MemberSpec_('mustSpecifyDrugPackage', 'mustSpecifyDrugPackage', 0, 1, {'minOccurs': '0', 'name': 'mustSpecifyDrugPackage', 'type': 'mustSpecifyDrugPackage'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugsInfo=None, mustSpecifyDrugPackage=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.drugsInfo = drugsInfo
        self.drugsInfo_nsprefix_ = None
        self.mustSpecifyDrugPackage = mustSpecifyDrugPackage
        self.mustSpecifyDrugPackage_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, objectInfoUsingTextForm)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if objectInfoUsingTextForm.subclass:
            return objectInfoUsingTextForm.subclass(*args_, **kwargs_)
        else:
            return objectInfoUsingTextForm(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.drugsInfo is not None or
            self.mustSpecifyDrugPackage is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugsInfo':
            obj_ = drugsInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugsInfo = obj_
            obj_.original_tagname_ = 'drugsInfo'
        elif nodeName_ == 'mustSpecifyDrugPackage':
            obj_ = mustSpecifyDrugPackage.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.mustSpecifyDrugPackage = obj_
            obj_.original_tagname_ = 'mustSpecifyDrugPackage'
# end class objectInfoUsingTextForm


class drugQuantityCustomersInfo(GeneratedsSuper):
    """Количество (объем) закупаемого лекарственного препарата в разбивке по
    заказчикам в основном варианте поставки. Поле total в составе блока
    рассчитывается автоматически"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugQuantityCustomerInfo': MemberSpec_('drugQuantityCustomerInfo', 'drugQuantityCustomerInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'drugQuantityCustomerInfo', 'type': 'drugQuantityCustomerInfo'}, 12),
        'total': MemberSpec_('total', ['quantity18p11Type', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'total', 'type': 'xs:decimal'}, 12),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugQuantityCustomerInfo=None, total=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if drugQuantityCustomerInfo is None:
            self.drugQuantityCustomerInfo = []
        else:
            self.drugQuantityCustomerInfo = drugQuantityCustomerInfo
        self.drugQuantityCustomerInfo_nsprefix_ = None
        self.total = total
        self.validate_quantity18p11Type(self.total)
        self.total_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugQuantityCustomersInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugQuantityCustomersInfo.subclass:
            return drugQuantityCustomersInfo.subclass(*args_, **kwargs_)
        else:
            return drugQuantityCustomersInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_quantity18p11Type(self, value):
        result = True
        # Validate type quantity18p11Type, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 29:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on quantity18p11Type' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_quantity18p11Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_quantity18p11Type_patterns_, ))
                result = False
        return result
    validate_quantity18p11Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,11})?)$']]
    def hasContent_(self):
        if (
            self.drugQuantityCustomerInfo or
            self.total is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugQuantityCustomerInfo':
            obj_ = drugQuantityCustomerInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugQuantityCustomerInfo.append(obj_)
            obj_.original_tagname_ = 'drugQuantityCustomerInfo'
        elif nodeName_ == 'total' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'total')
            fval_ = self.gds_validate_decimal(fval_, node, 'total')
            self.total = fval_
            self.total_nsprefix_ = child_.prefix
            # validate type quantity18p11Type
            self.validate_quantity18p11Type(self.total)
# end class drugQuantityCustomersInfo


class drugQuantityCustomerInfo(GeneratedsSuper):
    """Количество (объем) закупаемого лекарственного препарата для заказчика"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'customer': MemberSpec_('customer', 'customer', 0, 0, {'name': 'customer', 'type': 'organizationRef'}, 12),
        'quantity': MemberSpec_('quantity', ['quantity18p11Type', 'xs:decimal'], 0, 0, {'name': 'quantity', 'type': 'xs:decimal'}, 12),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, customer=None, quantity=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer = customer
        self.customer_nsprefix_ = None
        self.quantity = quantity
        self.validate_quantity18p11Type(self.quantity)
        self.quantity_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugQuantityCustomerInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugQuantityCustomerInfo.subclass:
            return drugQuantityCustomerInfo.subclass(*args_, **kwargs_)
        else:
            return drugQuantityCustomerInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_quantity18p11Type(self, value):
        result = True
        # Validate type quantity18p11Type, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 29:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on quantity18p11Type' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_quantity18p11Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_quantity18p11Type_patterns_, ))
                result = False
        return result
    validate_quantity18p11Type_patterns_ = [['^(\\d{1,18}(\\.\\d{1,11})?)$']]
    def hasContent_(self):
        if (
            self.customer is not None or
            self.quantity is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'customer':
            class_obj_ = self.get_class_obj_(child_, organizationRef)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customer = obj_
            obj_.original_tagname_ = 'customer'
        elif nodeName_ == 'quantity' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'quantity')
            fval_ = self.gds_validate_decimal(fval_, node, 'quantity')
            self.quantity = fval_
            self.quantity_nsprefix_ = child_.prefix
            # validate type quantity18p11Type
            self.validate_quantity18p11Type(self.quantity)
# end class drugQuantityCustomerInfo


class quantityUndefined(GeneratedsSuper):
    """Невозможно определить количество (объём)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'quantityUndefined': MemberSpec_('quantityUndefined', 'quantityUndefined', 0, 0, {'fixed': 'true', 'name': 'quantityUndefined', 'type': 'xs:boolean'}, 12),
        'price': MemberSpec_('price', ['moneyLongType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'price', 'type': 'xs:string'}, 12),
        'drugPurchaseObjectCustomersInfo': MemberSpec_('drugPurchaseObjectCustomersInfo', 'drugPurchaseObjectCustomersInfo', 0, 1, {'minOccurs': '0', 'name': 'drugPurchaseObjectCustomersInfo', 'type': 'drugPurchaseObjectCustomersInfo'}, 12),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, quantityUndefined_member=None, price=None, drugPurchaseObjectCustomersInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.quantityUndefined = quantityUndefined_member
        self.quantityUndefined_nsprefix_ = None
        self.price = price
        self.validate_moneyLongType(self.price)
        self.price_nsprefix_ = None
        self.drugPurchaseObjectCustomersInfo = drugPurchaseObjectCustomersInfo
        self.drugPurchaseObjectCustomersInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, quantityUndefined)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if quantityUndefined.subclass:
            return quantityUndefined.subclass(*args_, **kwargs_)
        else:
            return quantityUndefined(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_moneyLongType(self, value):
        result = True
        # Validate type moneyLongType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 30:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyLongType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyLongType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyLongType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyLongType_patterns_, ))
                result = False
        return result
    validate_moneyLongType_patterns_ = [['^((-)?\\d+(\\.\\d{1,11})?)$']]
    def hasContent_(self):
        if (
            self.quantityUndefined is not None or
            self.price is not None or
            self.drugPurchaseObjectCustomersInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'quantityUndefined':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'quantityUndefined')
            ival_ = self.gds_validate_boolean(ival_, node, 'quantityUndefined')
            self.quantityUndefined = ival_
            self.quantityUndefined_nsprefix_ = child_.prefix
        elif nodeName_ == 'price':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'price')
            value_ = self.gds_validate_string(value_, node, 'price')
            self.price = value_
            self.price_nsprefix_ = child_.prefix
            # validate type moneyLongType
            self.validate_moneyLongType(self.price)
        elif nodeName_ == 'drugPurchaseObjectCustomersInfo':
            obj_ = drugPurchaseObjectCustomersInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugPurchaseObjectCustomersInfo = obj_
            obj_.original_tagname_ = 'drugPurchaseObjectCustomersInfo'
# end class quantityUndefined


class drugPurchaseObjectCustomersInfo(GeneratedsSuper):
    """Информация об участии заказчиков в закупке указанного лекарственного
    препарата. Контролируется обязательность заполнения при двух и более
    заказчиках в блоке "Требования заказчиков" (customerRequirements)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugPurchaseObjectCustomerInfo': MemberSpec_('drugPurchaseObjectCustomerInfo', 'drugPurchaseObjectCustomerInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'drugPurchaseObjectCustomerInfo', 'type': 'drugPurchaseObjectCustomerInfo'}, 12),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugPurchaseObjectCustomerInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if drugPurchaseObjectCustomerInfo is None:
            self.drugPurchaseObjectCustomerInfo = []
        else:
            self.drugPurchaseObjectCustomerInfo = drugPurchaseObjectCustomerInfo
        self.drugPurchaseObjectCustomerInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugPurchaseObjectCustomersInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugPurchaseObjectCustomersInfo.subclass:
            return drugPurchaseObjectCustomersInfo.subclass(*args_, **kwargs_)
        else:
            return drugPurchaseObjectCustomersInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.drugPurchaseObjectCustomerInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugPurchaseObjectCustomerInfo':
            obj_ = drugPurchaseObjectCustomerInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugPurchaseObjectCustomerInfo.append(obj_)
            obj_.original_tagname_ = 'drugPurchaseObjectCustomerInfo'
# end class drugPurchaseObjectCustomersInfo


class drugPurchaseObjectCustomerInfo(GeneratedsSuper):
    """Информация об участии заказчика в закупке указанного лекарственного
    препарата"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'customer': MemberSpec_('customer', 'customer', 0, 0, {'name': 'customer', 'type': 'organizationRef'}, 12),
        'drugPurchaseObjectIsPurchased': MemberSpec_('drugPurchaseObjectIsPurchased', 'xs:boolean', 0, 0, {'name': 'drugPurchaseObjectIsPurchased', 'type': 'xs:boolean'}, 12),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, customer=None, drugPurchaseObjectIsPurchased=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.customer = customer
        self.customer_nsprefix_ = None
        self.drugPurchaseObjectIsPurchased = drugPurchaseObjectIsPurchased
        self.drugPurchaseObjectIsPurchased_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugPurchaseObjectCustomerInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugPurchaseObjectCustomerInfo.subclass:
            return drugPurchaseObjectCustomerInfo.subclass(*args_, **kwargs_)
        else:
            return drugPurchaseObjectCustomerInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.customer is not None or
            self.drugPurchaseObjectIsPurchased is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'customer':
            class_obj_ = self.get_class_obj_(child_, organizationRef)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customer = obj_
            obj_.original_tagname_ = 'customer'
        elif nodeName_ == 'drugPurchaseObjectIsPurchased':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'drugPurchaseObjectIsPurchased')
            ival_ = self.gds_validate_boolean(ival_, node, 'drugPurchaseObjectIsPurchased')
            self.drugPurchaseObjectIsPurchased = ival_
            self.drugPurchaseObjectIsPurchased_nsprefix_ = child_.prefix
# end class drugPurchaseObjectCustomerInfo


class MNNInfoType(GeneratedsSuper):
    """Тип: Международное, группировочное или химическое наименование
    лекарственного препарата (МНН)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'MNNExternalCode': MemberSpec_('MNNExternalCode', ['drugExternalCodeType', 'xs:string'], 0, 0, {'name': 'MNNExternalCode', 'type': 'xs:string'}, None),
        'MNNName': MemberSpec_('MNNName', ['drugName2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'MNNName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, MNNExternalCode=None, MNNName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.MNNExternalCode = MNNExternalCode
        self.validate_drugExternalCodeType(self.MNNExternalCode)
        self.MNNExternalCode_nsprefix_ = None
        self.MNNName = MNNName
        self.validate_drugName2000Type(self.MNNName)
        self.MNNName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MNNInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MNNInfoType.subclass:
            return MNNInfoType.subclass(*args_, **kwargs_)
        else:
            return MNNInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugExternalCodeType(self, value):
        result = True
        # Validate type drugExternalCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugExternalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugExternalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_drugName2000Type(self, value):
        result = True
        # Validate type drugName2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugName2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugName2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.MNNExternalCode is not None or
            self.MNNName is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'MNNExternalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MNNExternalCode')
            value_ = self.gds_validate_string(value_, node, 'MNNExternalCode')
            self.MNNExternalCode = value_
            self.MNNExternalCode_nsprefix_ = child_.prefix
            # validate type drugExternalCodeType
            self.validate_drugExternalCodeType(self.MNNExternalCode)
        elif nodeName_ == 'MNNName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'MNNName')
            value_ = self.gds_validate_string(value_, node, 'MNNName')
            self.MNNName = value_
            self.MNNName_nsprefix_ = child_.prefix
            # validate type drugName2000Type
            self.validate_drugName2000Type(self.MNNName)
# end class MNNInfoType


class tradeInfoType(GeneratedsSuper):
    """Тип: Торговое наименование (ТН) лекарственного препарата"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'positionTradeNameExternalCode': MemberSpec_('positionTradeNameExternalCode', ['drugExternalCodeType', 'xs:string'], 0, 0, {'name': 'positionTradeNameExternalCode', 'type': 'xs:string'}, None),
        'tradeName': MemberSpec_('tradeName', ['drugNameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'tradeName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, positionTradeNameExternalCode=None, tradeName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.positionTradeNameExternalCode = positionTradeNameExternalCode
        self.validate_drugExternalCodeType(self.positionTradeNameExternalCode)
        self.positionTradeNameExternalCode_nsprefix_ = None
        self.tradeName = tradeName
        self.validate_drugNameType(self.tradeName)
        self.tradeName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tradeInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tradeInfoType.subclass:
            return tradeInfoType.subclass(*args_, **kwargs_)
        else:
            return tradeInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugExternalCodeType(self, value):
        result = True
        # Validate type drugExternalCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugExternalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugExternalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_drugNameType(self, value):
        result = True
        # Validate type drugNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.positionTradeNameExternalCode is not None or
            self.tradeName is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'positionTradeNameExternalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'positionTradeNameExternalCode')
            value_ = self.gds_validate_string(value_, node, 'positionTradeNameExternalCode')
            self.positionTradeNameExternalCode = value_
            self.positionTradeNameExternalCode_nsprefix_ = child_.prefix
            # validate type drugExternalCodeType
            self.validate_drugExternalCodeType(self.positionTradeNameExternalCode)
        elif nodeName_ == 'tradeName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tradeName')
            value_ = self.gds_validate_string(value_, node, 'tradeName')
            self.tradeName = value_
            self.tradeName_nsprefix_ = child_.prefix
            # validate type drugNameType
            self.validate_drugNameType(self.tradeName)
# end class tradeInfoType


class drugChangeInfoType(GeneratedsSuper):
    """Тип: Информация указываемая при ручном изменении лекарственного
    препарата"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'drugChangeReason': MemberSpec_('drugChangeReason', 'drugChangeReasonRef', 0, 0, {'name': 'drugChangeReason', 'type': 'drugChangeReasonRef'}, None),
        'commentOrRequestNumber': MemberSpec_('commentOrRequestNumber', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'commentOrRequestNumber', 'type': 'xs:string'}, None),
        'drugRef': MemberSpec_('drugRef', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'drugRef', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, drugChangeReason=None, commentOrRequestNumber=None, drugRef=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.drugChangeReason = drugChangeReason
        self.drugChangeReason_nsprefix_ = None
        self.commentOrRequestNumber = commentOrRequestNumber
        self.validate_text2000Type(self.commentOrRequestNumber)
        self.commentOrRequestNumber_nsprefix_ = None
        self.drugRef = drugRef
        self.validate_text2000Type(self.drugRef)
        self.drugRef_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugChangeInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugChangeInfoType.subclass:
            return drugChangeInfoType.subclass(*args_, **kwargs_)
        else:
            return drugChangeInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.drugChangeReason is not None or
            self.commentOrRequestNumber is not None or
            self.drugRef is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'drugChangeReason':
            obj_ = drugChangeReasonRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugChangeReason = obj_
            obj_.original_tagname_ = 'drugChangeReason'
        elif nodeName_ == 'commentOrRequestNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'commentOrRequestNumber')
            value_ = self.gds_validate_string(value_, node, 'commentOrRequestNumber')
            self.commentOrRequestNumber = value_
            self.commentOrRequestNumber_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.commentOrRequestNumber)
        elif nodeName_ == 'drugRef':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'drugRef')
            value_ = self.gds_validate_string(value_, node, 'drugRef')
            self.drugRef = value_
            self.drugRef_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.drugRef)
# end class drugChangeInfoType


class drugInterchangeReferenceInfoType(GeneratedsSuper):
    """Тип: Сведения о лекарственных препаратах с учетом взаимозаменяемости"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'isInterchange': MemberSpec_('isInterchange', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'isInterchange', 'type': 'xs:boolean'}, None),
        'interchangeGroupInfo': MemberSpec_('interchangeGroupInfo', 'interchangeGroupInfo', 0, 0, {'name': 'interchangeGroupInfo', 'type': 'interchangeGroupInfo'}, None),
        'drugInfo': MemberSpec_('drugInfo', 'drugInfo', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'drugInfo', 'type': 'drugInfo'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, isInterchange=None, interchangeGroupInfo=None, drugInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.isInterchange = isInterchange
        self.isInterchange_nsprefix_ = None
        self.interchangeGroupInfo = interchangeGroupInfo
        self.interchangeGroupInfo_nsprefix_ = None
        if drugInfo is None:
            self.drugInfo = []
        else:
            self.drugInfo = drugInfo
        self.drugInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInterchangeReferenceInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInterchangeReferenceInfoType.subclass:
            return drugInterchangeReferenceInfoType.subclass(*args_, **kwargs_)
        else:
            return drugInterchangeReferenceInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.isInterchange is not None or
            self.interchangeGroupInfo is not None or
            self.drugInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'isInterchange':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isInterchange')
            ival_ = self.gds_validate_boolean(ival_, node, 'isInterchange')
            self.isInterchange = ival_
            self.isInterchange_nsprefix_ = child_.prefix
        elif nodeName_ == 'interchangeGroupInfo':
            obj_ = interchangeGroupInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.interchangeGroupInfo = obj_
            obj_.original_tagname_ = 'interchangeGroupInfo'
        elif nodeName_ == 'drugInfo':
            obj_ = drugInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInfo.append(obj_)
            obj_.original_tagname_ = 'drugInfo'
# end class drugInterchangeReferenceInfoType


class interchangeGroupInfo(GeneratedsSuper):
    """Группа взаимозаменяемости по справочнику ЕСКЛП"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'groupCode': MemberSpec_('groupCode', ['drugExternalCodeType', 'xs:string'], 0, 0, {'name': 'groupCode', 'type': 'xs:string'}, None),
        'groupName': MemberSpec_('groupName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'groupName', 'type': 'xs:string'}, None),
        'groupOKEI': MemberSpec_('groupOKEI', 'groupOKEI', 0, 1, {'form': 'qualified', 'minOccurs': '0', 'name': 'groupOKEI', 'type': 'groupOKEI'}, None),
        'groupPriceValue': MemberSpec_('groupPriceValue', ['drugDecimalCodeType', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'groupPriceValue', 'type': 'xs:decimal'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, groupCode=None, groupName=None, groupOKEI=None, groupPriceValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.groupCode = groupCode
        self.validate_drugExternalCodeType(self.groupCode)
        self.groupCode_nsprefix_ = None
        self.groupName = groupName
        self.validate_text2000Type(self.groupName)
        self.groupName_nsprefix_ = None
        self.groupOKEI = groupOKEI
        self.groupOKEI_nsprefix_ = None
        self.groupPriceValue = groupPriceValue
        self.validate_drugDecimalCodeType(self.groupPriceValue)
        self.groupPriceValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, interchangeGroupInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if interchangeGroupInfo.subclass:
            return interchangeGroupInfo.subclass(*args_, **kwargs_)
        else:
            return interchangeGroupInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_drugExternalCodeType(self, value):
        result = True
        # Validate type drugExternalCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on drugExternalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on drugExternalCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_drugDecimalCodeType(self, value):
        result = True
        # Validate type drugDecimalCodeType, a restriction on xs:decimal.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, decimal_.Decimal):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (decimal_.Decimal)' % {"value": value, "lineno": lineno, })
                return False
            if len(str(value)) >= 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd totalDigits restriction on drugDecimalCodeType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.groupCode is not None or
            self.groupName is not None or
            self.groupOKEI is not None or
            self.groupPriceValue is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'groupCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'groupCode')
            value_ = self.gds_validate_string(value_, node, 'groupCode')
            self.groupCode = value_
            self.groupCode_nsprefix_ = child_.prefix
            # validate type drugExternalCodeType
            self.validate_drugExternalCodeType(self.groupCode)
        elif nodeName_ == 'groupName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'groupName')
            value_ = self.gds_validate_string(value_, node, 'groupName')
            self.groupName = value_
            self.groupName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.groupName)
        elif nodeName_ == 'groupOKEI':
            obj_ = groupOKEI.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.groupOKEI = obj_
            obj_.original_tagname_ = 'groupOKEI'
        elif nodeName_ == 'groupPriceValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'groupPriceValue')
            fval_ = self.gds_validate_decimal(fval_, node, 'groupPriceValue')
            self.groupPriceValue = fval_
            self.groupPriceValue_nsprefix_ = child_.prefix
            # validate type drugDecimalCodeType
            self.validate_drugDecimalCodeType(self.groupPriceValue)
# end class interchangeGroupInfo


class groupOKEI(GeneratedsSuper):
    """Единица измерения группы.
    Игнорируется при приеме, заполняется автоматически на основании справочника
    "Группы взаимозаменяемости лекарственных препаратов"
    (nsiFarmDrugInterchangeGroup)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', ['text500Type', 'xs:string'], 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'OKEI': MemberSpec_('OKEI', 'OKEIRef', 0, 0, {'name': 'OKEI', 'type': 'OKEIRef'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, name=None, OKEI=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_text500Type(self.name)
        self.name_nsprefix_ = None
        self.OKEI = OKEI
        self.OKEI_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, groupOKEI)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if groupOKEI.subclass:
            return groupOKEI.subclass(*args_, **kwargs_)
        else:
            return groupOKEI(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text500Type(self, value):
        result = True
        # Validate type text500Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text500Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text500Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.name is not None or
            self.OKEI is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text500Type
            self.validate_text500Type(self.name)
        elif nodeName_ == 'OKEI':
            obj_ = OKEIRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKEI = obj_
            obj_.original_tagname_ = 'OKEI'
# end class groupOKEI


class drugInterchangeManualInfoType(GeneratedsSuper):
    """Тип: Сведения о лекарственных препаратах с учетом взаимозаменяемости,
    своя группа"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'isInterchange': MemberSpec_('isInterchange', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'isInterchange', 'type': 'xs:boolean'}, None),
        'drugInfo': MemberSpec_('drugInfo', 'drugInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'drugInfo', 'type': 'drugInfo'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, isInterchange=None, drugInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.isInterchange = isInterchange
        self.isInterchange_nsprefix_ = None
        if drugInfo is None:
            self.drugInfo = []
        else:
            self.drugInfo = drugInfo
        self.drugInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInterchangeManualInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInterchangeManualInfoType.subclass:
            return drugInterchangeManualInfoType.subclass(*args_, **kwargs_)
        else:
            return drugInterchangeManualInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.isInterchange is not None or
            self.drugInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'isInterchange':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isInterchange')
            ival_ = self.gds_validate_boolean(ival_, node, 'isInterchange')
            self.isInterchange = ival_
            self.isInterchange_nsprefix_ = child_.prefix
        elif nodeName_ == 'drugInfo':
            obj_ = drugInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInfo.append(obj_)
            obj_.original_tagname_ = 'drugInfo'
# end class drugInterchangeManualInfoType


class drugInterchangeTextFormInfoType(GeneratedsSuper):
    """Тип: Сведения о лекарственных препаратах с учетом взаимозаменяемости,
    своя группа в текстовой форме"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'isInterchange': MemberSpec_('isInterchange', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'isInterchange', 'type': 'xs:boolean'}, None),
        'drugInfo': MemberSpec_('drugInfo', 'drugInfo', 1, 0, {'maxOccurs': 'unbounded', 'name': 'drugInfo', 'type': 'drugInfo'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, isInterchange=None, drugInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.isInterchange = isInterchange
        self.isInterchange_nsprefix_ = None
        if drugInfo is None:
            self.drugInfo = []
        else:
            self.drugInfo = drugInfo
        self.drugInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugInterchangeTextFormInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugInterchangeTextFormInfoType.subclass:
            return drugInterchangeTextFormInfoType.subclass(*args_, **kwargs_)
        else:
            return drugInterchangeTextFormInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.isInterchange is not None or
            self.drugInfo
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'isInterchange':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'isInterchange')
            ival_ = self.gds_validate_boolean(ival_, node, 'isInterchange')
            self.isInterchange = ival_
            self.isInterchange_nsprefix_ = child_.prefix
        elif nodeName_ == 'drugInfo':
            obj_ = drugInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.drugInfo.append(obj_)
            obj_.original_tagname_ = 'drugInfo'
# end class drugInterchangeTextFormInfoType


class KTRUCharacteristicValueType(GeneratedsSuper):
    """Тип КТРУ: Значение характеристики позиции КТРУЗаполняется для
    качественной характеристикиЗаполняется для количественной
    характеристикиЗаполняется для количественных характеристик"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'qualityDescription': MemberSpec_('qualityDescription', ['ktruDictNameType', 'xs:string'], 0, 0, {'name': 'qualityDescription', 'type': 'xs:string'}, 15),
        'OKEI': MemberSpec_('OKEI', 'OKEIRef', 0, 1, {'minOccurs': '0', 'name': 'OKEI', 'type': 'OKEIRef'}, 15),
        'valueFormat': MemberSpec_('valueFormat', ['ktruCharacteristicValueFormatType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'valueFormat', 'type': 'xs:string'}, 15),
        'rangeSet': MemberSpec_('rangeSet', 'rangeSet', 0, 0, {'name': 'rangeSet', 'type': 'rangeSet'}, 16),
        'valueSet': MemberSpec_('valueSet', 'valueSet', 0, 0, {'name': 'valueSet', 'type': 'valueSet'}, 16),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, qualityDescription=None, OKEI=None, valueFormat=None, rangeSet=None, valueSet=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.qualityDescription = qualityDescription
        self.validate_ktruDictNameType(self.qualityDescription)
        self.qualityDescription_nsprefix_ = None
        self.OKEI = OKEI
        self.OKEI_nsprefix_ = None
        self.valueFormat = valueFormat
        self.validate_ktruCharacteristicValueFormatType(self.valueFormat)
        self.valueFormat_nsprefix_ = None
        self.rangeSet = rangeSet
        self.rangeSet_nsprefix_ = None
        self.valueSet = valueSet
        self.valueSet_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KTRUCharacteristicValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KTRUCharacteristicValueType.subclass:
            return KTRUCharacteristicValueType.subclass(*args_, **kwargs_)
        else:
            return KTRUCharacteristicValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruDictNameType(self, value):
        result = True
        # Validate type ktruDictNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruCharacteristicValueFormatType(self, value):
        result = True
        # Validate type ktruCharacteristicValueFormatType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['N', 'A']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruCharacteristicValueFormatType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.qualityDescription is not None or
            self.OKEI is not None or
            self.valueFormat is not None or
            self.rangeSet is not None or
            self.valueSet is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'qualityDescription':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'qualityDescription')
            value_ = self.gds_validate_string(value_, node, 'qualityDescription')
            self.qualityDescription = value_
            self.qualityDescription_nsprefix_ = child_.prefix
            # validate type ktruDictNameType
            self.validate_ktruDictNameType(self.qualityDescription)
        elif nodeName_ == 'OKEI':
            obj_ = OKEIRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKEI = obj_
            obj_.original_tagname_ = 'OKEI'
        elif nodeName_ == 'valueFormat':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'valueFormat')
            value_ = self.gds_validate_string(value_, node, 'valueFormat')
            self.valueFormat = value_
            self.valueFormat_nsprefix_ = child_.prefix
            # validate type ktruCharacteristicValueFormatType
            self.validate_ktruCharacteristicValueFormatType(self.valueFormat)
        elif nodeName_ == 'rangeSet':
            obj_ = rangeSet.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rangeSet = obj_
            obj_.original_tagname_ = 'rangeSet'
        elif nodeName_ == 'valueSet':
            obj_ = valueSet.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.valueSet = obj_
            obj_.original_tagname_ = 'valueSet'
# end class KTRUCharacteristicValueType


class rangeSet(GeneratedsSuper):
    """Набор диапазонов значений характеристик"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'valueRange': MemberSpec_('valueRange', 'valueRange', 0, 0, {'name': 'valueRange', 'type': 'valueRange'}, 16),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, valueRange=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.valueRange = valueRange
        self.valueRange_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, rangeSet)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if rangeSet.subclass:
            return rangeSet.subclass(*args_, **kwargs_)
        else:
            return rangeSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.valueRange is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'valueRange':
            obj_ = valueRange.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.valueRange = obj_
            obj_.original_tagname_ = 'valueRange'
# end class rangeSet


class valueRange(GeneratedsSuper):
    """Диапазон значенийВ случае отсутствия должна быть задана верхняя граница
    диапазона (maxMathNotation + max) В случае отсутствия должна быть
    задана нижняя граница диапазона (minMathNotation + min)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'minMathNotation': MemberSpec_('minMathNotation', ['ktruMinMathNotationType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'minMathNotation', 'type': 'xs:string'}, 16),
        'min': MemberSpec_('min', ['min', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'min', 'type': 'xs:decimal'}, 16),
        'maxMathNotation': MemberSpec_('maxMathNotation', ['ktruMaxMathNotationType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'maxMathNotation', 'type': 'xs:string'}, 16),
        'max': MemberSpec_('max', ['max', 'xs:decimal'], 0, 1, {'minOccurs': '0', 'name': 'max', 'type': 'xs:decimal'}, 16),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, minMathNotation=None, min=None, maxMathNotation=None, max=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.minMathNotation = minMathNotation
        self.validate_ktruMinMathNotationType(self.minMathNotation)
        self.minMathNotation_nsprefix_ = None
        self.min = min
        self.min_nsprefix_ = None
        self.maxMathNotation = maxMathNotation
        self.validate_ktruMaxMathNotationType(self.maxMathNotation)
        self.maxMathNotation_nsprefix_ = None
        self.max = max
        self.max_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, valueRange)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if valueRange.subclass:
            return valueRange.subclass(*args_, **kwargs_)
        else:
            return valueRange(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruMinMathNotationType(self, value):
        result = True
        # Validate type ktruMinMathNotationType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['greater', 'greaterOrEqual']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruMinMathNotationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruMaxMathNotationType(self, value):
        result = True
        # Validate type ktruMaxMathNotationType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['less', 'lessOrEqual']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruMaxMathNotationType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.minMathNotation is not None or
            self.min is not None or
            self.maxMathNotation is not None or
            self.max is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'minMathNotation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'minMathNotation')
            value_ = self.gds_validate_string(value_, node, 'minMathNotation')
            self.minMathNotation = value_
            self.minMathNotation_nsprefix_ = child_.prefix
            # validate type ktruMinMathNotationType
            self.validate_ktruMinMathNotationType(self.minMathNotation)
        elif nodeName_ == 'min' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'min')
            fval_ = self.gds_validate_decimal(fval_, node, 'min')
            self.min = fval_
            self.min_nsprefix_ = child_.prefix
        elif nodeName_ == 'maxMathNotation':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'maxMathNotation')
            value_ = self.gds_validate_string(value_, node, 'maxMathNotation')
            self.maxMathNotation = value_
            self.maxMathNotation_nsprefix_ = child_.prefix
            # validate type ktruMaxMathNotationType
            self.validate_ktruMaxMathNotationType(self.maxMathNotation)
        elif nodeName_ == 'max' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'max')
            fval_ = self.gds_validate_decimal(fval_, node, 'max')
            self.max = fval_
            self.max_nsprefix_ = child_.prefix
# end class valueRange


class min(GeneratedsSuper):
    """Минимальное значение диапазона"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, min)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if min.subclass:
            return min.subclass(*args_, **kwargs_)
        else:
            return min(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_min(self, value):
        result = True
        # Validate type min, a restriction on xs:decimal.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class min


class max(GeneratedsSuper):
    """Максимальное значение диапазона"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, max)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if max.subclass:
            return max.subclass(*args_, **kwargs_)
        else:
            return max(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_max(self, value):
        result = True
        # Validate type max, a restriction on xs:decimal.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class max


class valueSet(GeneratedsSuper):
    """Набор конкретных значений характеристики"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'concreteValue': MemberSpec_('concreteValue', ['concreteValue', 'xs:decimal'], 0, 0, {'name': 'concreteValue', 'type': 'xs:decimal'}, 16),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, concreteValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.concreteValue = concreteValue
        self.concreteValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, valueSet)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if valueSet.subclass:
            return valueSet.subclass(*args_, **kwargs_)
        else:
            return valueSet(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.concreteValue is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'concreteValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_decimal(sval_, node, 'concreteValue')
            fval_ = self.gds_validate_decimal(fval_, node, 'concreteValue')
            self.concreteValue = fval_
            self.concreteValue_nsprefix_ = child_.prefix
# end class valueSet


class concreteValue(GeneratedsSuper):
    """Конкретное значение"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, concreteValue)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if concreteValue.subclass:
            return concreteValue.subclass(*args_, **kwargs_)
        else:
            return concreteValue(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_concreteValue(self, value):
        result = True
        # Validate type concreteValue, a restriction on xs:decimal.
        pass
        return result
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class concreteValue


class manualKTRUCharacteristicType(GeneratedsSuper):
    """Тип КТРУ: Характеристика товаров, работ, услуг для ввода в текстовой
    форме"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', ['ktruDictNameType', 'xs:string'], 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'type_': MemberSpec_('type_', ['ktruCharacteristicTypeType', 'xs:string'], 0, 0, {'name': 'type', 'type': 'xs:string'}, None),
        'values': MemberSpec_('values', 'values', 0, 0, {'name': 'values', 'type': 'values'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, name=None, type_=None, values=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_ktruDictNameType(self.name)
        self.name_nsprefix_ = None
        self.type_ = type_
        self.validate_ktruCharacteristicTypeType(self.type_)
        self.type__nsprefix_ = None
        self.values = values
        self.values_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, manualKTRUCharacteristicType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if manualKTRUCharacteristicType.subclass:
            return manualKTRUCharacteristicType.subclass(*args_, **kwargs_)
        else:
            return manualKTRUCharacteristicType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruDictNameType(self, value):
        result = True
        # Validate type ktruDictNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruCharacteristicTypeType(self, value):
        result = True
        # Validate type ktruCharacteristicTypeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruCharacteristicTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.name is not None or
            self.type_ is not None or
            self.values is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type ktruDictNameType
            self.validate_ktruDictNameType(self.name)
        elif nodeName_ == 'type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'type')
            value_ = self.gds_validate_string(value_, node, 'type')
            self.type_ = value_
            self.type_nsprefix_ = child_.prefix
            # validate type ktruCharacteristicTypeType
            self.validate_ktruCharacteristicTypeType(self.type_)
        elif nodeName_ == 'values':
            obj_ = values.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.values = obj_
            obj_.original_tagname_ = 'values'
# end class manualKTRUCharacteristicType


class values(GeneratedsSuper):
    """Допустимые значения характеристики"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'value': MemberSpec_('value', 'value', 1, 0, {'maxOccurs': 'unbounded', 'name': 'value', 'type': 'KTRUCharacteristicValueType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if value is None:
            self.value = []
        else:
            self.value = value
        self.value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, values)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if values.subclass:
            return values.subclass(*args_, **kwargs_)
        else:
            return values(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.value
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value':
            obj_ = KTRUCharacteristicValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.value.append(obj_)
            obj_.original_tagname_ = 'value'
# end class values


class refKTRUCharacteristicType(GeneratedsSuper):
    """Тип КТРУ: Характеристика товаров, работ, услуг для ввода из
    справочника"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['ktruDictCodeType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['ktruDictNameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'type_': MemberSpec_('type_', ['ktruCharacteristicTypeType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'type', 'type': 'xs:string'}, None),
        'kind': MemberSpec_('kind', ['ktruCharacteristicKindType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'kind', 'type': 'xs:string'}, None),
        'values': MemberSpec_('values', 'values', 0, 1, {'minOccurs': '0', 'name': 'values', 'type': 'values'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, type_=None, kind=None, values=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_ktruDictCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_ktruDictNameType(self.name)
        self.name_nsprefix_ = None
        self.type_ = type_
        self.validate_ktruCharacteristicTypeType(self.type_)
        self.type__nsprefix_ = None
        self.kind = kind
        self.validate_ktruCharacteristicKindType(self.kind)
        self.kind_nsprefix_ = None
        self.values = values
        self.values_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, refKTRUCharacteristicType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if refKTRUCharacteristicType.subclass:
            return refKTRUCharacteristicType.subclass(*args_, **kwargs_)
        else:
            return refKTRUCharacteristicType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruDictCodeType(self, value):
        result = True
        # Validate type ktruDictCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruDictCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruDictCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruDictNameType(self, value):
        result = True
        # Validate type ktruDictNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruCharacteristicTypeType(self, value):
        result = True
        # Validate type ktruCharacteristicTypeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruCharacteristicTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruCharacteristicKindType(self, value):
        result = True
        # Validate type ktruCharacteristicKindType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2', '3']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruCharacteristicKindType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.name is not None or
            self.type_ is not None or
            self.kind is not None or
            self.values is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type ktruDictCodeType
            self.validate_ktruDictCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type ktruDictNameType
            self.validate_ktruDictNameType(self.name)
        elif nodeName_ == 'type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'type')
            value_ = self.gds_validate_string(value_, node, 'type')
            self.type_ = value_
            self.type_nsprefix_ = child_.prefix
            # validate type ktruCharacteristicTypeType
            self.validate_ktruCharacteristicTypeType(self.type_)
        elif nodeName_ == 'kind':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'kind')
            value_ = self.gds_validate_string(value_, node, 'kind')
            self.kind = value_
            self.kind_nsprefix_ = child_.prefix
            # validate type ktruCharacteristicKindType
            self.validate_ktruCharacteristicKindType(self.kind)
        elif nodeName_ == 'values':
            obj_ = values.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.values = obj_
            obj_.original_tagname_ = 'values'
# end class refKTRUCharacteristicType


class rightSideKTRUCharacteristicType(GeneratedsSuper):
    """Тип: Характеристика позиции правой части (ПЧ) КТРУ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'name': MemberSpec_('name', ['ktruDictNameType', 'xs:string'], 0, 0, {'name': 'name', 'type': 'xs:string'}, None),
        'type_': MemberSpec_('type_', ['ktruCharacteristicTypeType', 'xs:string'], 0, 0, {'name': 'type', 'type': 'xs:string'}, None),
        'value': MemberSpec_('value', 'value', 0, 0, {'name': 'value', 'type': 'KTRUCharacteristicValueType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, name=None, type_=None, value=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.name = name
        self.validate_ktruDictNameType(self.name)
        self.name_nsprefix_ = None
        self.type_ = type_
        self.validate_ktruCharacteristicTypeType(self.type_)
        self.type__nsprefix_ = None
        self.value = value
        self.value_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, rightSideKTRUCharacteristicType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if rightSideKTRUCharacteristicType.subclass:
            return rightSideKTRUCharacteristicType.subclass(*args_, **kwargs_)
        else:
            return rightSideKTRUCharacteristicType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruDictNameType(self, value):
        result = True
        # Validate type ktruDictNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruDictNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_ktruCharacteristicTypeType(self, value):
        result = True
        # Validate type ktruCharacteristicTypeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ktruCharacteristicTypeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.name is not None or
            self.type_ is not None or
            self.value is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type ktruDictNameType
            self.validate_ktruDictNameType(self.name)
        elif nodeName_ == 'type':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'type')
            value_ = self.gds_validate_string(value_, node, 'type')
            self.type_ = value_
            self.type_nsprefix_ = child_.prefix
            # validate type ktruCharacteristicTypeType
            self.validate_ktruCharacteristicTypeType(self.type_)
        elif nodeName_ == 'value':
            obj_ = KTRUCharacteristicValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.value = obj_
            obj_.original_tagname_ = 'value'
# end class rightSideKTRUCharacteristicType


class addInfoKTRURef(GeneratedsSuper):
    """Тип: Ссылка на справочник дополнительных сведений позиции правой части
    КТРУ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['ktruDictCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text500Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_ktruDictCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text500Type(self.name)
        self.name_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, addInfoKTRURef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if addInfoKTRURef.subclass:
            return addInfoKTRURef.subclass(*args_, **kwargs_)
        else:
            return addInfoKTRURef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruDictCodeType(self, value):
        result = True
        # Validate type ktruDictCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruDictCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruDictCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text500Type(self, value):
        result = True
        # Validate type text500Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text500Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text500Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.name is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type ktruDictCodeType
            self.validate_ktruDictCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text500Type
            self.validate_text500Type(self.name)
# end class addInfoKTRURef


class tenderPlan2020InfoType(GeneratedsSuper):
    """Тип: Информация о плане-графике закупок с 01.01.2020"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'plan2020Number': MemberSpec_('plan2020Number', ['tenderPlan2020RegNumberType', 'xs:string'], 0, 0, {'name': 'plan2020Number', 'type': 'xs:string'}, None),
        'position2020Number': MemberSpec_('position2020Number', ['tenderPlan2020PositionNumberType', 'xs:string'], 0, 0, {'name': 'position2020Number', 'type': 'xs:string'}, 17),
        'position2020ExtNumber': MemberSpec_('position2020ExtNumber', ['documentNumberType', 'xs:string'], 0, 0, {'name': 'position2020ExtNumber', 'type': 'xs:string'}, 17),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, plan2020Number=None, position2020Number=None, position2020ExtNumber=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.plan2020Number = plan2020Number
        self.validate_tenderPlan2020RegNumberType(self.plan2020Number)
        self.plan2020Number_nsprefix_ = None
        self.position2020Number = position2020Number
        self.validate_tenderPlan2020PositionNumberType(self.position2020Number)
        self.position2020Number_nsprefix_ = None
        self.position2020ExtNumber = position2020ExtNumber
        self.validate_documentNumberType(self.position2020ExtNumber)
        self.position2020ExtNumber_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tenderPlan2020InfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tenderPlan2020InfoType.subclass:
            return tenderPlan2020InfoType.subclass(*args_, **kwargs_)
        else:
            return tenderPlan2020InfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_tenderPlan2020RegNumberType(self, value):
        result = True
        # Validate type tenderPlan2020RegNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tenderPlan2020RegNumberType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_tenderPlan2020PositionNumberType(self, value):
        result = True
        # Validate type tenderPlan2020PositionNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 24:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on tenderPlan2020PositionNumberType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_documentNumberType(self, value):
        result = True
        # Validate type documentNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on documentNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on documentNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.plan2020Number is not None or
            self.position2020Number is not None or
            self.position2020ExtNumber is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'plan2020Number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'plan2020Number')
            value_ = self.gds_validate_string(value_, node, 'plan2020Number')
            self.plan2020Number = value_
            self.plan2020Number_nsprefix_ = child_.prefix
            # validate type tenderPlan2020RegNumberType
            self.validate_tenderPlan2020RegNumberType(self.plan2020Number)
        elif nodeName_ == 'position2020Number':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'position2020Number')
            value_ = self.gds_validate_string(value_, node, 'position2020Number')
            self.position2020Number = value_
            self.position2020Number_nsprefix_ = child_.prefix
            # validate type tenderPlan2020PositionNumberType
            self.validate_tenderPlan2020PositionNumberType(self.position2020Number)
        elif nodeName_ == 'position2020ExtNumber':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'position2020ExtNumber')
            value_ = self.gds_validate_string(value_, node, 'position2020ExtNumber')
            self.position2020ExtNumber = value_
            self.position2020ExtNumber_nsprefix_ = child_.prefix
            # validate type documentNumberType
            self.validate_documentNumberType(self.position2020ExtNumber)
# end class tenderPlan2020InfoType


class tenderPlan2020OKPD2RefType(GeneratedsSuper):
    """Тип: Классификация по ОКПД2 в планах графиках с 01.01.2020"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'OKPD2': MemberSpec_('OKPD2', 'OKPD2', 0, 0, {'name': 'OKPD2', 'type': 'OKPD2Ref'}, 18),
        'undefined': MemberSpec_('undefined', 'undefined', 0, 0, {'default': '0000', 'name': 'undefined', 'type': 'xs:string'}, 18),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, OKPD2=None, undefined='0000', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.OKPD2 = OKPD2
        self.OKPD2_nsprefix_ = None
        self.undefined = undefined
        self.undefined_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tenderPlan2020OKPD2RefType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tenderPlan2020OKPD2RefType.subclass:
            return tenderPlan2020OKPD2RefType.subclass(*args_, **kwargs_)
        else:
            return tenderPlan2020OKPD2RefType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.OKPD2 is not None or
            self.undefined != "0000"
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OKPD2':
            class_obj_ = self.get_class_obj_(child_, OKPD2Ref)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OKPD2 = obj_
            obj_.original_tagname_ = 'OKPD2'
        elif nodeName_ == 'undefined':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'undefined')
            value_ = self.gds_validate_string(value_, node, 'undefined')
            self.undefined = value_
            self.undefined_nsprefix_ = child_.prefix
# end class tenderPlan2020OKPD2RefType


class tenderPlan2020KVRRefType(GeneratedsSuper):
    """Тип: Классификация по КВР в планах графиках с 01.01.2020"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'KVR': MemberSpec_('KVR', 'KVR', 0, 0, {'name': 'KVR', 'type': 'KVRRef'}, 19),
        'undefined': MemberSpec_('undefined', 'undefined', 0, 0, {'default': '000', 'name': 'undefined', 'type': 'xs:string'}, 19),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, KVR=None, undefined='000', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.KVR = KVR
        self.KVR_nsprefix_ = None
        self.undefined = undefined
        self.undefined_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tenderPlan2020KVRRefType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tenderPlan2020KVRRefType.subclass:
            return tenderPlan2020KVRRefType.subclass(*args_, **kwargs_)
        else:
            return tenderPlan2020KVRRefType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.KVR is not None or
            self.undefined != "000"
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'KVR':
            obj_ = KVRRef.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KVR = obj_
            obj_.original_tagname_ = 'KVR'
        elif nodeName_ == 'undefined':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'undefined')
            value_ = self.gds_validate_string(value_, node, 'undefined')
            self.undefined = value_
            self.undefined_nsprefix_ = child_.prefix
# end class tenderPlan2020KVRRefType


class publicDiscussionInfoType(GeneratedsSuper):
    """Тип: Сведения об общественном обсуждении"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'publicDiscussionInEISInfo': MemberSpec_('publicDiscussionInEISInfo', 'publicDiscussionInEISInfo', 0, 0, {'name': 'publicDiscussionInEISInfo', 'type': 'publicDiscussionInEISInfo'}, 20),
        'publicDiscussionNotInEIS': MemberSpec_('publicDiscussionNotInEIS', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'publicDiscussionNotInEIS', 'type': 'xs:boolean'}, 20),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, publicDiscussionInEISInfo=None, publicDiscussionNotInEIS=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publicDiscussionInEISInfo = publicDiscussionInEISInfo
        self.publicDiscussionInEISInfo_nsprefix_ = None
        self.publicDiscussionNotInEIS = publicDiscussionNotInEIS
        self.publicDiscussionNotInEIS_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, publicDiscussionInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if publicDiscussionInfoType.subclass:
            return publicDiscussionInfoType.subclass(*args_, **kwargs_)
        else:
            return publicDiscussionInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.publicDiscussionInEISInfo is not None or
            self.publicDiscussionNotInEIS is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'publicDiscussionInEISInfo':
            obj_ = publicDiscussionInEISInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.publicDiscussionInEISInfo = obj_
            obj_.original_tagname_ = 'publicDiscussionInEISInfo'
        elif nodeName_ == 'publicDiscussionNotInEIS':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'publicDiscussionNotInEIS')
            ival_ = self.gds_validate_boolean(ival_, node, 'publicDiscussionNotInEIS')
            self.publicDiscussionNotInEIS = ival_
            self.publicDiscussionNotInEIS_nsprefix_ = child_.prefix
# end class publicDiscussionInfoType


class publicDiscussionInEISInfo(GeneratedsSuper):
    """Общественное обсуждение проводится в ЕИС"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'publicDiscussionInEIS': MemberSpec_('publicDiscussionInEIS', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'publicDiscussionInEIS', 'type': 'xs:boolean'}, 20),
        'publicDiscussionNum': MemberSpec_('publicDiscussionNum', ['publicDiscussionNumType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'publicDiscussionNum', 'type': 'xs:string'}, 20),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, publicDiscussionInEIS=None, publicDiscussionNum=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.publicDiscussionInEIS = publicDiscussionInEIS
        self.publicDiscussionInEIS_nsprefix_ = None
        self.publicDiscussionNum = publicDiscussionNum
        self.validate_publicDiscussionNumType(self.publicDiscussionNum)
        self.publicDiscussionNum_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, publicDiscussionInEISInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if publicDiscussionInEISInfo.subclass:
            return publicDiscussionInEISInfo.subclass(*args_, **kwargs_)
        else:
            return publicDiscussionInEISInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_publicDiscussionNumType(self, value):
        result = True
        # Validate type publicDiscussionNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_publicDiscussionNumType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_publicDiscussionNumType_patterns_, ))
                result = False
        return result
    validate_publicDiscussionNumType_patterns_ = [['^(\\d{8}|\\d{12})$']]
    def hasContent_(self):
        if (
            self.publicDiscussionInEIS is not None or
            self.publicDiscussionNum is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'publicDiscussionInEIS':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'publicDiscussionInEIS')
            ival_ = self.gds_validate_boolean(ival_, node, 'publicDiscussionInEIS')
            self.publicDiscussionInEIS = ival_
            self.publicDiscussionInEIS_nsprefix_ = child_.prefix
        elif nodeName_ == 'publicDiscussionNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'publicDiscussionNum')
            value_ = self.gds_validate_string(value_, node, 'publicDiscussionNum')
            self.publicDiscussionNum = value_
            self.publicDiscussionNum_nsprefix_ = child_.prefix
            # validate type publicDiscussionNumType
            self.validate_publicDiscussionNumType(self.publicDiscussionNum)
# end class publicDiscussionInEISInfo


class bankSupportContractRequiredInfoType(GeneratedsSuper):
    """Тип: Информации о банковском и (или) казначейском сопровождении
    контакта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'bankSupportContractRequired': MemberSpec_('bankSupportContractRequired', 'xs:boolean', 0, 1, {'fixed': 'true', 'minOccurs': '0', 'name': 'bankSupportContractRequired', 'type': 'xs:boolean'}, None),
        'treasurySupportContractRequired': MemberSpec_('treasurySupportContractRequired', 'xs:boolean', 0, 1, {'fixed': 'true', 'minOccurs': '0', 'name': 'treasurySupportContractRequired', 'type': 'xs:boolean'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, bankSupportContractRequired=None, treasurySupportContractRequired=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.bankSupportContractRequired = bankSupportContractRequired
        self.bankSupportContractRequired_nsprefix_ = None
        self.treasurySupportContractRequired = treasurySupportContractRequired
        self.treasurySupportContractRequired_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, bankSupportContractRequiredInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if bankSupportContractRequiredInfoType.subclass:
            return bankSupportContractRequiredInfoType.subclass(*args_, **kwargs_)
        else:
            return bankSupportContractRequiredInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.bankSupportContractRequired is not None or
            self.treasurySupportContractRequired is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'bankSupportContractRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'bankSupportContractRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'bankSupportContractRequired')
            self.bankSupportContractRequired = ival_
            self.bankSupportContractRequired_nsprefix_ = child_.prefix
        elif nodeName_ == 'treasurySupportContractRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'treasurySupportContractRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'treasurySupportContractRequired')
            self.treasurySupportContractRequired = ival_
            self.treasurySupportContractRequired_nsprefix_ = child_.prefix
# end class bankSupportContractRequiredInfoType


class bankSupportContractRequiredInfo2020Type(GeneratedsSuper):
    """Тип: Информации о банковском и (или) казначейском сопровождении контакта
    для ЭA20,ЭОК20,ЭЗК20,ЭЗТ,ЭЗакА20,ЭЗакК20"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'bankSupportContractRequired': MemberSpec_('bankSupportContractRequired', 'xs:boolean', 0, 1, {'fixed': 'true', 'minOccurs': '0', 'name': 'bankSupportContractRequired', 'type': 'xs:boolean'}, None),
        'treasurySupportContractInfo': MemberSpec_('treasurySupportContractInfo', 'treasurySupportContractInfo', 0, 1, {'minOccurs': '0', 'name': 'treasurySupportContractInfo', 'type': 'treasurySupportContractInfo'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, bankSupportContractRequired=None, treasurySupportContractInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.bankSupportContractRequired = bankSupportContractRequired
        self.bankSupportContractRequired_nsprefix_ = None
        self.treasurySupportContractInfo = treasurySupportContractInfo
        self.treasurySupportContractInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, bankSupportContractRequiredInfo2020Type)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if bankSupportContractRequiredInfo2020Type.subclass:
            return bankSupportContractRequiredInfo2020Type.subclass(*args_, **kwargs_)
        else:
            return bankSupportContractRequiredInfo2020Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.bankSupportContractRequired is not None or
            self.treasurySupportContractInfo is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'bankSupportContractRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'bankSupportContractRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'bankSupportContractRequired')
            self.bankSupportContractRequired = ival_
            self.bankSupportContractRequired_nsprefix_ = child_.prefix
        elif nodeName_ == 'treasurySupportContractInfo':
            obj_ = treasurySupportContractInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.treasurySupportContractInfo = obj_
            obj_.original_tagname_ = 'treasurySupportContractInfo'
# end class bankSupportContractRequiredInfo2020Type


class treasurySupportContractInfo(GeneratedsSuper):
    """Информация о казначейском сопровождении контракта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'treasurySupportContractRequired': MemberSpec_('treasurySupportContractRequired', 'xs:boolean', 0, 0, {'fixed': 'true', 'name': 'treasurySupportContractRequired', 'type': 'xs:boolean'}, None),
        'treasurySupportContractType': MemberSpec_('treasurySupportContractType', ['treasurySupportContractEnum', 'xs:string'], 0, 0, {'name': 'treasurySupportContractType', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, treasurySupportContractRequired=None, treasurySupportContractType=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.treasurySupportContractRequired = treasurySupportContractRequired
        self.treasurySupportContractRequired_nsprefix_ = None
        self.treasurySupportContractType = treasurySupportContractType
        self.validate_treasurySupportContractEnum(self.treasurySupportContractType)
        self.treasurySupportContractType_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, treasurySupportContractInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if treasurySupportContractInfo.subclass:
            return treasurySupportContractInfo.subclass(*args_, **kwargs_)
        else:
            return treasurySupportContractInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_treasurySupportContractEnum(self, value):
        result = True
        # Validate type treasurySupportContractEnum, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['ALL', 'ADV']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on treasurySupportContractEnum' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.treasurySupportContractRequired is not None or
            self.treasurySupportContractType is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'treasurySupportContractRequired':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'treasurySupportContractRequired')
            ival_ = self.gds_validate_boolean(ival_, node, 'treasurySupportContractRequired')
            self.treasurySupportContractRequired = ival_
            self.treasurySupportContractRequired_nsprefix_ = child_.prefix
        elif nodeName_ == 'treasurySupportContractType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'treasurySupportContractType')
            value_ = self.gds_validate_string(value_, node, 'treasurySupportContractType')
            self.treasurySupportContractType = value_
            self.treasurySupportContractType_nsprefix_ = child_.prefix
            # validate type treasurySupportContractEnum
            self.validate_treasurySupportContractEnum(self.treasurySupportContractType)
# end class treasurySupportContractInfo


class paymentGuaranteeInfoType(GeneratedsSuper):
    """Тип: Информация о платеже для гарантийных обязательств в извещении"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'amount': MemberSpec_('amount', ['moneyType', 'xs:string'], 0, 0, {'name': 'amount', 'type': 'xs:string'}, None),
        'part': MemberSpec_('part', ['percentRestr0100D11Type', 'xs:double'], 0, 1, {'minOccurs': '0', 'name': 'part', 'type': 'xs:double'}, None),
        'procedureInfo': MemberSpec_('procedureInfo', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'procedureInfo', 'type': 'xs:string'}, None),
        'account': MemberSpec_('account', 'account', 0, 1, {'minOccurs': '0', 'name': 'account', 'type': 'paymentPropertysType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, amount=None, part=None, procedureInfo=None, account=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.amount = amount
        self.validate_moneyType(self.amount)
        self.amount_nsprefix_ = None
        self.part = part
        self.validate_percentRestr0100D11Type(self.part)
        self.part_nsprefix_ = None
        self.procedureInfo = procedureInfo
        self.validate_text2000Type(self.procedureInfo)
        self.procedureInfo_nsprefix_ = None
        self.account = account
        self.account_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, paymentGuaranteeInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if paymentGuaranteeInfoType.subclass:
            return paymentGuaranteeInfoType.subclass(*args_, **kwargs_)
        else:
            return paymentGuaranteeInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_moneyType(self, value):
        result = True
        # Validate type moneyType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 21:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on moneyType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_moneyType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_moneyType_patterns_, ))
                result = False
        return result
    validate_moneyType_patterns_ = [['^((-)?\\d+(\\.\\d{1,2})?)$']]
    def validate_percentRestr0100D11Type(self, value):
        result = True
        # Validate type percentRestr0100D11Type, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if value < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minInclusive restriction on percentRestr0100D11Type' % {"value": value, "lineno": lineno} )
                result = False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on percentRestr0100D11Type' % {"value": value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_percentRestr0100D11Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_percentRestr0100D11Type_patterns_, ))
                result = False
        return result
    validate_percentRestr0100D11Type_patterns_ = [['^(\\d+(\\.\\d{1,11})?)$']]
    def validate_text2000Type(self, value):
        result = True
        # Validate type text2000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text2000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.amount is not None or
            self.part is not None or
            self.procedureInfo is not None or
            self.account is not None
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'amount':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'amount')
            value_ = self.gds_validate_string(value_, node, 'amount')
            self.amount = value_
            self.amount_nsprefix_ = child_.prefix
            # validate type moneyType
            self.validate_moneyType(self.amount)
        elif nodeName_ == 'part' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'part')
            fval_ = self.gds_validate_double(fval_, node, 'part')
            self.part = fval_
            self.part_nsprefix_ = child_.prefix
            # validate type percentRestr0100D11Type
            self.validate_percentRestr0100D11Type(self.part)
        elif nodeName_ == 'procedureInfo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'procedureInfo')
            value_ = self.gds_validate_string(value_, node, 'procedureInfo')
            self.procedureInfo = value_
            self.procedureInfo_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.procedureInfo)
        elif nodeName_ == 'account':
            obj_ = paymentPropertysType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.account = obj_
            obj_.original_tagname_ = 'account'
# end class paymentGuaranteeInfoType


class control99ControlObjectWithMandatoryDocsInfoType(control99DocumentObjectType):
    """Тип: Сведения об объектах контроля по 99 статье с обязательным блоком
    controlDocumentsInfo"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'controlDocumentsInfo': MemberSpec_('controlDocumentsInfo', 'controlDocumentsInfo', 0, 0, {'name': 'controlDocumentsInfo', 'type': 'controlDocumentsInfo'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = control99DocumentObjectType
    def __init__(self, name=None, date=None, number=None, controlDocumentsInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(control99ControlObjectWithMandatoryDocsInfoType, self).__init__(name, date, number,  **kwargs_)
        self.controlDocumentsInfo = controlDocumentsInfo
        self.controlDocumentsInfo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, control99ControlObjectWithMandatoryDocsInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if control99ControlObjectWithMandatoryDocsInfoType.subclass:
            return control99ControlObjectWithMandatoryDocsInfoType.subclass(*args_, **kwargs_)
        else:
            return control99ControlObjectWithMandatoryDocsInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.controlDocumentsInfo is not None or
            super(control99ControlObjectWithMandatoryDocsInfoType, self).hasContent_()
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(control99ControlObjectWithMandatoryDocsInfoType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'controlDocumentsInfo':
            obj_ = controlDocumentsInfo.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.controlDocumentsInfo = obj_
            obj_.original_tagname_ = 'controlDocumentsInfo'
        super(control99ControlObjectWithMandatoryDocsInfoType, self).buildChildren(child_, node, nodeName_, True)
# end class control99ControlObjectWithMandatoryDocsInfoType


class attachmentInfo(attachmentType):
    """Вложенный файл"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'signatureCheckUrl': MemberSpec_('signatureCheckUrl', ['hrefType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'signatureCheckUrl', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = attachmentType
    def __init__(self, publishedContentId=None, fileName=None, fileSize=None, docDescription=None, docDate=None, url=None, contentId=None, content=None, cryptoSigns=None, signatureCheckUrl=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(attachmentInfo, self).__init__(publishedContentId, fileName, fileSize, docDescription, docDate, url, contentId, content, cryptoSigns,  **kwargs_)
        self.signatureCheckUrl = signatureCheckUrl
        self.validate_hrefType(self.signatureCheckUrl)
        self.signatureCheckUrl_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, attachmentInfo)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if attachmentInfo.subclass:
            return attachmentInfo.subclass(*args_, **kwargs_)
        else:
            return attachmentInfo(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_hrefType(self, value):
        result = True
        # Validate type hrefType, a restriction on xs:string.
        pass
        return result
    def hasContent_(self):
        if (
            self.signatureCheckUrl is not None or
            super(attachmentInfo, self).hasContent_()
        ):
            return True
        else:
            return False
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(attachmentInfo, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'signatureCheckUrl':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'signatureCheckUrl')
            value_ = self.gds_validate_string(value_, node, 'signatureCheckUrl')
            self.signatureCheckUrl = value_
            self.signatureCheckUrl_nsprefix_ = child_.prefix
            # validate type hrefType
            self.validate_hrefType(self.signatureCheckUrl)
        super(attachmentInfo, self).buildChildren(child_, node, nodeName_, True)
# end class attachmentInfo


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xs_int'
        rootClass = xs_int
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_=namespacedefs,
##             pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xs_int'
        rootClass = xs_int
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         content = etree_.tostring(
##             rootElement, pretty_print=True,
##             xml_declaration=True, encoding="utf-8")
##         sys.stdout.write(str(content))
##         sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xs_int'
        rootClass = xs_int
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
##     if not silence:
##         sys.stdout.write('<?xml version="1.0" ?>\n')
##         rootObj.export(
##             sys.stdout, 0, name_=rootTag,
##             namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'xs_int'
        rootClass = xs_int
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('#from CommonTypes import *\n\n')
##         sys.stdout.write('import CommonTypes as model_\n\n')
##         sys.stdout.write('rootObj = model_.rootClass(\n')
##         rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##         sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
    "{http://zakupki.gov.ru/oos/base/1}bikType": "bikType2",
    "{http://zakupki.gov.ru/oos/base/1}checkResultNumberType": "checkResultNumberType3",
    "{http://zakupki.gov.ru/oos/base/1}hrefType": "hrefType4",
    "{http://zakupki.gov.ru/oos/base/1}innType": "innType5",
    "{http://zakupki.gov.ru/oos/base/1}monthType": "monthType6",
    "{http://zakupki.gov.ru/oos/base/1}organizationRef": "organizationRef1",
    "{http://zakupki.gov.ru/oos/base/1}prescriptionNumberType": "prescriptionNumberType7",
    "{http://zakupki.gov.ru/oos/base/1}yearType": "yearType8",
    "{http://zakupki.gov.ru/oos/common/1}appRejectedReasonType": "appRejectedReasonType9",
    "{http://zakupki.gov.ru/oos/common/1}commissionMemberType": "commissionMemberType11",
    "{http://zakupki.gov.ru/oos/common/1}commissionType": "commissionType10",
    "{http://zakupki.gov.ru/oos/common/1}organizationType": "organizationType12",
    "{http://zakupki.gov.ru/oos/common/1}participantType": "participantType13",
    "{http://zakupki.gov.ru/oos/common/1}signatureType": "signatureType14",

}
__all__ = [
    "ETPRef",
    "KTRU",
    "KTRUCharacteristicValueType",
    "KTRURef",
    "KVRFinancingType",
    "KVRFinancingsType",
    "KVRRef",
    "MNNInfo",
    "MNNInfoType",
    "NPASt14Ref",
    "OKEIRef",
    "OKFSRef",
    "OKOPFRef",
    "OKPD2",
    "OKPD2Ref",
    "OKPORef",
    "OKSMRef",
    "OKTMOPPORef",
    "OKTMORef",
    "abandonedReasonRef",
    "addInfoKTRURef",
    "addRequirement",
    "addRequirementType",
    "addRequirements",
    "appRejectedReasonType",
    "attachmentInfo",
    "attachmentListSignCheckUrlType",
    "attachmentListType",
    "attachmentListWithKindType",
    "attachmentType",
    "attachmentWithKindType",
    "bankSupportContractRequiredInfo2020Type",
    "bankSupportContractRequiredInfoType",
    "budgetFundsContractRef",
    "changePriceFoundationRef",
    "characteristics",
    "closedEPCasesRef",
    "code",
    "commissionMemberType",
    "commissionMembers",
    "commissionRoleType",
    "commissionType",
    "commonUnitsMeasurementsRef",
    "concreteValue",
    "contactInfo",
    "content",
    "contractLifeCycleCaseRef",
    "contractOKEIExtendedRef",
    "contractOKEIRef",
    "contractRefusalReasonRef",
    "control99ControlAuthorityInfoType",
    "control99ControlObjectWithMandatoryDocsInfoType",
    "control99CustomerInfoType",
    "control99DocumentObjectType",
    "control99NoticeComplianceWithDocType",
    "control99ResponsibleType",
    "controlDocumentsInfo",
    "controlObjectsInfo",
    "cryptoSigns",
    "currencyCBRFRef",
    "currencyRateType",
    "currencyRef",
    "customerInfo",
    "customerQuantities",
    "customerQuantity",
    "deviationFactFoundationRef",
    "docPropertyType",
    "docRejectReasonRef",
    "docType",
    "documentKindRef",
    "dosageInfo",
    "drugChangeInfoType",
    "drugChangeReasonRef",
    "drugInfo",
    "drugInfoType",
    "drugInfoUsingTextFormType",
    "drugInterchangeInfo",
    "drugInterchangeManualInfoType",
    "drugInterchangeReferenceInfoType",
    "drugInterchangeTextFormInfoType",
    "drugPurchaseObjectCustomerInfo",
    "drugPurchaseObjectCustomersInfo",
    "drugPurchaseObjectInfo",
    "drugQuantityCustomerInfo",
    "drugQuantityCustomersInfo",
    "drugsInfo",
    "errorInfoType",
    "evasDevFactFoundationRef",
    "exception",
    "exclusionReason615Ref",
    "extPrintFormType",
    "financeResourcesType",
    "fundingSources615Ref",
    "groupOKEI",
    "individualPersonForeignStateInfo",
    "individualPersonRFInfo",
    "interchangeGroupInfo",
    "legalEntityForeignStateInfo",
    "legalEntityRFInfo",
    "manualKTRUCharacteristicType",
    "max",
    "medicamentalFormInfo",
    "min",
    "mustSpecifyDrugPackage",
    "name",
    "nationalCode",
    "objectInfoUsingReferenceInfo",
    "objectInfoUsingTextForm",
    "organizationRef",
    "organizationType",
    "packagingInfo",
    "participantType",
    "paymentGuaranteeInfoType",
    "paymentPropertysType",
    "personType",
    "placeOfStayInRFInfo",
    "placeOfStayInRegCountryInfo",
    "placingWayRef",
    "prefRateRef",
    "preferenseType",
    "prefsReqsRef",
    "printFormType",
    "publicDiscussionInEISInfo",
    "publicDiscussionInfoType",
    "purchaseDrugObjectsInfoType",
    "purchaseIsMaxPriceCurrencyType",
    "purchaseObject",
    "purchaseObjectsType",
    "purchaseSubjectRef",
    "qualifiedContractorRef",
    "quantity",
    "quantityUndefined",
    "rangeSet",
    "rate",
    "refKTRUCharacteristicType",
    "registerInRFTaxBodiesInfo",
    "rejectReasonRef",
    "reqValue",
    "requirement2020Type",
    "requirement2020WithAddReqsType",
    "requirementRestrictionType",
    "requirementType",
    "requirementWithAddReqsType",
    "requirementsType",
    "restrictionSt14",
    "restrictionSt14Type",
    "restrictionType",
    "righSideKTRURef",
    "rightSideKTRUCharacteristicType",
    "schemeVersion",
    "serviceWorkSt166Ref",
    "sid",
    "signature",
    "signatureType",
    "targetArticleFinancingType",
    "targetArticleFinancingsType",
    "tenderPlan2020InfoType",
    "tenderPlan2020KVRRefType",
    "tenderPlan2020OKPD2RefType",
    "terminationGround615Ref",
    "terminationReason615Ref",
    "tradeInfo",
    "tradeInfoType",
    "treasurySupportContractInfo",
    "type_",
    "valueRange",
    "valueSet",
    "values",
    "violationType"
]
