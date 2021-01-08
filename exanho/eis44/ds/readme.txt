1. cp -T exanho/eis44/ds/generateds_config.py /home/kks/git/exanho/venv/bin/generateds_config.py

2. /home/kks/git/exanho/venv/bin/generateDS.py -f --one-file-per-xsd --output-directory="/home/kks/git/exanho/exanho/eis44/ds" --use-source-file-as-module-name --use-getter-setter="none" --enable-slots --member-specs="dict" --export="" --silence /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/export_types.xsd

Command line options:
  ('-f', '')
  ('--one-file-per-xsd', '')
  ('--output-directory', '/home/kks/git/exanho/exanho/eis44/ds')
  ('--use-source-file-as-module-name', '')
  ('--use-getter-setter', 'none')
  ('--enable-slots', '')
  ('--member-specs', 'dict')
  ('--export', '')
  ('--silence', '')
Command line arguments:
  /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/export_types.xsd

3. Replace 

3.1 in all generated py-files
from generatedssuper import GeneratedsSuper
with
from .generatedssuper import GeneratedsSuper

3.2.1 export_types.py
#
# Data representation classes.
#

from ...
...

with

#
# Data representation classes.
#

from .IntegrationTypes import zfcs_contract2015Type
from .IntegrationTypes import zfcs_contractCancel2015Type
from .IntegrationTypes import zfcs_contractProcedure2015Type
from .IntegrationTypes import zfcs_contractProcedureCancel2015Type

3.2.2 IntegrationTypes.py
#
# Data representation classes.
#

from ...
...

with

#
# Data representation classes.
#

from .BaseTypes import *
from .CommonTypes import *

3.2.3 CommonTypes.py
#
# Data representation classes.
#

from ...
...

with

#
# Data representation classes.
#

from .BaseTypes import *

3.2.4 BaseTypes.py
#
# Data representation classes.
#

from ...
...

with

#
# Data representation classes.
#

4 Fix classes:

4.1 zfcs_contract2015Type

member_data_items_ = {
        ...
        'suppliers': MemberSpec_('suppliers', 'suppliers', 0, 0, {'name': 'suppliers', 'type': 'contract2015suppliers'}, None),
        ...
    }

def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        ...
        elif nodeName_ == 'suppliers':
            obj_ = contract2015suppliers.factory(parent_object_=self)
            ...
        ...

5. Add classes:

5.1
class contract2015suppliers(GeneratedsSuper):
    """Поставщики"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = {
        'supplier': MemberSpec_('supplier', 'supplier', 1, 0, {'maxOccurs': 'unbounded', 'name': 'supplier', 'type': 'zfcs_contract2015SupplierType'}, None),
    }
    __slots__ = GeneratedsSuper.gds_subclass_slots(member_data_items_)
    subclass = None
    superclass = None
    def __init__(self, supplier=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if supplier is None:
            self.supplier = []
        else:
            self.supplier = supplier
        self.supplier_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contract2015suppliers)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contract2015suppliers.subclass:
            return contract2015suppliers.subclass(*args_, **kwargs_)
        else:
            return contract2015suppliers(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.supplier
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
        if nodeName_ == 'supplier':
            obj_ = zfcs_contract2015SupplierType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.supplier.append(obj_)
            obj_.original_tagname_ = 'supplier'
# end class contract2015suppliers