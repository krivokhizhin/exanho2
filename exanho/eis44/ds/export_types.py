#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Wed Jan  6 18:39:07 2021 by generateDS.py version 2.37.11.
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

from .IntegrationTypes import zfcs_contract2015Type
from .IntegrationTypes import zfcs_contractCancel2015Type
from .IntegrationTypes import zfcs_contractProcedure2015Type
from .IntegrationTypes import zfcs_contractProcedureCancel2015Type

class export(GeneratedsSuper):
    """Схема данных подсистемы экспорта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'contract': MemberSpec_('contract', 'contract', 1, 0, {'maxOccurs': 'unbounded', 'name': 'contract', 'type': 'zfcs_contract2015Type'}, 1),
        'contractCancel': MemberSpec_('contractCancel', 'zfcs_contractCancel2015Type', 1, 0, {'maxOccurs': 'unbounded', 'name': 'contractCancel', 'type': 'zfcs_contractCancel2015Type'}, 1),
        'contractProcedure': MemberSpec_('contractProcedure', 'contractProcedure', 1, 0, {'maxOccurs': 'unbounded', 'name': 'contractProcedure', 'type': 'zfcs_contractProcedure2015Type'}, 1),
        'contractProcedureCancel': MemberSpec_('contractProcedureCancel', 'zfcs_contractProcedureCancel2015Type', 1, 0, {'maxOccurs': 'unbounded', 'name': 'contractProcedureCancel', 'type': 'zfcs_contractProcedureCancel2015Type'}, 1),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, contract=None, contractCancel=None, contractProcedure=None, contractProcedureCancel=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if contract is None:
            self.contract = []
        else:
            self.contract = contract
        self.contract_nsprefix_ = None
        if contractCancel is None:
            self.contractCancel = []
        else:
            self.contractCancel = contractCancel
        self.contractCancel_nsprefix_ = None
        if contractProcedure is None:
            self.contractProcedure = []
        else:
            self.contractProcedure = contractProcedure
        self.contractProcedure_nsprefix_ = None
        if contractProcedureCancel is None:
            self.contractProcedureCancel = []
        else:
            self.contractProcedureCancel = contractProcedureCancel
        self.contractProcedureCancel_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, export)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if export.subclass:
            return export.subclass(*args_, **kwargs_)
        else:
            return export(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.contract or
            self.contractCancel or
            self.contractProcedure or
            self.contractProcedureCancel
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
        if nodeName_ == 'contract':
            obj_ = zfcs_contract2015Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contract.append(obj_)
            obj_.original_tagname_ = 'contract'
        elif nodeName_ == 'contractCancel':
            obj_ = zfcs_contractCancel2015Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contractCancel.append(obj_)
            obj_.original_tagname_ = 'contractCancel'
        elif nodeName_ == 'contractProcedure':
            obj_ = zfcs_contractProcedure2015Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contractProcedure.append(obj_)
            obj_.original_tagname_ = 'contractProcedure'
        elif nodeName_ == 'contractProcedureCancel':
            obj_ = zfcs_contractProcedureCancel2015Type.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contractProcedureCancel.append(obj_)
            obj_.original_tagname_ = 'contractProcedureCancel'
# end class export


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
        rootTag = 'export'
        rootClass = export
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
        rootTag = 'export'
        rootClass = export
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
        rootTag = 'export'
        rootClass = export
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
        rootTag = 'export'
        rootClass = export
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('#from export_types import *\n\n')
##         sys.stdout.write('import export_types as model_\n\n')
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
    "BIK",
    "BODocInfo",
    "BOSignType",
    "EFNumber",
    "EPType",
    "ETPPrivilegesByOrganizationRole",
    "ETPRef",
    "GRBSCode",
    "GUID",
    "IKUInfo",
    "IKZInfo",
    "INN",
    "KBK",
    "KBK2016",
    "KBKInfo",
    "KBKTotalsInfo",
    "KBKType",
    "KBKsInfo",
    "KBKsTotalsInfo",
    "KOSGU",
    "KPP",
    "KTRU",
    "KTRUCharacteristicValueType",
    "KTRUInfo",
    "KTRUNotUsingReason",
    "KTRURef",
    "KTRUs",
    "KVR",
    "KVRFinancingType",
    "KVRFinancingsType",
    "KVRRef",
    "KVRTotalInfo",
    "KVRTotalsInfo",
    "MNNInfo",
    "MNNInfoType",
    "MNNTextForm",
    "MNNsInfo",
    "NIR",
    "NPASt14Ref",
    "NPAsInfo",
    "NSI",
    "OGRN",
    "OKATO",
    "OKEIRef",
    "OKEIType",
    "OKEIs",
    "OKFSRef",
    "OKOGU",
    "OKOPF",
    "OKOPFRef",
    "OKPD2",
    "OKPD2Ref",
    "OKPD2s",
    "OKPO",
    "OKPORef",
    "OKSMRef",
    "OKTMOCode",
    "OKTMOPPORef",
    "OKTMORef",
    "OKVEDs",
    "SNILS",
    "UBPCode",
    "abandonedReasonRef",
    "accessDBService",
    "account",
    "accounts",
    "accreditationStatus",
    "act",
    "actFinanceInfo",
    "actInfo",
    "actNumber",
    "action",
    "activity",
    "addComplexityText",
    "addInfo",
    "addInfoKTRURef",
    "addInfoText",
    "addRequirement",
    "addRequirementType",
    "addRequirements",
    "additionalInfo",
    "additionalInformation",
    "additionalInformations",
    "address",
    "addressLine",
    "admissionResult",
    "admissionResults",
    "admittedInfo",
    "advance",
    "advanceFinCondition",
    "advanceItem",
    "advancePaymentPayDoc",
    "advancePaymentSum",
    "agreementInfo",
    "agreementNumber",
    "agreementsTotalsInfo",
    "amountInPercents",
    "amountOverpaidInfo",
    "amountOverpaidsInfo",
    "amountRefundInfo",
    "amountRefundsInfo",
    "ancestorListInfo",
    "ancestorsListInfo",
    "answers",
    "appForm",
    "appFormat",
    "appParticipants",
    "appParticipantsInfo",
    "appRejectedReasonType",
    "application",
    "applicationFeaturesCorrespondence",
    "applicationParticipants",
    "applications",
    "approveFor",
    "approveInfo",
    "approveOrderReasonInfo",
    "approvedFrom",
    "athInfo",
    "athsInfo",
    "attachment",
    "attachmentInfo",
    "attachmentListSignCheckUrlType",
    "attachmentListType",
    "attachmentListWithKindType",
    "attachmentType",
    "attachmentWithKindType",
    "attachments",
    "auctionItem",
    "auctionItemsType",
    "auctionProduct",
    "auctionProducts",
    "audit",
    "auditOrg",
    "authenticity",
    "author",
    "authorityName",
    "authorityPrescription",
    "authorizedPersonInfo",
    "auto",
    "autoExDateCalcSign",
    "autoExDateInfo",
    "bankAddress",
    "bankCancelDetails",
    "bankGuarantee",
    "bankGuaranteeRefusalInfo",
    "bankGuaranteeReturn",
    "bankGuaranteeReturnInfo",
    "bankGuaranteeTermination",
    "bankGuaranteeTerminationInfo",
    "bankName",
    "bankSupportContractRequiredInfo2020Type",
    "bankSupportContractRequiredInfoType",
    "bankSupportInfo",
    "bankSupportText",
    "barcode",
    "barcodeNew",
    "base",
    "baseChange",
    "baseDocument",
    "baseExcludedDocInfo",
    "basement",
    "basementInfo",
    "bidType",
    "bidding",
    "budget",
    "budgetFinancing",
    "budgetFinancings",
    "budgetFunds",
    "budgetFundsContractRef",
    "budgetary",
    "budgets",
    "building",
    "businessTripService",
    "cancel",
    "cancelChance",
    "cancelInfo",
    "cancelOrg",
    "cancelProtocol",
    "cancelProtocols",
    "cancelReason",
    "cancelledProcedureId",
    "cashAccount",
    "centralizedPurchaseInfo",
    "certificateInfo",
    "certificateMask",
    "certificateNumber",
    "certificateSN",
    "changePriceFoundationRef",
    "changeType",
    "changes",
    "characteristic",
    "characteristicValues",
    "characteristics",
    "checkInfo",
    "checkList",
    "checkSubjects",
    "checkedOrder",
    "childGroup",
    "childGroupsList",
    "childrenCriteriaType",
    "clarificationRequestType",
    "clarificationType",
    "classifier",
    "classifiers",
    "closedEPCasesRef",
    "code",
    "codePhrase",
    "codesOKTMOPPO",
    "collectedAmountInPercents",
    "collectionStatisticService",
    "comment",
    "commission",
    "commission44",
    "commission94",
    "commissionMember",
    "commissionMemberType",
    "commissionMembers",
    "commissionName",
    "commissionRoleType",
    "commissionType",
    "commonAttributesType",
    "commonInfo",
    "commonUnitsMeasurementsRef",
    "compDocuments",
    "competitiveDocumentProvisioning",
    "complaint",
    "complaintGroupItems",
    "completeness",
    "complexityInfo",
    "concreteValue",
    "condValue",
    "conditionScoring",
    "conditions",
    "conditionsScoring",
    "confirmContactInfo",
    "constructionWorkGroup",
    "constructionWorksInfo",
    "constructor",
    "consumerPackagesQuantity",
    "consumerPackagingInfo",
    "consumerTotal",
    "contactEMail",
    "contactInfo",
    "contactInfoType",
    "contactPersonType",
    "contactPhone",
    "content",
    "contract",
    "contractChange",
    "contractCondition",
    "contractConditionAttributesType",
    "contractConditions",
    "contractExecutionEnsure",
    "contractExecutionPaymentPlan",
    "contractFinCondition",
    "contractInfo",
    "contractInvalidation",
    "contractInvalidationCancel",
    "contractLifeCycleCaseRef",
    "contractLifeCycleCases",
    "contractLifeCycleCasesInfo",
    "contractLifeCycleInfo",
    "contractMaxPrice",
    "contractNotPublished",
    "contractOKEIExtendedRef",
    "contractOKEIRef",
    "contractPrice",
    "contractPrintFormInfo",
    "contractProcedure",
    "contractProcedureInfo",
    "contractProceduresInfo",
    "contractRefusalReasonRef",
    "contractService",
    "contractServiceOfficer",
    "contractSignType",
    "contractType",
    "contractor",
    "contractors",
    "contractsInfo",
    "control99ControlAuthorityInfoType",
    "control99ControlObjectWithMandatoryDocsInfoType",
    "control99CustomerInfoType",
    "control99DocsInfo",
    "control99DocumentObjectType",
    "control99NoticeComplianceWithDocType",
    "control99ResponsibleType",
    "controlDocumentsInfo",
    "controlObjectType",
    "controlObjectsInfo",
    "controlPersonalSignature",
    "controlResult1084point14B",
    "controlResultAgreement",
    "controlResultIKZ",
    "controlResultKBK",
    "controlResultTargetArticle",
    "controlResultsAgreement",
    "controlResultsIKZ",
    "controlResultsKBK",
    "controlResultsTargetArticle",
    "corrAccount",
    "correspondencies",
    "cost",
    "costCriterion",
    "countryCode",
    "countryFullName",
    "countryType",
    "courtDecision",
    "courtDesNumber",
    "courtName",
    "courtsDecision",
    "courtsDecisionOrgName",
    "creationProductDocRequisites",
    "criteria",
    "criterias",
    "criterion",
    "criterionCode",
    "criterionGroup",
    "criterionGroups",
    "criterionRef",
    "criterionScoring",
    "cryptoSigns",
    "currencyCBRFRef",
    "currencyRate",
    "currencyRateType",
    "currencyRef",
    "currencyType",
    "customer",
    "customerInfo",
    "customerLBOInfo",
    "customerLBOsInfo",
    "customerQuantities",
    "customerQuantity",
    "customerRequirement",
    "customerRequirements",
    "customerSignature",
    "customers",
    "damagePayments",
    "data",
    "day",
    "days",
    "decisionInfo",
    "decisionNumber",
    "delayPenalties",
    "delayWriteOffPenalties",
    "deliveredQuantity",
    "deliveryPlace",
    "deliveryProcedure",
    "deliveryTerm",
    "desNumber",
    "descendantInfo",
    "description",
    "deviationFactFoundationRef",
    "digitalCode",
    "direction",
    "discrepanciesText",
    "discussion",
    "discussionResult",
    "docAcceptance",
    "docAcceptancePayDoc",
    "docDescription",
    "docExecution",
    "docInfo",
    "docName",
    "docNumber",
    "docPropertyType",
    "docRejectReasonRef",
    "docReqType",
    "docTermination",
    "docType",
    "docTypeCode",
    "document",
    "documentBase",
    "documentCode",
    "documentCompliance",
    "documentCompliances",
    "documentInfo",
    "documentKindRef",
    "documentList",
    "documentName",
    "documentNum",
    "documentRequirement",
    "documentRequirements",
    "documentType",
    "documentTypes",
    "documentationLots",
    "documents",
    "dosageFactor",
    "dosageFactorRange",
    "dosageFactorRangeMax",
    "dosageFactorRangeMin",
    "dosageFactorRangeStep",
    "dosageFactorRanges",
    "dosageFactorValue",
    "dosageFactors",
    "dosageFormInfo",
    "dosageInfo",
    "dosageUser",
    "dosageValue",
    "dosagesInfo",
    "drugChangeInfoType",
    "drugChangeReasonRef",
    "drugInfo",
    "drugInfoType",
    "drugInfoUsingReferenceInfo",
    "drugInfoUsingTextForm",
    "drugInfoUsingTextFormType",
    "drugInterchangeInfo",
    "drugInterchangeManualInfoType",
    "drugInterchangeReferenceInfoType",
    "drugInterchangeTextFormInfoType",
    "drugPurchaseObjectCustomerInfo",
    "drugPurchaseObjectCustomersInfo",
    "drugPurchaseObjectInfo",
    "drugPurchaseObjectsInfo",
    "drugQuantityCustomerInfo",
    "drugQuantityCustomersInfo",
    "drugSeries",
    "drugsInfo",
    "drugsTypeDetails",
    "editedCertificateNumber",
    "editedDosageInfo",
    "editedManufacturerInfo",
    "editedMedicamentalFormInfo",
    "editedPackagingsInfo",
    "editedTradeInfo",
    "element",
    "elementList",
    "email",
    "endContratProcedureTerm",
    "energyServiceContract",
    "ensuringWay",
    "equivalenceParam",
    "errCode",
    "errorCorrection",
    "errorInfoType",
    "esIssuerDN",
    "esIssuerSN",
    "evalCriterion",
    "evalValue",
    "evaluationResult",
    "evaluationResults",
    "evasDevFactFoundationRef",
    "eventLink",
    "examination",
    "exception",
    "exclude",
    "excludedInfoBase",
    "excludedInfoInfo",
    "exclusionReason615Ref",
    "execObligationsGuaranteeInfo",
    "execution",
    "executionInfo",
    "executionObligationGuarantee",
    "executionPeriod",
    "executions",
    "existInRegulationRules",
    "expensesInfo",
    "expirationDateCustomFormatInfo",
    "expirationDateMonthYear",
    "explanation",
    "export",
    "extCode",
    "extNumber",
    "extPrintFormType",
    "externalPrescription",
    "extraBudgetFundsTotalsInfo",
    "extrabudget",
    "extrabudgetFunds",
    "extrabudgetary",
    "factDates",
    "factualAddress",
    "fax",
    "fcsOrder",
    "features111Info",
    "featuresCorrespondences",
    "federalAuthorityOrder",
    "fileName",
    "fileSize",
    "fileTypeCode",
    "finance111Info",
    "financeInfo",
    "financeResourcesType",
    "financeSource",
    "financeSources",
    "financeSupport",
    "financeSupportPushasesZK",
    "finances",
    "financingSourcesInfo",
    "financings",
    "firstName",
    "firstNameLat",
    "formedBOInfo",
    "foundation",
    "foundationDoc",
    "foundationProtocol",
    "foundationProtocolNumber",
    "foundationRefundDocInfo",
    "foundationRefundDocsInfo",
    "foundations",
    "founders",
    "ftgInfo",
    "fullName",
    "fullName553",
    "fullName554",
    "funcCharacteristics",
    "fundingSources615Ref",
    "generateBOInfo",
    "goodsDelivered",
    "goodsQuantity",
    "group",
    "groupInfo",
    "groupOKEI",
    "groupPrice",
    "groupPriceList",
    "guarantee",
    "guaranteeApp",
    "guaranteeAppType",
    "guaranteeContract",
    "guaranteeContractType",
    "guaranteeEnsure",
    "guaranteeInfo",
    "guaranteePrice",
    "guaranteeReturn",
    "guaranteeTime",
    "guaranteeType",
    "guaranties",
    "guarantor",
    "guideService",
    "hearing",
    "href",
    "hrefType",
    "id",
    "idNumber",
    "idNumberExtension",
    "improperExecution",
    "improperExecutionInfo",
    "inabilityFoundationText",
    "includingExpences",
    "indexNum",
    "indications",
    "indicator",
    "indicatorOffer",
    "indicatorOffers",
    "indicatorScoring",
    "indicators",
    "indicted",
    "individualBusinessman",
    "individualBusinessmanRF",
    "individualPerson",
    "individualPersonForeignState",
    "individualPersonForeignStateInfo",
    "individualPersonForeignStateisCulture",
    "individualPersonRF",
    "individualPersonRFInfo",
    "individualPersonRFisCulture",
    "info",
    "infoProduct",
    "initiativeType",
    "initiatorChange",
    "inn",
    "inputBOFlag",
    "interchangeGroup",
    "interchangeGroupInfo",
    "internalUrl",
    "internationalName",
    "internationalSymbol",
    "invalid",
    "invalidReasonType",
    "invalidationData",
    "invalidationDataListInfo",
    "invalidationReasonDocument",
    "invalidityInfo",
    "jointBidding",
    "jointBiddingInfo",
    "journalNumber",
    "kbk",
    "kladr",
    "kladrCode",
    "kladrPlace",
    "kladrType",
    "ktruCharacteristic",
    "ktruPosition",
    "lastName",
    "lastNameLat",
    "lastOffer",
    "legalActDetails",
    "legalActs",
    "legalEntity",
    "legalEntity307",
    "legalEntity44",
    "legalEntityForeignState",
    "legalEntityForeignStateInfo",
    "legalEntityRF",
    "legalEntityRFInfo",
    "legalFormOld",
    "lifeTime",
    "limPriceInfo",
    "limPricesInfo",
    "loadId",
    "loadUrl",
    "localName",
    "localSymbol",
    "login",
    "lot",
    "lotDocRequirements",
    "lotRefType",
    "lots",
    "maintenanceRepairService",
    "majorRepairEnsure",
    "manual",
    "manualKTRUCharacteristicType",
    "manufacturerInfo",
    "manufacturerOKSMCode",
    "manufacturerReportPrinformInfo",
    "massVolume",
    "max",
    "maxPrice",
    "maxPriceReason",
    "mechanism",
    "medicalProductInfo",
    "medicamentalFormInfo",
    "medicine",
    "methodNotCh1St22",
    "methodPriceFoundationText",
    "methodsFoundation",
    "middleName",
    "middleNameLat",
    "min",
    "minTime",
    "minVolume",
    "missingInRegulationRules",
    "missingIndexNums",
    "modification",
    "modificationInfo",
    "modificationType",
    "modifyContract",
    "modifyTerminateInfo",
    "municipalities",
    "mustExecuteContract",
    "mustSpecifyDrugPackage",
    "name",
    "nationalCode",
    "newRespOrg",
    "noKladrForRegionSettlement",
    "nomBank",
    "nonNormMNNInfo",
    "nonNormMNNsListInfo",
    "nonNormMedFormDosage",
    "nonNormMedFormsDosagesListInfo",
    "nonbudgetFinancing",
    "nonbudgetFinancings",
    "nonregistered",
    "notIncludedReasonsText",
    "notOosFcsOrder",
    "notOosOrder",
    "notRecovery",
    "noticeDetails",
    "noticeNumber",
    "notifRespOrg",
    "notificationCancelFailure",
    "notificationCancelFailureOrg",
    "notificationCancelType",
    "notificationCommission",
    "notificationEFType",
    "notificationFeatureType",
    "notificationFeatures",
    "notificationLots",
    "notificationNumber",
    "notificationOKType",
    "notificationPOType",
    "notificationPlacement",
    "notificationPlacerChangeType",
    "notificationSZType",
    "notificationType",
    "notificationZKType",
    "nsiRejectReason",
    "num",
    "number",
    "object",
    "objectInfoUsingReferenceInfo",
    "objectInfoUsingTextForm",
    "objects",
    "office",
    "ogrn",
    "okopfType",
    "oosOrder",
    "order",
    "orderName",
    "orderNumber",
    "orders",
    "ordinalNumber",
    "orgFactAddress",
    "orgName",
    "orgPostAddress",
    "organizationForeignState",
    "organizationLinks",
    "organizationName",
    "organizationRF",
    "organizationRef",
    "organizationRoleItem",
    "organizationRoles",
    "organizationType",
    "other",
    "otherCases",
    "otherPeriodicityText",
    "outcomeIndicators",
    "overallValue",
    "owner",
    "ownerInfo",
    "p1Place",
    "p2Place",
    "p3Place",
    "packagingInfo",
    "packagingsInfo",
    "paid",
    "paragraphs",
    "paramValue",
    "parentCode",
    "parentContractSubject",
    "parentPositionInfo",
    "parentProtocolNumber",
    "parentRegNumber",
    "part",
    "part10St34Case",
    "participant",
    "participantType",
    "participants",
    "particularsActProcurement",
    "payDoc",
    "payDocToDocAcceptanceCompliances",
    "payDocTypeInfo",
    "payInfo",
    "payment",
    "paymentAmountDetail",
    "paymentCondition",
    "paymentGuaranteeInfoType",
    "paymentPropertysType",
    "payments",
    "penalties",
    "penalty",
    "penaltyAccrual",
    "penaltyChange",
    "penaltyChangeFact",
    "penaltyFact",
    "penaltyReason",
    "penaltyReturn",
    "percentage",
    "period",
    "periodYearFrom",
    "periodYearTo",
    "periodicity",
    "personForeignState",
    "personRF",
    "personType",
    "phase1",
    "phase2",
    "phone",
    "place",
    "placeOfStay",
    "placeOfStayInRF",
    "placeOfStayInRFInfo",
    "placeOfStayInRegCountry",
    "placeOfStayInRegCountryInfo",
    "placementFeature",
    "placementOrgInfo",
    "placementResultType",
    "placer",
    "placerChange",
    "placerInfo",
    "placesOfOrigin",
    "placing",
    "placing44FZ",
    "placing94FZ",
    "placingNotificationTerm",
    "placingWay",
    "placingWayCode",
    "placingWayDocType",
    "placingWayFoundationText",
    "placingWayInfo",
    "placingWayName",
    "placingWayRef",
    "placingWayType",
    "placingWays",
    "planContractMaxPrice",
    "planDescription",
    "planNumber",
    "planPayments",
    "planPeriod",
    "planType",
    "plannedCheck",
    "plannedSurvey",
    "pointLaw",
    "position",
    "positionInfo",
    "positionModification",
    "positionTradeName",
    "positionTradeNameUsingTextForm",
    "positions",
    "positionsTradeName",
    "postAddress",
    "postAddressInfo",
    "postAdressInfo",
    "prefExpl",
    "prefRateRef",
    "prefValue",
    "preferenseType",
    "preferenses",
    "preferensesRequirement",
    "preferensesRequirements",
    "prefsReqsGroup",
    "prefsReqsRef",
    "prescriptionControl",
    "prescriptionInfo",
    "previousRespOrg",
    "price",
    "priceChangeReason",
    "priceInfo",
    "priceOffers",
    "priceRUR",
    "priceType",
    "pricesInfo",
    "pricesZNVLPInfo",
    "primaryPackagingInfo",
    "printFormDocument",
    "printFormDocuments",
    "printFormType",
    "procedure",
    "procedureInfo",
    "procent",
    "processingInfo",
    "product",
    "productName",
    "productRequirement",
    "productType",
    "products",
    "productsAveragePriceInfo",
    "productsChange",
    "productsCountries",
    "productsSpecification",
    "productsSumPaymentsInfo",
    "productsType",
    "prohibitedContent",
    "prohibitedContentOrgName",
    "projectDocumentation",
    "projectInfo",
    "protocolCancelType",
    "protocolCommissionMember",
    "protocolCommissionMembers",
    "protocolEF1Type",
    "protocolEF2Type",
    "protocolEF3Type",
    "protocolEvasionType",
    "protocolLot",
    "protocolLots",
    "protocolNumber",
    "protocolOK1Type",
    "protocolOK2Type",
    "protocolOK3Type",
    "protocolPO1Type",
    "protocolPublisher",
    "protocolType",
    "protocolZK1Type",
    "protocolZK5Type",
    "providedPeriod",
    "providedPurchases",
    "publicDiscussion",
    "publicDiscussion2017",
    "publicDiscussionFacet",
    "publicDiscussionFacets",
    "publicDiscussionInEISInfo",
    "publicDiscussionInfo",
    "publicDiscussionInfoType",
    "publicDiscussionLargePurchasePhase2",
    "publicDiscussionQuestion",
    "publishOrg",
    "publishYear",
    "purchase",
    "purchase83",
    "purchase83st544",
    "purchase93",
    "purchaseAmountLess100",
    "purchaseAmountLess400",
    "purchaseCodes",
    "purchaseConditions",
    "purchaseDrugObjectsInfoType",
    "purchaseFinCondition",
    "purchaseGraph",
    "purchaseInfo",
    "purchaseIsMaxPriceCurrencyType",
    "purchaseObject",
    "purchaseObjectInfo",
    "purchaseObjectSid",
    "purchaseObjects",
    "purchaseObjectsType",
    "purchasePlanFullName",
    "purchasePlanPositionInfo",
    "purchasePlanPositionsInfo",
    "purchasePlanShortName",
    "purchaseProlongation",
    "purchaseRequestEnsure",
    "purchaseResponsible",
    "purchaseResponsibleInfo",
    "purchaseSubjectRef",
    "purchases",
    "purposeInfo",
    "qualifiedContractorRef",
    "qualitativeCriterion",
    "qualityGuaranteeInfo",
    "quantity",
    "quantityContractSubject",
    "quantityContractSubjects",
    "quantityDrugContractSubject",
    "quantityDrugContractSubjects",
    "quantityItem",
    "quantityPurchase",
    "quantityUndefined",
    "question",
    "questionType",
    "questions",
    "rangeSet",
    "rate",
    "rateValue",
    "realization",
    "reason",
    "reasonCode",
    "reasonLaw",
    "recoveryToStage",
    "reestrPrescription",
    "refId",
    "refKTRUCharacteristicType",
    "refundOverpaymentInfo",
    "refundOverpaymentsInfo",
    "refusalFact",
    "refusalFactFoundation",
    "refusalFacts",
    "refusalInfo",
    "refusalReasons",
    "regNum",
    "regNumber",
    "region",
    "regions",
    "registerInRFTaxBodies",
    "registerInRFTaxBodiesInfo",
    "registrationInfo",
    "rejectReasonRef",
    "rejectedApplication",
    "rejectedApplications",
    "reparation",
    "reparations",
    "reparationsDocuments",
    "reportCode",
    "reqNumber",
    "reqValue",
    "request",
    "requestNumber",
    "requestRegNumber",
    "requirement",
    "requirement2020Type",
    "requirement2020WithAddReqsType",
    "requirementCompliance",
    "requirementCompliances",
    "requirementFoundationText",
    "requirementRestrictionType",
    "requirementType",
    "requirementWithAddReqsType",
    "requirements",
    "requirementsFoundation",
    "requirementsType",
    "responsibleContactInfo",
    "responsibleDecision",
    "responsibleInfo",
    "responsibleRole",
    "restrictionSt14",
    "restrictionSt14Type",
    "restrictionType",
    "restrictions",
    "restructure",
    "resultType",
    "returnedAmountInPercents",
    "righSideKTRURef",
    "rightSideKTRUCharacteristicType",
    "rightSideKTRUInfo",
    "rightToConcludeContractPriceInfo",
    "role",
    "rubricatorInfo",
    "rubricators",
    "sIdInfo",
    "schemeVersion",
    "scoring",
    "section",
    "sellProductDocRequisites",
    "serviceWorkSt166Ref",
    "settlement",
    "settlementType",
    "shortName",
    "shortName553",
    "shortName554",
    "shortStreet",
    "sid",
    "signature",
    "signatureType",
    "signer",
    "singleCustomer",
    "singleCustomerContractApproval",
    "singleCustomerPurchase",
    "singleCustomerReason",
    "singularName",
    "sketchPlan",
    "sources",
    "specialPurchase",
    "specialPurchaseModification",
    "specialPurchases",
    "st14Info",
    "stage",
    "stageAdvancePaymentSum",
    "stageOne",
    "stageTwo",
    "stages",
    "standardContract",
    "standardContracts",
    "standarts",
    "state",
    "statement",
    "status",
    "subContractNumber",
    "subContractPriceInfo",
    "subContractor",
    "subContractors",
    "subContractorsSum",
    "subPurchaseObjectsInfo",
    "subject",
    "subjectComplaint",
    "subjectComplaintGroup",
    "subjectType",
    "subjects",
    "subsection",
    "substitutedOrder",
    "success",
    "sumInPercents",
    "supplier",
    "supplierInfo",
    "supplierSignature",
    "supplierType",
    "suppliers",
    "targetArticleFinancingType",
    "targetArticleFinancingsType",
    "taxPayerCode",
    "teachingService",
    "templateKTRUs",
    "tendePlanInfoType",
    "tender",
    "tenderPlan",
    "tenderPlan2017FullName",
    "tenderPlan2017ShortName",
    "tenderPlan2020Info",
    "tenderPlan2020InfoType",
    "tenderPlan2020KVRRefType",
    "tenderPlan2020OKPD2RefType",
    "tenderPlanInfo",
    "tenderPlanPurchaseGroups",
    "tenders",
    "tendersInfo",
    "term",
    "terminateContract",
    "termination",
    "terminationGround615Ref",
    "terminationReason",
    "terminationReason615Ref",
    "terminations",
    "timeEFType",
    "timeRange",
    "timeRanges",
    "timeZoneOlson",
    "timeZoneUtcOffset",
    "topic",
    "total",
    "tradeInfo",
    "tradeInfoType",
    "tradeMark",
    "tradeName",
    "treasurySupportContractInfo",
    "typeCode",
    "typeCodes",
    "typeRMIS",
    "type_",
    "undefined",
    "unfairSupplier",
    "unfairSupplierApproval",
    "unplannedCheck",
    "unplannedCheckComplaint",
    "unplannedEventType",
    "unplannedSurvey",
    "url",
    "usageMax",
    "usageMin",
    "useCases",
    "usedInRPGInfo",
    "user",
    "usingRGKInfo",
    "usingTextForm",
    "value",
    "valueRange",
    "valueSet",
    "values",
    "violationInfo",
    "violationType",
    "violations",
    "voucherEntry",
    "waiverNotice",
    "warnings",
    "winner",
    "winners",
    "writeOffPenalties",
    "www",
    "year",
    "yearPlan",
    "yearsList",
    "zfcs_ETPType",
    "zfcs_KTRUCharacteristicType",
    "zfcs_KTRUCharacteristicValueType",
    "zfcs_KTRUClassifierType",
    "zfcs_KTRUIndustryClassifierNodeType",
    "zfcs_KTRUIndustryClassifierType",
    "zfcs_KTRUPositionType",
    "zfcs_KTRUPositionsType",
    "zfcs_KTRURef",
    "zfcs_KTRUSignType",
    "zfcs_KTRUStandartType",
    "zfcs_KVRRef",
    "zfcs_LBOType",
    "zfcs_MNNInfoType",
    "zfcs_OKATORef",
    "zfcs_OKEIRef",
    "zfcs_OKFSRef",
    "zfcs_OKPD2Ref",
    "zfcs_OKPDRef",
    "zfcs_OKPORef",
    "zfcs_OKSMRef",
    "zfcs_OKTMOPPORef",
    "zfcs_OKTMORef",
    "zfcs_OKVEDRef",
    "zfcs_PositionKBK2016sYearsType",
    "zfcs_PositionKBKsYearsType",
    "zfcs_PositionKOSGUsYearsType",
    "zfcs_PositionKVRsYearsType",
    "zfcs_TOFKRef",
    "zfcs_abandonedReasonType",
    "zfcs_accountType",
    "zfcs_accreditedEPSupplierType",
    "zfcs_accreditedEPSupplier_attachmentListType",
    "zfcs_accreditedEPSupplier_attachmentType",
    "zfcs_addInfoInvalidType",
    "zfcs_addInfoType",
    "zfcs_admissionResults",
    "zfcs_appRejectedReasonNotIDType",
    "zfcs_appRejectedReasonType",
    "zfcs_appealDetailsType",
    "zfcs_applicantNewType",
    "zfcs_applicantType",
    "zfcs_applicationAdmittedInfoType",
    "zfcs_applicationCorrespondence",
    "zfcs_attachmentListType",
    "zfcs_attachmentType",
    "zfcs_auditActionSubjectsRef",
    "zfcs_auditResultType",
    "zfcs_bankGuaranteeInfoType",
    "zfcs_bankGuaranteeInvalidType",
    "zfcs_bankGuaranteeOrganizationType",
    "zfcs_bankGuaranteeOtherBankNoticeType",
    "zfcs_bankGuaranteeParticipantType",
    "zfcs_bankGuaranteeRef615ReasonType",
    "zfcs_bankGuaranteeRefReasonType",
    "zfcs_bankGuaranteeRefusalInvalidType",
    "zfcs_bankGuaranteeRefusalType",
    "zfcs_bankGuaranteeReturnInfoType",
    "zfcs_bankGuaranteeReturnInvalidType",
    "zfcs_bankGuaranteeReturnType",
    "zfcs_bankGuaranteeTerminationInvalidType",
    "zfcs_bankGuaranteeTerminationType",
    "zfcs_bankGuaranteeType",
    "zfcs_baseRef",
    "zfcs_bidType",
    "zfcs_bigProjectCostType",
    "zfcs_bigProjectFinancingYearsType",
    "zfcs_bigProjectFinancingsType",
    "zfcs_bigProjectMemberType",
    "zfcs_bigProjectValueType",
    "zfcs_budgetFinancingsType",
    "zfcs_budgetFundsContract2015",
    "zfcs_checkPlanCheckInfoType",
    "zfcs_checkPlanCommonInfoPrintFormType",
    "zfcs_checkPlanCommonInfoType",
    "zfcs_checkPlanType",
    "zfcs_checkResultActType",
    "zfcs_checkResultCancelCommonInfoType",
    "zfcs_checkResultCancelType",
    "zfcs_checkResultCommonInfoPrintFormType",
    "zfcs_checkResultCommonInfoType",
    "zfcs_checkResultComplaintType",
    "zfcs_checkResultDecisionType",
    "zfcs_checkResultPlannedCheckType",
    "zfcs_checkResultPrescriptionType",
    "zfcs_checkResultType",
    "zfcs_checkResultUnplannedCheckComplaintType",
    "zfcs_checkResultUnplannedCheckType",
    "zfcs_checkSubjectPlanType",
    "zfcs_clarificationProcedureInfoType",
    "zfcs_clarificationRequestType",
    "zfcs_clarificationType",
    "zfcs_closedMethodsOfReasonRef",
    "zfcs_commissionMemberInAppType",
    "zfcs_commissionMemberType",
    "zfcs_commissionRoleType",
    "zfcs_commissionType",
    "zfcs_commonUnitsMeasurementsType",
    "zfcs_complaintCancelInfoType",
    "zfcs_complaintCancelPrintFormType",
    "zfcs_complaintCancelType",
    "zfcs_complaintCommonInfoPrintFormType",
    "zfcs_complaintCommonInfoType",
    "zfcs_complaintGroupType",
    "zfcs_complaintModificationType",
    "zfcs_complaintObjectType",
    "zfcs_complaintOrderType",
    "zfcs_complaintProjectSubjectType",
    "zfcs_complaintPurchaseType",
    "zfcs_complaintReturnInfoType",
    "zfcs_complaintSubjectType",
    "zfcs_complaintType",
    "zfcs_confirmationType",
    "zfcs_contactInfoType",
    "zfcs_contactPersonType",
    "zfcs_contract2015BankGuaranteeReturnType",
    "zfcs_contract2015DrugPurchaseInfoType",
    "zfcs_contract2015EnforcementType",
    "zfcs_contract2015PriceInfoType",
    "zfcs_contract2015PurchaseObjectInfoType",
    "zfcs_contract2015SingleCustomerType",
    "zfcs_contract2015SubContractInfoType",
    "zfcs_contract2015SupplierType",
    "zfcs_contract2015TenderPlanInfoType",
    "zfcs_contract2015Type",
    "zfcs_contract2015_DocDictRef",
    "zfcs_contract2015_documentInfo",
    "zfcs_contract2015_payDocInfo",
    "zfcs_contractAvailableForElAct",
    "zfcs_contractCancel2015Type",
    "zfcs_contractCancelType",
    "zfcs_contractExecutionType",
    "zfcs_contractGuaranteePaymentInfoType",
    "zfcs_contractMultiType",
    "zfcs_contractProcedure2015BankGuaranteePaymentType",
    "zfcs_contractProcedure2015BankGuaranteeTerminationType",
    "zfcs_contractProcedure2015HoldCashEnforcementType",
    "zfcs_contractProcedure2015ProductsCountryType",
    "zfcs_contractProcedure2015SearchDrugProductsAttrsType",
    "zfcs_contractProcedure2015SearchProductsAttrsType",
    "zfcs_contractProcedure2015Type",
    "zfcs_contractProcedureCancel2015Type",
    "zfcs_contractProcedureCancelType",
    "zfcs_contractProcedureType",
    "zfcs_contractSignType",
    "zfcs_contractTerminationReasonType",
    "zfcs_contractType",
    "zfcs_contract_OKEIType",
    "zfcs_contract_attachmentListType",
    "zfcs_contract_attachmentType",
    "zfcs_contract_printFormType",
    "zfcs_control99BeginMessageType",
    "zfcs_control99ConfirmType",
    "zfcs_control99ConfirmationType",
    "zfcs_control99ContractAttachmentListType",
    "zfcs_control99ContractExtractType",
    "zfcs_control99ControlAuthorityInfoType",
    "zfcs_control99ControlObjectType",
    "zfcs_control99ControlObjectWithMandatoryDocsInfoType",
    "zfcs_control99ControlResultType",
    "zfcs_control99ControlResultsIKZType",
    "zfcs_control99CustomerInfoType",
    "zfcs_control99DocLinkType",
    "zfcs_control99DocumentObjectType",
    "zfcs_control99ExtPrintFormType",
    "zfcs_control99NoticeComplianceType",
    "zfcs_control99NoticeComplianceWithDocType",
    "zfcs_control99NoticeProtocolCommonInfoType",
    "zfcs_control99NotificationExtractType",
    "zfcs_control99OwnerInfoType",
    "zfcs_control99ProtocolCommonInfoType",
    "zfcs_control99ProtocolExtractType",
    "zfcs_control99ProtocolMismatchReductFundsType",
    "zfcs_control99ProtocolMismatchType",
    "zfcs_control99PurchasePlanExtractType",
    "zfcs_control99PurchasePlanPositionType",
    "zfcs_control99RefusalMessageType",
    "zfcs_control99ResponsibleType",
    "zfcs_control99TenderPlan2017ExtractType",
    "zfcs_control99TenderPlan2017PositionType",
    "zfcs_control99TenderPlan2017SpecialPurchaseType",
    "zfcs_controlRegistersAttachmentListType",
    "zfcs_controlRegistersAttachmentType",
    "zfcs_countryRef",
    "zfcs_criterionType",
    "zfcs_currencyFullRef",
    "zfcs_currencyRateContract2015",
    "zfcs_currencyRef",
    "zfcs_customerReportBaseType",
    "zfcs_customerReportBigProjectMonitoringInvalidType",
    "zfcs_customerReportBigProjectMonitoringType",
    "zfcs_customerReportContractExecutionInvalidType",
    "zfcs_customerReportContractExecutionType",
    "zfcs_customerReportInvalidType",
    "zfcs_customerReportSingleContractorInvalidType",
    "zfcs_customerReportSingleContractorType",
    "zfcs_customerReportSmallScaleBusinessInvalidType",
    "zfcs_customerReportSmallScaleBusinessType",
    "zfcs_customerReportType",
    "zfcs_decisionDetailsType",
    "zfcs_decisionRef",
    "zfcs_deviationFactFoundation",
    "zfcs_docCancelReasonType",
    "zfcs_docType",
    "zfcs_documentRequirementType",
    "zfcs_documentationEAType",
    "zfcs_drugInfoType",
    "zfcs_drugInfoUsingTextFormType",
    "zfcs_edoNsiOperatorInfoType",
    "zfcs_electronicComplaintType",
    "zfcs_eruzNsiContractorExcludeReasonType",
    "zfcs_eruzNsiContractorUserRightType",
    "zfcs_etpActionRefType",
    "zfcs_etpPrivilege",
    "zfcs_eventPlanProjectType",
    "zfcs_eventPlanSuspensionType",
    "zfcs_eventPlanType",
    "zfcs_eventResultCancelProjectType",
    "zfcs_eventResultCancelType",
    "zfcs_eventResultPlannedCheckType",
    "zfcs_eventResultPrescriptionType",
    "zfcs_eventResultProjectType",
    "zfcs_eventResultType",
    "zfcs_eventResultUnplannedCheckType",
    "zfcs_extPrintFormType",
    "zfcs_extraBudgetFundsContract2015",
    "zfcs_foundationProtocolInfoType",
    "zfcs_guaranteeType",
    "zfcs_guarantee_attachmentListType",
    "zfcs_guarantee_attachmentType",
    "zfcs_improperContractExecutionType",
    "zfcs_indicatorType",
    "zfcs_infoProtocolZKBIType",
    "zfcs_invalidReportType",
    "zfcs_kladrPlacesType",
    "zfcs_kladrType",
    "zfcs_linkUser",
    "zfcs_lotI111Type",
    "zfcs_lotISType",
    "zfcs_lotInfoType",
    "zfcs_lotOKType",
    "zfcs_lotZKType",
    "zfcs_manufacturerReportCancelType",
    "zfcs_manufacturerReportNPAType",
    "zfcs_manufacturerReportOrganizationType",
    "zfcs_manufacturerReportProductType",
    "zfcs_manufacturerReportProductsType",
    "zfcs_manufacturerReportSupplerInfoType",
    "zfcs_manufacturerReportType",
    "zfcs_masterDataType",
    "zfcs_modifyTerminateContractType",
    "zfcs_nonbudgetFinancingsType",
    "zfcs_noticeDetailsType",
    "zfcs_notificationCancelFailureType",
    "zfcs_notificationCancelType",
    "zfcs_notificationEFDateChangeType",
    "zfcs_notificationEFType",
    "zfcs_notificationEPType",
    "zfcs_notificationExceptionOrgType",
    "zfcs_notificationExceptionType",
    "zfcs_notificationI111Type",
    "zfcs_notificationISMType",
    "zfcs_notificationISOType",
    "zfcs_notificationLotCancelType",
    "zfcs_notificationLotChangeType",
    "zfcs_notificationModification111Type",
    "zfcs_notificationModificationType",
    "zfcs_notificationOKDType",
    "zfcs_notificationOKOUType",
    "zfcs_notificationOKType",
    "zfcs_notificationOrgChangeType",
    "zfcs_notificationPOType",
    "zfcs_notificationRemoveDocType",
    "zfcs_notificationZKType",
    "zfcs_notificationZPType",
    "zfcs_notificationZakAType",
    "zfcs_notificationZakKDType",
    "zfcs_notificationZakKOUType",
    "zfcs_notificationZakKType",
    "zfcs_nsiAbandonedReasonType",
    "zfcs_nsiAuditActionSubjectsType",
    "zfcs_nsiBankGuaranteeRefusal615ReasonType",
    "zfcs_nsiBankGuaranteeRefusalReasonType",
    "zfcs_nsiBudgetType",
    "zfcs_nsiBusinessControlType",
    "zfcs_nsiBusinessControlsType",
    "zfcs_nsiCalendarDaysType",
    "zfcs_nsiChangePriceFoundationType",
    "zfcs_nsiClosedEPCasesType",
    "zfcs_nsiClosedMethodsOfReason",
    "zfcs_nsiCommissionRoleType",
    "zfcs_nsiCommissionType",
    "zfcs_nsiContractCurrencyCBRFType",
    "zfcs_nsiContractExecutionDocType",
    "zfcs_nsiContractModificationReasonType",
    "zfcs_nsiContractOKOPFExtraBudgetType",
    "zfcs_nsiContractPenaltyReasonType",
    "zfcs_nsiContractPriceChangeReasonType",
    "zfcs_nsiContractRefusalReasonType",
    "zfcs_nsiContractReparationDocType",
    "zfcs_nsiContractSingleCustomerReasonType",
    "zfcs_nsiContractTerminationReasonType",
    "zfcs_nsiControl99SubjectOrgType",
    "zfcs_nsiControl99SubjectType",
    "zfcs_nsiCurrencyType",
    "zfcs_nsiDeviationFactFoundationType",
    "zfcs_nsiDocRejectReasonType",
    "zfcs_nsiDrugChangeReason",
    "zfcs_nsiDrugOKEIType",
    "zfcs_nsiEADocType",
    "zfcs_nsiEAESCountry",
    "zfcs_nsiEPDocType",
    "zfcs_nsiETPType",
    "zfcs_nsiEtpActionType",
    "zfcs_nsiEvalCriterionType",
    "zfcs_nsiEvasDevFactFoundationType",
    "zfcs_nsiFarmDrugDictionary",
    "zfcs_nsiFarmDrugDosageInfoType",
    "zfcs_nsiFarmDrugInterchangeGroup",
    "zfcs_nsiFarmDrugInterchangeGroupInfo",
    "zfcs_nsiGroupBuildType",
    "zfcs_nsiKBKBudgetType",
    "zfcs_nsiKOSGUType",
    "zfcs_nsiKTRUNotUsingReasonType",
    "zfcs_nsiKTRUType",
    "zfcs_nsiKVRType",
    "zfcs_nsiModifyReasonOZType",
    "zfcs_nsiNationalProject",
    "zfcs_nsiOKEIType",
    "zfcs_nsiOKFSType",
    "zfcs_nsiOKOPFType",
    "zfcs_nsiOKPD2Type",
    "zfcs_nsiOKPDType",
    "zfcs_nsiOKSMType",
    "zfcs_nsiOKTMOPPOType",
    "zfcs_nsiOKTMOType",
    "zfcs_nsiOKVED2Type",
    "zfcs_nsiOKVEDType",
    "zfcs_nsiOffBudgetType",
    "zfcs_nsiOrganizationRightsType",
    "zfcs_nsiOrganizationType",
    "zfcs_nsiOrganizationTypesType",
    "zfcs_nsiPlacingWayType",
    "zfcs_nsiPlanPositionChangeReasonType",
    "zfcs_nsiPrefRateType",
    "zfcs_nsiPublicDiscussionDecisionsType",
    "zfcs_nsiPublicDiscussionQuestionnarieType",
    "zfcs_nsiPurchaseDocumentTypesType",
    "zfcs_nsiPurchasePlanPositionChangeReasonType",
    "zfcs_nsiPurchasePreferencesType",
    "zfcs_nsiPurchaseRejectReasonType",
    "zfcs_nsiRMISType",
    "zfcs_nsiRightSideKTRUType",
    "zfcs_nsiSingleCustomerReasonOZType",
    "zfcs_nsiSpecialPurchase2020Type",
    "zfcs_nsiSpecialPurchaseType",
    "zfcs_nsiTRUAdmissionNPA",
    "zfcs_nsiTenderPlan2017ContractLifeCycleCaseType",
    "zfcs_nsiTenderPlan2017PositionChangeReasonType",
    "zfcs_nsiTenderPlan2020PositionChangeReasonType",
    "zfcs_nsiTenderPlanPurchaseGroupType",
    "zfcs_nsiUserType",
    "zfcs_nsiWorldTimeZoneType",
    "zfcs_okopfRef",
    "zfcs_orderDetailsType",
    "zfcs_organizationBudgetsType",
    "zfcs_organizationControlRegistersRef",
    "zfcs_organizationInfoExtendedType",
    "zfcs_organizationInfoForZCType",
    "zfcs_organizationInfoType",
    "zfcs_organizationInfoWithOgrnType",
    "zfcs_organizationLink",
    "zfcs_organizationRef",
    "zfcs_participantType",
    "zfcs_paymentInfoType",
    "zfcs_penalty_documentInfoList",
    "zfcs_periodType",
    "zfcs_placementResultType",
    "zfcs_placingWayType",
    "zfcs_planPositionChangeReasonRef",
    "zfcs_preferenseType",
    "zfcs_printFormType",
    "zfcs_projectIncomingConfirmationType",
    "zfcs_protocolCancelReasonType",
    "zfcs_protocolCancelType",
    "zfcs_protocolDeviationType",
    "zfcs_protocolEF1Type",
    "zfcs_protocolEF2Type",
    "zfcs_protocolEF3Type",
    "zfcs_protocolEFInvalidationType",
    "zfcs_protocolEFSingleAppType",
    "zfcs_protocolEFSinglePartType",
    "zfcs_protocolEvasionType",
    "zfcs_protocolModificationReasonType",
    "zfcs_protocolModificationType",
    "zfcs_protocolOK1Type",
    "zfcs_protocolOK2Type",
    "zfcs_protocolOKD1Type",
    "zfcs_protocolOKD2Type",
    "zfcs_protocolOKD3Type",
    "zfcs_protocolOKD4Type",
    "zfcs_protocolOKD5Type",
    "zfcs_protocolOKDSingleAppType",
    "zfcs_protocolOKOU1Type",
    "zfcs_protocolOKOU2Type",
    "zfcs_protocolOKOU3Type",
    "zfcs_protocolOKOUSingleAppType",
    "zfcs_protocolOKSingleAppType",
    "zfcs_protocolPOType",
    "zfcs_protocolZKAfterProlongType",
    "zfcs_protocolZKBIAfterProlongType",
    "zfcs_protocolZKBIType",
    "zfcs_protocolZKType",
    "zfcs_protocolZPExtractType",
    "zfcs_protocolZPFinalType",
    "zfcs_protocolZPType",
    "zfcs_publicDiscussionAnswerType",
    "zfcs_publicDiscussionAuthorType",
    "zfcs_publicDiscussionCommentType",
    "zfcs_publicDiscussionCommonInfo2016Type",
    "zfcs_publicDiscussionCommonInfoType",
    "zfcs_publicDiscussionDecisionRef",
    "zfcs_publicDiscussionFacetRef",
    "zfcs_publicDiscussionFormType",
    "zfcs_publicDiscussionFoundationRef",
    "zfcs_publicDiscussionLargePurchase2016Type",
    "zfcs_publicDiscussionLargePurchasePhase1Type",
    "zfcs_publicDiscussionLargePurchasePhase2Type",
    "zfcs_publicDiscussionPhase1SuspensionType",
    "zfcs_publicDiscussionPhase1Type",
    "zfcs_publicDiscussionPhase2SuspensionType",
    "zfcs_publicDiscussionPhase2Type",
    "zfcs_publicDiscussionPhases2016Type",
    "zfcs_publicDiscussionProtocol2016Type",
    "zfcs_publicDiscussionProtocolType",
    "zfcs_publicDiscussionPurchaseAddInfo2016Type",
    "zfcs_publicDiscussionPurchasePlanAddInfoType",
    "zfcs_publicDiscussionQuestionRef",
    "zfcs_publicDiscussionSuspension2016Type",
    "zfcs_publicDiscussionType",
    "zfcs_purchaseApprovalType",
    "zfcs_purchaseBOBudgetFinancingType",
    "zfcs_purchaseBOBudgetFinancingsType",
    "zfcs_purchaseBOInfoType",
    "zfcs_purchaseCancelReasonType",
    "zfcs_purchaseChangeType",
    "zfcs_purchaseDocumentCancelType",
    "zfcs_purchaseDocumentCommonType",
    "zfcs_purchaseDocumentType",
    "zfcs_purchaseDrugPurchaseObjectsInfoType",
    "zfcs_purchaseNotification111Type",
    "zfcs_purchaseNotificationISType",
    "zfcs_purchaseNotificationType",
    "zfcs_purchaseOrganizationType",
    "zfcs_purchasePlanAddInfoType",
    "zfcs_purchasePlanAgreementTotalsInfoType",
    "zfcs_purchasePlanChangeType",
    "zfcs_purchasePlanCommonInfoType",
    "zfcs_purchasePlanExecutionType",
    "zfcs_purchasePlanFinanceResourcesType",
    "zfcs_purchasePlanKBKsInfoType",
    "zfcs_purchasePlanKBKsTotalsInfoType",
    "zfcs_purchasePlanKVRRefType",
    "zfcs_purchasePlanLegalActsType",
    "zfcs_purchasePlanOKPD2RefType",
    "zfcs_purchasePlanOrganizationType",
    "zfcs_purchasePlanPeriodicityType",
    "zfcs_purchasePlanPositionChangeReasonRef",
    "zfcs_purchasePlanPositionDecisionType",
    "zfcs_purchasePlanPositionType",
    "zfcs_purchasePlanPurchasesSubsecYearsInfoType",
    "zfcs_purchasePlanSpecialPurchaseRef",
    "zfcs_purchasePlanSpecialPurchaseType",
    "zfcs_purchasePlanType",
    "zfcs_purchaseProcedureBiddingType",
    "zfcs_purchaseProcedureCollectingType",
    "zfcs_purchaseProcedureCollectingWithFormType",
    "zfcs_purchaseProcedureContractingType",
    "zfcs_purchaseProcedureOKDType",
    "zfcs_purchaseProcedureOKOUType",
    "zfcs_purchaseProcedureOKType",
    "zfcs_purchaseProcedureOpeningType",
    "zfcs_purchaseProcedurePrequalificationType",
    "zfcs_purchaseProcedureScoringPlaceType",
    "zfcs_purchaseProcedureScoringType",
    "zfcs_purchaseProcedureSelectingType",
    "zfcs_purchaseProcedureZakAType",
    "zfcs_purchaseProlongationCommonType",
    "zfcs_purchaseProlongationOKType",
    "zfcs_purchaseProlongationZKType",
    "zfcs_purchaseProtocolEFNoCommissionType",
    "zfcs_purchaseProtocolEFType",
    "zfcs_purchaseProtocolType",
    "zfcs_quickRefOrganizationType",
    "zfcs_refusalFact",
    "zfcs_refusalFactFoundation",
    "zfcs_regulationRulesInvalidType",
    "zfcs_regulationRulesType",
    "zfcs_releasePurchaseDocumentationType",
    "zfcs_repAutoNotPassProtocolType",
    "zfcs_repAutoTestNoticeType",
    "zfcs_repCommonInfo",
    "zfcs_repContractChangeInfo",
    "zfcs_repContractInfo",
    "zfcs_repContractTerminationInfo",
    "zfcs_repDates",
    "zfcs_repModificationInfo",
    "zfcs_repNPA",
    "zfcs_repOnlySupplierType",
    "zfcs_repPlacerOrgType",
    "zfcs_repProductType",
    "zfcs_repProductsType",
    "zfcs_repSimpleOrganizationInfo",
    "zfcs_repSupplierInfo",
    "zfcs_requestForQuotationCancelType",
    "zfcs_requestForQuotationType",
    "zfcs_requirementType",
    "zfcs_requirementWithAddReqsType",
    "zfcs_restrictionType",
    "zfcs_rightSideKTRUCharacteristicType",
    "zfcs_rightSideKTRUPositionType",
    "zfcs_secondPartAppOpeningType",
    "zfcs_signIncomingConfirmationType",
    "zfcs_signIncomingReqConfirmationType",
    "zfcs_sketchPlanExecutionType",
    "zfcs_sketchPlanType",
    "zfcs_sourceUnplannedCheckType",
    "zfcs_stageType",
    "zfcs_standardContractInvalidType",
    "zfcs_standardContractPurchaseObjectType",
    "zfcs_standardContractType",
    "zfcs_subStageType",
    "zfcs_subjectRFRef",
    "zfcs_tendePlanInfoType",
    "zfcs_tenderPlan2017CommonInfoType",
    "zfcs_tenderPlan2017ContractLifeCycleCaseRef",
    "zfcs_tenderPlan2017DrugNumberType",
    "zfcs_tenderPlan2017DrugPurchaseObjectsInfoType",
    "zfcs_tenderPlan2017FinalPositionsPPRF73Type",
    "zfcs_tenderPlan2017FinalPositionsType",
    "zfcs_tenderPlan2017FinanceResourcesType",
    "zfcs_tenderPlan2017KBKsInfoType",
    "zfcs_tenderPlan2017ManualKtruCharacteristicType",
    "zfcs_tenderPlan2017MethodPriceFoundationType",
    "zfcs_tenderPlan2017NumberType",
    "zfcs_tenderPlan2017PositionChangeReasonRef",
    "zfcs_tenderPlan2017PositionDecisionType",
    "zfcs_tenderPlan2017PositionType",
    "zfcs_tenderPlan2017PrefsReqsFoundationType",
    "zfcs_tenderPlan2017PrefsReqsType",
    "zfcs_tenderPlan2017ProductType",
    "zfcs_tenderPlan2017PurchasePlanPositionRefType",
    "zfcs_tenderPlan2017RefKtruCharacteristicType",
    "zfcs_tenderPlan2017SpecialPurchaseType",
    "zfcs_tenderPlan2017Type",
    "zfcs_tenderPlanCancelType",
    "zfcs_tenderPlanChange2017Type",
    "zfcs_tenderPlanChangeIDType",
    "zfcs_tenderPlanChangeType",
    "zfcs_tenderPlanCommonInfoType",
    "zfcs_tenderPlanFinalPositionsType",
    "zfcs_tenderPlanIDType",
    "zfcs_tenderPlanPositionKBK2016sType",
    "zfcs_tenderPlanPositionKBKsType",
    "zfcs_tenderPlanPositionKOSGUsType",
    "zfcs_tenderPlanPositionKVRsType",
    "zfcs_tenderPlanPositionType",
    "zfcs_tenderPlanTotalPositionKBK2016sType",
    "zfcs_tenderPlanTotalPositionKBKsType",
    "zfcs_tenderPlanTotalPositionKOSGUsType",
    "zfcs_tenderPlanTotalPositionKVRsType",
    "zfcs_tenderPlanType",
    "zfcs_tenderPlanUnstructuredType",
    "zfcs_tenderPlan_ContextType",
    "zfcs_tenderSuspensionType",
    "zfcs_tenderplan2017PurchaseFailedConsequenceType",
    "zfcs_timeEFType",
    "zfcs_timelineViolationType",
    "zfcs_tradeInfoType",
    "zfcs_unfairSupplierType",
    "zfcs_unplannedCheckBaseType",
    "zfcs_unplannedCheckCancelType",
    "zfcs_unplannedCheckCheckedObjectType",
    "zfcs_unplannedCheckCommonInfoPrintFormType",
    "zfcs_unplannedCheckCommonInfoType",
    "zfcs_unplannedCheckObjectType",
    "zfcs_unplannedCheckSubjectPlanType",
    "zfcs_unplannedCheckTenderSuspType",
    "zfcs_unplannedCheckType",
    "zfcs_unplannedEventBaseType",
    "zfcs_unplannedEventCancelProjectType",
    "zfcs_unplannedEventCancelType",
    "zfcs_unplannedEventEventLinkType",
    "zfcs_unplannedEventProjectType",
    "zfcs_unplannedEventSuspensionType",
    "zfcs_unplannedEventType",
    "zfcs_userTenderPlanType",
    "zfcs_violationType",
    "zip"
]