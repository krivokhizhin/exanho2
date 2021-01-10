#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sun Jan 10 17:22:35 2021 by generateDS.py version 2.37.11.
# Python 3.8.2 (default, Apr 12 2020, 19:32:31)  [GCC 8.3.0]
#
# Command line options:
#   ('-f', '')
#   ('--one-file-per-xsd', '')
#   ('--output-directory', '/home/kks/git/exanho/exanho/eis44/ds/contracts')
#   ('--use-source-file-as-module-name', '')
#   ('--use-getter-setter', 'none')
#   ('--enable-slots', '')
#   ('--member-specs', 'dict')
#   ('--export', '')
#   ('--silence', '')
#
# Command line arguments:
#   /home/kks/git/exanho/exanho/eis44/ds/contracts/xsd/fcsExport.xsd
#
# Command line:
#   /home/kks/git/exanho/venv/bin/generateDS.py -f --one-file-per-xsd --output-directory="/home/kks/git/exanho/exanho/eis44/ds/contracts" --use-source-file-as-module-name --use-getter-setter="none" --enable-slots --member-specs="dict" --export --silence /home/kks/git/exanho/exanho/eis44/ds/contracts/xsd/fcsExport.xsd
#
# Current working directory (os.getcwd()):
#   exanho
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
    from ..generatedssuper import GeneratedsSuper
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


class abandonedReasonRef(GeneratedsSuper):
    """Ссылка на справочник Основания признания торгов несостоявшимися"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['abandonedReasonCode', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['abandonedReasonName', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_abandonedReasonCode(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_abandonedReasonName(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, abandonedReasonRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if abandonedReasonRef.subclass:
            return abandonedReasonRef.subclass(*args_, **kwargs_)
        else:
            return abandonedReasonRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_abandonedReasonCode(self, value):
        result = True
        # Validate type abandonedReasonCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on abandonedReasonCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on abandonedReasonCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_abandonedReasonName(self, value):
        result = True
        # Validate type abandonedReasonName, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on abandonedReasonName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on abandonedReasonName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type abandonedReasonCode
            self.validate_abandonedReasonCode(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type abandonedReasonName
            self.validate_abandonedReasonName(self.name)
# end class abandonedReasonRef


class budgetFundsContractRef(GeneratedsSuper):
    """Ссылка на Код и наименование бюджета в контракте"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['budgetCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_budgetCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, budgetFundsContractRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if budgetFundsContractRef.subclass:
            return budgetFundsContractRef.subclass(*args_, **kwargs_)
        else:
            return budgetFundsContractRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_budgetCodeType(self, value):
        result = True
        # Validate type budgetCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on budgetCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on budgetCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type budgetCodeType
            self.validate_budgetCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class budgetFundsContractRef


class contractRefusalReasonRef(GeneratedsSuper):
    """Ссылка на справочник Основания для отказа от заключения контракта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['contractRefusalReasonCodeType', 'text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text500Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_contractRefusalReasonCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text500Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contractRefusalReasonRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contractRefusalReasonRef.subclass:
            return contractRefusalReasonRef.subclass(*args_, **kwargs_)
        else:
            return contractRefusalReasonRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_contractRefusalReasonCodeType(self, value):
        result = True
        # Validate type contractRefusalReasonCodeType, a restriction on text10Type.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contractRefusalReasonCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on contractRefusalReasonCodeType' % {"value" : value, "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type contractRefusalReasonCodeType
            self.validate_contractRefusalReasonCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text500Type
            self.validate_text500Type(self.name)
# end class contractRefusalReasonRef


class contractLifeCycleCaseRef(GeneratedsSuper):
    """Ссылка на справочник: Случаи заключения контракта жизненного цикла"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['contractLifeCycleCaseCodeType', 'text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_contractLifeCycleCaseCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contractLifeCycleCaseRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contractLifeCycleCaseRef.subclass:
            return contractLifeCycleCaseRef.subclass(*args_, **kwargs_)
        else:
            return contractLifeCycleCaseRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_contractLifeCycleCaseCodeType(self, value):
        result = True
        # Validate type contractLifeCycleCaseCodeType, a restriction on text10Type.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on contractLifeCycleCaseCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on contractLifeCycleCaseCodeType' % {"value" : value, "lineno": lineno} )
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
            # validate type contractLifeCycleCaseCodeType
            self.validate_contractLifeCycleCaseCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class contractLifeCycleCaseRef


