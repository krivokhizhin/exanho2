#!/usr/bin/env python
# -*- mode: pymode; coding: latin1; -*-

import sys
import re

#
# You must include the following class definition at the top of
#   your method specification file.
#
class MethodSpec(object):
    def __init__(self, name='', source='', class_names='',
            class_names_compiled=None):
        """MethodSpec -- A specification of a method.
        Member variables:
            name -- The method name
            source -- The source code for the method.  Must be
                indented to fit in a class definition.
            class_names -- A regular expression that must match the
                class names in which the method is to be inserted.
            class_names_compiled -- The compiled class names.
                generateDS.py will do this compile for you.
        """
        self.name = name
        self.source = source
        if class_names is None:
            self.class_names = ('.*', )
        else:
            self.class_names = class_names
        if class_names_compiled is None:
            self.class_names_compiled = re.compile(self.class_names)
        else:
            self.class_names_compiled = class_names_compiled
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_source(self):
        return self.source
    def set_source(self, source):
        self.source = source
    def get_class_names(self):
        return self.class_names
    def set_class_names(self, class_names):
        self.class_names = class_names
        self.class_names_compiled = re.compile(class_names)
    def get_class_names_compiled(self):
        return self.class_names_compiled
    def set_class_names_compiled(self, class_names_compiled):
        self.class_names_compiled = class_names_compiled
    def match_name(self, class_name):
        """Match against the name of the class currently being generated.
        If this method returns True, the method will be inserted in
          the generated class.
        """
        if self.class_names_compiled.search(class_name):
            return True
        else:
            return False
    def get_interpolated_source(self, values_dict):
        """Get the method source code, interpolating values from values_dict
        into it.  The source returned by this method is inserted into
        the generated class.
        """
        source = self.source % values_dict
        return source
    def show(self):
        print('specification:')
        print('    name: %s' % (self.name, ))
        print(self.source)
        print('    class_names: %s' % (self.class_names, ))
        print('    names pat  : %s' % (self.class_names_compiled.pattern, ))


#
# Provide one or more method specification such as the following.
# Notes:
# - Each generated class contains a class variable _member_data_items.
#   This variable contains a list of instances of class _MemberSpec.
#   See the definition of class _MemberSpec near the top of the
#   generated superclass file and also section "User Methods" in
#   the documentation, as well as the examples below.

#
# Replace the following method specifications with your own.

pattern_class_names = r'^zfcs_contract2015Type$|^zfcs_contractCancel2015Type$|^zfcs_contractProcedure2015Type$|^zfcs_contractProcedureCancel2015Type$'

#
# get_xml_tag method specification #1
#
get_xml_tag = MethodSpec(name='get_xml_tag',
    source='''\
    def get_xml_tag(self):
        return self.gds_elementtree_node_.tag
''',
    class_names=pattern_class_names,
    )

#
# get_children method specification #2
#
get_children = MethodSpec(name='get_children',
    source='''\
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
''',
    class_names=r'^export$',
    )


#
# Provide a list of your method specifications.
#   This list of specifications must be named METHOD_SPECS.
#
METHOD_SPECS = (
    get_xml_tag,
    get_children
    )


def test():
    for spec in METHOD_SPECS:
        spec.show()

def main():
    test()


if __name__ == '__main__':
    main()