class changePriceFoundationRef(GeneratedsSuper):
    """Ссылка на справочник: Обоснования изменения цены контракта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['changePriceFoundationNumType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_changePriceFoundationNumType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, changePriceFoundationRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if changePriceFoundationRef.subclass:
            return changePriceFoundationRef.subclass(*args_, **kwargs_)
        else:
            return changePriceFoundationRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_changePriceFoundationNumType(self, value):
        result = True
        # Validate type changePriceFoundationNumType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on changePriceFoundationNumType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on changePriceFoundationNumType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type changePriceFoundationNumType
            self.validate_changePriceFoundationNumType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class changePriceFoundationRef


class closedEPCasesRef(GeneratedsSuper):
    """Ссылка на справочник: Случаи проведения закрытой электронной
    процедуры"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_text10Type(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, closedEPCasesRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if closedEPCasesRef.subclass:
            return closedEPCasesRef.subclass(*args_, **kwargs_)
        else:
            return closedEPCasesRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text10Type(self, value):
        result = True
        # Validate type text10Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type text10Type
            self.validate_text10Type(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class closedEPCasesRef


class currencyRef(GeneratedsSuper):
    """Ссылка на ОКВ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['currencyCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text50Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_currencyCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text50Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, currencyRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if currencyRef.subclass:
            return currencyRef.subclass(*args_, **kwargs_)
        else:
            return currencyRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_currencyCodeType(self, value):
        result = True
        # Validate type currencyCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on currencyCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on currencyCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text50Type(self, value):
        result = True
        # Validate type text50Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type currencyCodeType
            self.validate_currencyCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text50Type
            self.validate_text50Type(self.name)
# end class currencyRef


class currencyCBRFRef(GeneratedsSuper):
    """Ссылка на справочник "Список валют, курс на которые устанавливается ЦБ
    РФ" (nsiContractCurrencyCBRF)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['currencyCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text50Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_currencyCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text50Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, currencyCBRFRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if currencyCBRFRef.subclass:
            return currencyCBRFRef.subclass(*args_, **kwargs_)
        else:
            return currencyCBRFRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_currencyCodeType(self, value):
        result = True
        # Validate type currencyCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on currencyCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on currencyCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text50Type(self, value):
        result = True
        # Validate type text50Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type currencyCodeType
            self.validate_currencyCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text50Type
            self.validate_text50Type(self.name)
# end class currencyCBRFRef


class deviationFactFoundationRef(GeneratedsSuper):
    """Ссылка на справочник Причины признания участника уклонившимся от
    заключения контракта"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['deviationFactFoundationCodeType', 'text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text1000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_deviationFactFoundationCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text1000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, deviationFactFoundationRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if deviationFactFoundationRef.subclass:
            return deviationFactFoundationRef.subclass(*args_, **kwargs_)
        else:
            return deviationFactFoundationRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_deviationFactFoundationCodeType(self, value):
        result = True
        # Validate type deviationFactFoundationCodeType, a restriction on text10Type.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on deviationFactFoundationCodeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on deviationFactFoundationCodeType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_text1000Type(self, value):
        result = True
        # Validate type text1000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type deviationFactFoundationCodeType
            self.validate_deviationFactFoundationCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text1000Type
            self.validate_text1000Type(self.name)
# end class deviationFactFoundationRef


class drugChangeReasonRef(GeneratedsSuper):
    """Ссылка на справочник: Причины корректировки справочных данных о
    лекарственных препаратах"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_text10Type(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, drugChangeReasonRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if drugChangeReasonRef.subclass:
            return drugChangeReasonRef.subclass(*args_, **kwargs_)
        else:
            return drugChangeReasonRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text10Type(self, value):
        result = True
        # Validate type text10Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type text10Type
            self.validate_text10Type(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class drugChangeReasonRef


class documentKindRef(GeneratedsSuper):
    """Ссылка на справочник: Виды прикреплённых документов"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_text10Type(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, documentKindRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if documentKindRef.subclass:
            return documentKindRef.subclass(*args_, **kwargs_)
        else:
            return documentKindRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text10Type(self, value):
        result = True
        # Validate type text10Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type text10Type
            self.validate_text10Type(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class documentKindRef


class ETPRef(GeneratedsSuper):
    """Ссылка на справочник Электронные площадки по ПП РФ № 615"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['etpCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text200Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'url': MemberSpec_('url', ['hrefType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'url', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, url=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_etpCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text200Type(self.name)
        self.name_nsprefix_ = None
        self.url = url
        self.validate_hrefType(self.url)
        self.url_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ETPRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ETPRef.subclass:
            return ETPRef.subclass(*args_, **kwargs_)
        else:
            return ETPRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_etpCodeType(self, value):
        result = True
        # Validate type etpCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on etpCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on etpCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
    def validate_hrefType(self, value):
        result = True
        # Validate type hrefType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1024:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on hrefType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on hrefType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.name is not None or
            self.url is not None
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
            # validate type etpCodeType
            self.validate_etpCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text200Type
            self.validate_text200Type(self.name)
        elif nodeName_ == 'url':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'url')
            value_ = self.gds_validate_string(value_, node, 'url')
            self.url = value_
            self.url_nsprefix_ = child_.prefix
            # validate type hrefType
            self.validate_hrefType(self.url)
# end class ETPRef


class KVRRef(GeneratedsSuper):
    """Ссылка на справочник "Коды видов расходов" (КВР)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['KVRCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_KVRCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KVRRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KVRRef.subclass:
            return KVRRef.subclass(*args_, **kwargs_)
        else:
            return KVRRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_KVRCodeType(self, value):
        result = True
        # Validate type KVRCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on KVRCodeType' % {"value": encode_str_2_3(value), "lineno": lineno} )
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
            # validate type KVRCodeType
            self.validate_KVRCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class KVRRef


class KTRURef(GeneratedsSuper):
    """Тип: Ссылка на КТРУ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['ktruCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'versionId': MemberSpec_('versionId', 'xs:long', 0, 1, {'minOccurs': '0', 'name': 'versionId', 'type': 'xs:long'}, None),
        'versionNumber': MemberSpec_('versionNumber', 'xs:int', 0, 1, {'minOccurs': '0', 'name': 'versionNumber', 'type': 'xs:int'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, versionId=None, versionNumber=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_ktruCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        self.versionId = versionId
        self.versionId_nsprefix_ = None
        self.versionNumber = versionNumber
        self.versionNumber_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KTRURef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KTRURef.subclass:
            return KTRURef.subclass(*args_, **kwargs_)
        else:
            return KTRURef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ktruCodeType(self, value):
        result = True
        # Validate type ktruCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 25:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ktruCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ktruCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            self.code is not None or
            self.name is not None or
            self.versionId is not None or
            self.versionNumber is not None
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
            # validate type ktruCodeType
            self.validate_ktruCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'versionId' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'versionId')
            ival_ = self.gds_validate_integer(ival_, node, 'versionId')
            self.versionId = ival_
            self.versionId_nsprefix_ = child_.prefix
        elif nodeName_ == 'versionNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'versionNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'versionNumber')
            self.versionNumber = ival_
            self.versionNumber_nsprefix_ = child_.prefix
# end class KTRURef


class NPASt14Ref(GeneratedsSuper):
    """Ссылка на справочник Нормативно-правовые акты, регулирующие допуск
    товаров, работ, услуг в соответствии со ст.14 Закона 44-ФЗ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['NPASt14CodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'shortName': MemberSpec_('shortName', ['text100Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'shortName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, shortName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_NPASt14CodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        self.shortName = shortName
        self.validate_text100Type(self.shortName)
        self.shortName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, NPASt14Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if NPASt14Ref.subclass:
            return NPASt14Ref.subclass(*args_, **kwargs_)
        else:
            return NPASt14Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_NPASt14CodeType(self, value):
        result = True
        # Validate type NPASt14CodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on NPASt14CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on NPASt14CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
    def validate_text100Type(self, value):
        result = True
        # Validate type text100Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text100Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text100Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.name is not None or
            self.shortName is not None
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
            # validate type NPASt14CodeType
            self.validate_NPASt14CodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'shortName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'shortName')
            value_ = self.gds_validate_string(value_, node, 'shortName')
            self.shortName = value_
            self.shortName_nsprefix_ = child_.prefix
            # validate type text100Type
            self.validate_text100Type(self.shortName)
# end class NPASt14Ref


class commonUnitsMeasurementsRef(GeneratedsSuper):
    """Тип: Ссылка на справочник "Общепринятые единицы измерения" """
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okeiCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text1000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_okeiCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text1000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, commonUnitsMeasurementsRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if commonUnitsMeasurementsRef.subclass:
            return commonUnitsMeasurementsRef.subclass(*args_, **kwargs_)
        else:
            return commonUnitsMeasurementsRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okeiCodeType(self, value):
        result = True
        # Validate type okeiCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text1000Type(self, value):
        result = True
        # Validate type text1000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type okeiCodeType
            self.validate_okeiCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text1000Type
            self.validate_text1000Type(self.name)
# end class commonUnitsMeasurementsRef


class OKPORef(GeneratedsSuper):
    """Ссылка на ОКПО"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okpoCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_okpoCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKPORef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKPORef.subclass:
            return OKPORef.subclass(*args_, **kwargs_)
        else:
            return OKPORef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okpoCodeType(self, value):
        result = True
        # Validate type okpoCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okpoCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okpoCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type okpoCodeType
            self.validate_okpoCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class OKPORef


class OKOPFRef(GeneratedsSuper):
    """Ссылка на ОКОПФ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okopfCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'singularName': MemberSpec_('singularName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'singularName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, singularName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_okopfCodeType(self.code)
        self.code_nsprefix_ = None
        self.singularName = singularName
        self.validate_text2000Type(self.singularName)
        self.singularName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKOPFRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKOPFRef.subclass:
            return OKOPFRef.subclass(*args_, **kwargs_)
        else:
            return OKOPFRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okopfCodeType(self, value):
        result = True
        # Validate type okopfCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okopfCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okopfCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            self.code is not None or
            self.singularName is not None
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
            # validate type okopfCodeType
            self.validate_okopfCodeType(self.code)
        elif nodeName_ == 'singularName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'singularName')
            value_ = self.gds_validate_string(value_, node, 'singularName')
            self.singularName = value_
            self.singularName_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.singularName)
# end class OKOPFRef


class OKPD2Ref(GeneratedsSuper):
    """Ссылка на ОКПД2"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'OKPDCode': MemberSpec_('OKPDCode', ['okpdCodeType', 'xs:string'], 0, 0, {'name': 'OKPDCode', 'type': 'xs:string'}, None),
        'OKPDName': MemberSpec_('OKPDName', ['okpdNameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'OKPDName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, OKPDCode=None, OKPDName=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.OKPDCode = OKPDCode
        self.validate_okpdCodeType(self.OKPDCode)
        self.OKPDCode_nsprefix_ = None
        self.OKPDName = OKPDName
        self.validate_okpdNameType(self.OKPDName)
        self.OKPDName_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKPD2Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKPD2Ref.subclass:
            return OKPD2Ref.subclass(*args_, **kwargs_)
        else:
            return OKPD2Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okpdCodeType(self, value):
        result = True
        # Validate type okpdCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okpdCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okpdCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_okpdNameType(self, value):
        result = True
        # Validate type okpdNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okpdNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okpdNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.OKPDCode is not None or
            self.OKPDName is not None
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
        if nodeName_ == 'OKPDCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OKPDCode')
            value_ = self.gds_validate_string(value_, node, 'OKPDCode')
            self.OKPDCode = value_
            self.OKPDCode_nsprefix_ = child_.prefix
            # validate type okpdCodeType
            self.validate_okpdCodeType(self.OKPDCode)
        elif nodeName_ == 'OKPDName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'OKPDName')
            value_ = self.gds_validate_string(value_, node, 'OKPDName')
            self.OKPDName = value_
            self.OKPDName_nsprefix_ = child_.prefix
            # validate type okpdNameType
            self.validate_okpdNameType(self.OKPDName)
# end class OKPD2Ref


class OKEIRef(GeneratedsSuper):
    """Ссылка на ОКЕИ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okeiCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'nationalCode': MemberSpec_('nationalCode', ['nationalCode', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nationalCode', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text1000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, nationalCode=None, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_okeiCodeType(self.code)
        self.code_nsprefix_ = None
        self.nationalCode = nationalCode
        self.nationalCode_nsprefix_ = None
        self.name = name
        self.validate_text1000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKEIRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKEIRef.subclass:
            return OKEIRef.subclass(*args_, **kwargs_)
        else:
            return OKEIRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okeiCodeType(self, value):
        result = True
        # Validate type okeiCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text1000Type(self, value):
        result = True
        # Validate type text1000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.nationalCode is not None or
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
            # validate type okeiCodeType
            self.validate_okeiCodeType(self.code)
        elif nodeName_ == 'nationalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nationalCode')
            value_ = self.gds_validate_string(value_, node, 'nationalCode')
            self.nationalCode = value_
            self.nationalCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text1000Type
            self.validate_text1000Type(self.name)
# end class OKEIRef


class nationalCode(GeneratedsSuper):
    """Национальное условное обозначение (поле localSymbol в справочнике ОКЕИ
    (nsiOKEI)). Игнорируется при приеме. автоматически заполняется
    значением из справочника и выгружается"""
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
                CurrentSubclassModule_, nationalCode)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if nationalCode.subclass:
            return nationalCode.subclass(*args_, **kwargs_)
        else:
            return nationalCode(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_nationalCode(self, value):
        result = True
        # Validate type nationalCode, a restriction on xs:string.
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
# end class nationalCode


class contractOKEIRef(GeneratedsSuper):
    """Ссылка на ОКЕИ в Реестре контрактов"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okeiCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'nationalCode': MemberSpec_('nationalCode', ['text50Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nationalCode', 'type': 'xs:string'}, None),
        'fullName': MemberSpec_('fullName', ['text1000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, nationalCode=None, fullName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_okeiCodeType(self.code)
        self.code_nsprefix_ = None
        self.nationalCode = nationalCode
        self.validate_text50Type(self.nationalCode)
        self.nationalCode_nsprefix_ = None
        self.fullName = fullName
        self.validate_text1000Type(self.fullName)
        self.fullName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contractOKEIRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contractOKEIRef.subclass:
            return contractOKEIRef.subclass(*args_, **kwargs_)
        else:
            return contractOKEIRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okeiCodeType(self, value):
        result = True
        # Validate type okeiCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text50Type(self, value):
        result = True
        # Validate type text50Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text1000Type(self, value):
        result = True
        # Validate type text1000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.nationalCode is not None or
            self.fullName is not None
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
            # validate type okeiCodeType
            self.validate_okeiCodeType(self.code)
        elif nodeName_ == 'nationalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nationalCode')
            value_ = self.gds_validate_string(value_, node, 'nationalCode')
            self.nationalCode = value_
            self.nationalCode_nsprefix_ = child_.prefix
            # validate type text50Type
            self.validate_text50Type(self.nationalCode)
        elif nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text1000Type
            self.validate_text1000Type(self.fullName)
# end class contractOKEIRef


class contractOKEIExtendedRef(GeneratedsSuper):
    """Ссылка на ОКЕИ в Реестре контрактов расширенная"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okeiCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'nationalCode': MemberSpec_('nationalCode', ['text50Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nationalCode', 'type': 'xs:string'}, None),
        'trueNationalCode': MemberSpec_('trueNationalCode', ['text50Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'trueNationalCode', 'type': 'xs:string'}, None),
        'fullName': MemberSpec_('fullName', ['text1000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullName', 'type': 'xs:string'}, None),
        'nationalName': MemberSpec_('nationalName', ['text50Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nationalName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, nationalCode=None, trueNationalCode=None, fullName=None, nationalName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_okeiCodeType(self.code)
        self.code_nsprefix_ = None
        self.nationalCode = nationalCode
        self.validate_text50Type(self.nationalCode)
        self.nationalCode_nsprefix_ = None
        self.trueNationalCode = trueNationalCode
        self.validate_text50Type(self.trueNationalCode)
        self.trueNationalCode_nsprefix_ = None
        self.fullName = fullName
        self.validate_text1000Type(self.fullName)
        self.fullName_nsprefix_ = None
        self.nationalName = nationalName
        self.validate_text50Type(self.nationalName)
        self.nationalName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contractOKEIExtendedRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contractOKEIExtendedRef.subclass:
            return contractOKEIExtendedRef.subclass(*args_, **kwargs_)
        else:
            return contractOKEIExtendedRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okeiCodeType(self, value):
        result = True
        # Validate type okeiCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okeiCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text50Type(self, value):
        result = True
        # Validate type text50Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 50:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text50Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text1000Type(self, value):
        result = True
        # Validate type text1000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.code is not None or
            self.nationalCode is not None or
            self.trueNationalCode is not None or
            self.fullName is not None or
            self.nationalName is not None
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
            # validate type okeiCodeType
            self.validate_okeiCodeType(self.code)
        elif nodeName_ == 'nationalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nationalCode')
            value_ = self.gds_validate_string(value_, node, 'nationalCode')
            self.nationalCode = value_
            self.nationalCode_nsprefix_ = child_.prefix
            # validate type text50Type
            self.validate_text50Type(self.nationalCode)
        elif nodeName_ == 'trueNationalCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'trueNationalCode')
            value_ = self.gds_validate_string(value_, node, 'trueNationalCode')
            self.trueNationalCode = value_
            self.trueNationalCode_nsprefix_ = child_.prefix
            # validate type text50Type
            self.validate_text50Type(self.trueNationalCode)
        elif nodeName_ == 'fullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fullName')
            value_ = self.gds_validate_string(value_, node, 'fullName')
            self.fullName = value_
            self.fullName_nsprefix_ = child_.prefix
            # validate type text1000Type
            self.validate_text1000Type(self.fullName)
        elif nodeName_ == 'nationalName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nationalName')
            value_ = self.gds_validate_string(value_, node, 'nationalName')
            self.nationalName = value_
            self.nationalName_nsprefix_ = child_.prefix
            # validate type text50Type
            self.validate_text50Type(self.nationalName)
# end class contractOKEIExtendedRef


class OKSMRef(GeneratedsSuper):
    """Ссылка на страну"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'countryCode': MemberSpec_('countryCode', ['countryCodeType', 'xs:string'], 0, 0, {'name': 'countryCode', 'type': 'xs:string'}, None),
        'countryFullName': MemberSpec_('countryFullName', ['text200Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'countryFullName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, countryCode=None, countryFullName=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.countryCode = countryCode
        self.validate_countryCodeType(self.countryCode)
        self.countryCode_nsprefix_ = None
        self.countryFullName = countryFullName
        self.validate_text200Type(self.countryFullName)
        self.countryFullName_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKSMRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKSMRef.subclass:
            return OKSMRef.subclass(*args_, **kwargs_)
        else:
            return OKSMRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_countryCodeType(self, value):
        result = True
        # Validate type countryCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on countryCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on countryCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
    def hasContent_(self):
        if (
            self.countryCode is not None or
            self.countryFullName is not None
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
        if nodeName_ == 'countryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCode')
            value_ = self.gds_validate_string(value_, node, 'countryCode')
            self.countryCode = value_
            self.countryCode_nsprefix_ = child_.prefix
            # validate type countryCodeType
            self.validate_countryCodeType(self.countryCode)
        elif nodeName_ == 'countryFullName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryFullName')
            value_ = self.gds_validate_string(value_, node, 'countryFullName')
            self.countryFullName = value_
            self.countryFullName_nsprefix_ = child_.prefix
            # validate type text200Type
            self.validate_text200Type(self.countryFullName)
# end class OKSMRef


class OKFSRef(GeneratedsSuper):
    """Ссылка на ОКФС"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['okfsCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_okfsCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKFSRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKFSRef.subclass:
            return OKFSRef.subclass(*args_, **kwargs_)
        else:
            return OKFSRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_okfsCodeType(self, value):
        result = True
        # Validate type okfsCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on okfsCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on okfsCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type okfsCodeType
            self.validate_okfsCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class OKFSRef


class OKTMORef(GeneratedsSuper):
    """Ссылка на ОКТМО"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['oktmoCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text1000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_oktmoCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text1000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKTMORef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKTMORef.subclass:
            return OKTMORef.subclass(*args_, **kwargs_)
        else:
            return OKTMORef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_oktmoCodeType(self, value):
        result = True
        # Validate type oktmoCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on oktmoCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on oktmoCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_text1000Type(self, value):
        result = True
        # Validate type text1000Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text1000Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type oktmoCodeType
            self.validate_oktmoCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text1000Type
            self.validate_text1000Type(self.name)
# end class OKTMORef


class OKTMOPPORef(GeneratedsSuper):
    """Ссылка на ОКТМО ППО (Справочник ZAKUPKI_DEV.NSI_PPO)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['oktmoCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_oktmoCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OKTMOPPORef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OKTMOPPORef.subclass:
            return OKTMOPPORef.subclass(*args_, **kwargs_)
        else:
            return OKTMOPPORef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_oktmoCodeType(self, value):
        result = True
        # Validate type oktmoCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on oktmoCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on oktmoCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type oktmoCodeType
            self.validate_oktmoCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class OKTMOPPORef


class organizationRef(GeneratedsSuper):
    """Ссылка на организацию"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'regNum': MemberSpec_('regNum', ['spzNumType', 'xs:string'], 0, 0, {'name': 'regNum', 'type': 'xs:string'}, None),
        'consRegistryNum': MemberSpec_('consRegistryNum', ['consRegistryNumType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'consRegistryNum', 'type': 'xs:string'}, None),
        'fullName': MemberSpec_('fullName', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'fullName', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, regNum=None, consRegistryNum=None, fullName=None, gds_collector_=None, **kwargs_):
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
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, organizationRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if organizationRef.subclass:
            return organizationRef.subclass(*args_, **kwargs_)
        else:
            return organizationRef(*args_, **kwargs_)
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
    def hasContent_(self):
        if (
            self.regNum is not None or
            self.consRegistryNum is not None or
            self.fullName is not None
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
# end class organizationRef


class placingWayRef(GeneratedsSuper):
    """Тип: Подспособ определения поставщика"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['placingWayCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text500Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_placingWayCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text500Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, placingWayRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if placingWayRef.subclass:
            return placingWayRef.subclass(*args_, **kwargs_)
        else:
            return placingWayRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_placingWayCodeType(self, value):
        result = True
        # Validate type placingWayCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on placingWayCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on placingWayCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type placingWayCodeType
            self.validate_placingWayCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text500Type
            self.validate_text500Type(self.name)
# end class placingWayRef


class prefsReqsRef(GeneratedsSuper):
    """Ссылка на справочник Преимущества (требования, ограничения)"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'shortName': MemberSpec_('shortName', ['prefsReqsShortNameType', 'xs:string'], 0, 0, {'name': 'shortName', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, shortName=None, name=None, gds_collector_=None, **kwargs_):
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
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, prefsReqsRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if prefsReqsRef.subclass:
            return prefsReqsRef.subclass(*args_, **kwargs_)
        else:
            return prefsReqsRef(*args_, **kwargs_)
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
    def hasContent_(self):
        if (
            self.shortName is not None or
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
# end class prefsReqsRef


class prefRateRef(GeneratedsSuper):
    """Ссылка на справочник вариантов размера преференциальной ставки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['text10Type', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'prefValue': MemberSpec_('prefValue', ['percentRestr0100Type', 'xs:double'], 0, 0, {'name': 'prefValue', 'type': 'xs:double'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, code=None, prefValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_text10Type(self.code)
        self.code_nsprefix_ = None
        self.prefValue = prefValue
        self.validate_percentRestr0100Type(self.prefValue)
        self.prefValue_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, prefRateRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if prefRateRef.subclass:
            return prefRateRef.subclass(*args_, **kwargs_)
        else:
            return prefRateRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_text10Type(self, value):
        result = True
        # Validate type text10Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on text10Type' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            self.code is not None or
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
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type text10Type
            self.validate_text10Type(self.code)
        elif nodeName_ == 'prefValue' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'prefValue')
            fval_ = self.gds_validate_double(fval_, node, 'prefValue')
            self.prefValue = fval_
            self.prefValue_nsprefix_ = child_.prefix
            # validate type percentRestr0100Type
            self.validate_percentRestr0100Type(self.prefValue)
# end class prefRateRef


class righSideKTRURef(GeneratedsSuper):
    """Тип: Ссылка на ПЧ КТРУ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['rightSideKTRUCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
        'versionNumber': MemberSpec_('versionNumber', 'xs:int', 0, 1, {'minOccurs': '0', 'name': 'versionNumber', 'type': 'xs:int'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_) + ['extensiontype_']
    subclass = None
    superclass = None
    def __init__(self, code=None, name=None, versionNumber=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = code
        self.validate_rightSideKTRUCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
        self.versionNumber = versionNumber
        self.versionNumber_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, righSideKTRURef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if righSideKTRURef.subclass:
            return righSideKTRURef.subclass(*args_, **kwargs_)
        else:
            return righSideKTRURef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_rightSideKTRUCodeType(self, value):
        result = True
        # Validate type rightSideKTRUCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 18:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on rightSideKTRUCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on rightSideKTRUCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            self.code is not None or
            self.name is not None or
            self.versionNumber is not None
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
            # validate type rightSideKTRUCodeType
            self.validate_rightSideKTRUCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
        elif nodeName_ == 'versionNumber' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'versionNumber')
            ival_ = self.gds_validate_integer(ival_, node, 'versionNumber')
            self.versionNumber = ival_
            self.versionNumber_nsprefix_ = child_.prefix
# end class righSideKTRURef


class rejectReasonRef(GeneratedsSuper):
    """Ссылка на справочник Причины для отказа в допуске заявки"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['rejectReasonCode', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['rejectReasonName', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_rejectReasonCode(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_rejectReasonName(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, rejectReasonRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if rejectReasonRef.subclass:
            return rejectReasonRef.subclass(*args_, **kwargs_)
        else:
            return rejectReasonRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_rejectReasonCode(self, value):
        result = True
        # Validate type rejectReasonCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on rejectReasonCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on rejectReasonCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_rejectReasonName(self, value):
        result = True
        # Validate type rejectReasonName, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on rejectReasonName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on rejectReasonName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type rejectReasonCode
            self.validate_rejectReasonCode(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type rejectReasonName
            self.validate_rejectReasonName(self.name)
# end class rejectReasonRef


class docRejectReasonRef(GeneratedsSuper):
    """Ссылка на справочник: Причины для отказа в предоставлении документации о
    закупке"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['rejectReasonCode', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['rejectReasonName', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_rejectReasonCode(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_rejectReasonName(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, docRejectReasonRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if docRejectReasonRef.subclass:
            return docRejectReasonRef.subclass(*args_, **kwargs_)
        else:
            return docRejectReasonRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_rejectReasonCode(self, value):
        result = True
        # Validate type rejectReasonCode, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on rejectReasonCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on rejectReasonCode' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_rejectReasonName(self, value):
        result = True
        # Validate type rejectReasonName, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 500:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on rejectReasonName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on rejectReasonName' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type rejectReasonCode
            self.validate_rejectReasonCode(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type rejectReasonName
            self.validate_rejectReasonName(self.name)
# end class docRejectReasonRef


class evasDevFactFoundationRef(GeneratedsSuper):
    """Тип: Ссылка на справочник Основания отказа (принятия решения) для ПОК и
    ППУ с 01.01.2021"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['evasDevFactFoundationCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['evasDevFactFoundationNameType', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_evasDevFactFoundationCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_evasDevFactFoundationNameType(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, evasDevFactFoundationRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if evasDevFactFoundationRef.subclass:
            return evasDevFactFoundationRef.subclass(*args_, **kwargs_)
        else:
            return evasDevFactFoundationRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_evasDevFactFoundationCodeType(self, value):
        result = True
        # Validate type evasDevFactFoundationCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 10:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on evasDevFactFoundationCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on evasDevFactFoundationCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_evasDevFactFoundationNameType(self, value):
        result = True
        # Validate type evasDevFactFoundationNameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 1000:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on evasDevFactFoundationNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on evasDevFactFoundationNameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'code':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'code')
            value_ = self.gds_validate_string(value_, node, 'code')
            self.code = value_
            self.code_nsprefix_ = child_.prefix
            # validate type evasDevFactFoundationCodeType
            self.validate_evasDevFactFoundationCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type evasDevFactFoundationNameType
            self.validate_evasDevFactFoundationNameType(self.name)
# end class evasDevFactFoundationRef


class purchaseSubjectRef(GeneratedsSuper):
    """Ссылка на справочник Предметы электронного аукциона по ПП РФ № 615"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['purchaseSubjectCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_purchaseSubjectCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, purchaseSubjectRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if purchaseSubjectRef.subclass:
            return purchaseSubjectRef.subclass(*args_, **kwargs_)
        else:
            return purchaseSubjectRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_purchaseSubjectCodeType(self, value):
        result = True
        # Validate type purchaseSubjectCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on purchaseSubjectCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on purchaseSubjectCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type purchaseSubjectCodeType
            self.validate_purchaseSubjectCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class purchaseSubjectRef


class exclusionReason615Ref(GeneratedsSuper):
    """Ссылка на справочник Справочник оснований для исключения сведений из
    реестра квалифицированных подрядных организаций"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['exclusionReason615CodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_exclusionReason615CodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, exclusionReason615Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if exclusionReason615Ref.subclass:
            return exclusionReason615Ref.subclass(*args_, **kwargs_)
        else:
            return exclusionReason615Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_exclusionReason615CodeType(self, value):
        result = True
        # Validate type exclusionReason615CodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on exclusionReason615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on exclusionReason615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type exclusionReason615CodeType
            self.validate_exclusionReason615CodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class exclusionReason615Ref


class fundingSources615Ref(GeneratedsSuper):
    """Ссылка на справочник Типы источников финансирования ПП РФ № 615"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['fundingSources615CodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text200Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_fundingSources615CodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text200Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, fundingSources615Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if fundingSources615Ref.subclass:
            return fundingSources615Ref.subclass(*args_, **kwargs_)
        else:
            return fundingSources615Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_fundingSources615CodeType(self, value):
        result = True
        # Validate type fundingSources615CodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on fundingSources615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on fundingSources615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type fundingSources615CodeType
            self.validate_fundingSources615CodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text200Type
            self.validate_text200Type(self.name)
# end class fundingSources615Ref


class qualifiedContractorRef(GeneratedsSuper):
    """Ссылка на реестр квалифицированных подрядных организаций по ПП РФ №
    615"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'registryNum': MemberSpec_('registryNum', ['qualifiedContractorCodeType', 'xs:string'], 0, 0, {'name': 'registryNum', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, registryNum=None, name=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.registryNum = registryNum
        self.validate_qualifiedContractorCodeType(self.registryNum)
        self.registryNum_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, qualifiedContractorRef)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if qualifiedContractorRef.subclass:
            return qualifiedContractorRef.subclass(*args_, **kwargs_)
        else:
            return qualifiedContractorRef(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_qualifiedContractorCodeType(self, value):
        result = True
        # Validate type qualifiedContractorCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_qualifiedContractorCodeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_qualifiedContractorCodeType_patterns_, ))
                result = False
        return result
    validate_qualifiedContractorCodeType_patterns_ = [['^(\\d{20})$']]
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
            self.registryNum is not None or
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
        if nodeName_ == 'registryNum':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'registryNum')
            value_ = self.gds_validate_string(value_, node, 'registryNum')
            self.registryNum = value_
            self.registryNum_nsprefix_ = child_.prefix
            # validate type qualifiedContractorCodeType
            self.validate_qualifiedContractorCodeType(self.registryNum)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class qualifiedContractorRef


class serviceWorkSt166Ref(GeneratedsSuper):
    """Ссылка на справочник Виды услуг и (или) работ в соотвествии со ст. 166
    Жилищного кодекса РФ"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['serviceWorkCodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_serviceWorkCodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, serviceWorkSt166Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if serviceWorkSt166Ref.subclass:
            return serviceWorkSt166Ref.subclass(*args_, **kwargs_)
        else:
            return serviceWorkSt166Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_serviceWorkCodeType(self, value):
        result = True
        # Validate type serviceWorkCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on serviceWorkCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on serviceWorkCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type serviceWorkCodeType
            self.validate_serviceWorkCodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class serviceWorkSt166Ref


class terminationGround615Ref(GeneratedsSuper):
    """Ссылка на справочник Основания расторжения договора по капитальному
    ремонту ПП РФ № 615"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['terminationGround615CodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_terminationGround615CodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, terminationGround615Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if terminationGround615Ref.subclass:
            return terminationGround615Ref.subclass(*args_, **kwargs_)
        else:
            return terminationGround615Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_terminationGround615CodeType(self, value):
        result = True
        # Validate type terminationGround615CodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on terminationGround615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on terminationGround615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type terminationGround615CodeType
            self.validate_terminationGround615CodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class terminationGround615Ref


class terminationReason615Ref(GeneratedsSuper):
    """Ссылка на справочник Причины расторжения договора по капитальному
    ремонту ПП РФ № 615"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'code': MemberSpec_('code', ['terminationReason615CodeType', 'xs:string'], 0, 0, {'name': 'code', 'type': 'xs:string'}, None),
        'name': MemberSpec_('name', ['text2000Type', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'name', 'type': 'xs:string'}, None),
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
        self.validate_terminationReason615CodeType(self.code)
        self.code_nsprefix_ = None
        self.name = name
        self.validate_text2000Type(self.name)
        self.name_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, terminationReason615Ref)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if terminationReason615Ref.subclass:
            return terminationReason615Ref.subclass(*args_, **kwargs_)
        else:
            return terminationReason615Ref(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_terminationReason615CodeType(self, value):
        result = True
        # Validate type terminationReason615CodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on terminationReason615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on terminationReason615CodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
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
            # validate type terminationReason615CodeType
            self.validate_terminationReason615CodeType(self.code)
        elif nodeName_ == 'name':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'name')
            value_ = self.gds_validate_string(value_, node, 'name')
            self.name = value_
            self.name_nsprefix_ = child_.prefix
            # validate type text2000Type
            self.validate_text2000Type(self.name)
# end class terminationReason615Ref


class schemeVersion(GeneratedsSuper):
    """Тип: Текущая версия схем"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'current': MemberSpec_('current', 'base:schemeVersionType', 0, 1, {'use': 'optional'}),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, current='11.0', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.current = _cast(None, current)
        self.current_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, schemeVersion)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if schemeVersion.subclass:
            return schemeVersion.subclass(*args_, **kwargs_)
        else:
            return schemeVersion(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_schemeVersionType(self, value):
        # Validate type base:schemeVersionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1.0', '4.1', '4.2', '4.3', '4.3.100', '4.4', '4.4.2', '4.5', '4.6', '5.0', '5.1', '5.2', '6.0', '6.1', '6.2', '6.2.100', '6.3', '6.4', '7.0', '7.1', '7.2', '7.3', '7.5', '8.0', '8.1', '8.2', '8.2.100', '8.3', '9.0', '9.1', '9.2', '9.3', '10.0', '10.1', '10.2', '10.2.310', '10.3', '11.0']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on schemeVersionType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
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
        value = find_attr_value_('current', node)
        if value is not None and 'current' not in already_processed:
            already_processed.add('current')
            self.current = value
            self.validate_schemeVersionType(self.current)    # validate type schemeVersionType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class schemeVersion


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
        rootTag = 'abandonedReasonRef'
        rootClass = abandonedReasonRef
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
        rootTag = 'abandonedReasonRef'
        rootClass = abandonedReasonRef
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
        rootTag = 'abandonedReasonRef'
        rootClass = abandonedReasonRef
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
        rootTag = 'abandonedReasonRef'
        rootClass = abandonedReasonRef
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
##     if not silence:
##         sys.stdout.write('#from BaseTypes import *\n\n')
##         sys.stdout.write('import BaseTypes as model_\n\n')
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
    "{http://zakupki.gov.ru/oos/base/1}bikType": "bikType1",
    "{http://zakupki.gov.ru/oos/base/1}checkResultNumberType": "checkResultNumberType2",
    "{http://zakupki.gov.ru/oos/base/1}innType": "innType3",
    "{http://zakupki.gov.ru/oos/base/1}monthType": "monthType4",
    "{http://zakupki.gov.ru/oos/base/1}prescriptionNumberType": "prescriptionNumberType5",
    "{http://zakupki.gov.ru/oos/base/1}yearType": "yearType6",
    "{http://zakupki.gov.ru/oos/common/1}organizationType": "organizationType7",
    "{http://zakupki.gov.ru/oos/common/1}signatureType": "signatureType8",

}
__all__ = [
    "ETPRef",
    "KTRURef",
    "KVRRef",
    "NPASt14Ref",
    "OKEIRef",
    "OKFSRef",
    "OKOPFRef",
    "OKPD2Ref",
    "OKPORef",
    "OKSMRef",
    "OKTMOPPORef",
    "OKTMORef",
    "abandonedReasonRef",
    "budgetFundsContractRef",
    "changePriceFoundationRef",
    "closedEPCasesRef",
    "commonUnitsMeasurementsRef",
    "contractLifeCycleCaseRef",
    "contractOKEIExtendedRef",
    "contractOKEIRef",
    "contractRefusalReasonRef",
    "currencyCBRFRef",
    "currencyRef",
    "deviationFactFoundationRef",
    "docRejectReasonRef",
    "documentKindRef",
    "drugChangeReasonRef",
    "evasDevFactFoundationRef",
    "exclusionReason615Ref",
    "fundingSources615Ref",
    "nationalCode",
    "organizationRef",
    "placingWayRef",
    "prefRateRef",
    "prefsReqsRef",
    "purchaseSubjectRef",
    "qualifiedContractorRef",
    "rejectReasonRef",
    "righSideKTRURef",
    "schemeVersion",
    "serviceWorkSt166Ref",
    "terminationGround615Ref",
    "terminationReason615Ref"
]
