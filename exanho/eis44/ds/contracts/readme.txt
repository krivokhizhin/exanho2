1. Copy xsd-files:
    cp -T /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/fcsExport.xsd /home/kks/git/exanho/exanho/eis44/ds/contracts/fcsExport.py
    cp -T /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/IntegrationTypes.xsd /home/kks/git/exanho/exanho/eis44/ds/contracts/IntegrationTypes.py
    cp -T /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/CommonTypes.xsd /home/kks/git/exanho/exanho/eis44/ds/contracts/CommonTypes.py
    cp -T /home/kks/git/exanho/exanho/eis44/ds/xsd/11.0.4/BaseTypes.xsd /home/kks/git/exanho/exanho/eis44/ds/contracts/BaseTypes.py

2. Correct xsd schemas:
2.1 fcsExport.xsd: remove unnecessary document types
2.2 IntegrationTypes.xsd: remove unnecessary document types, except for sections:
    - <!--Актуальные типы-->
    - <!--Дополнительная информация о закупках, контрактах (РДИ, бывш. ДИЗК)-->
    - <!--Контракты (РК). Основные документы-->
    - <!--Контракты (РК). Вспомогательные типы-->
    - <!--Ссылки на НСИ-->
    - <!--Недобросовестные поставщики (РНП)-->
    - <!--Разное-->
    - <!--Ссылки на общие справочники-->
    - and all group elements
2.3 IntegrationTypes.xsd:add corrected types from file (/home/kks/git/exanho/exanho/eis44/ds/contracts/xsd/corrected_types):
  - corr_supplierLegalEntityRF for zfcs_contract2015SupplierType -> legalEntityRF
  - corr_supplierLegalEntityForeignState for zfcs_contract2015SupplierType -> legalEntityForeignState
  - corr_supplierIndividualPersonRF for zfcs_contract2015SupplierType -> individualPersonRF 
  - corr_supplierIndividualPersonForeignState for zfcs_contract2015SupplierType -> individualPersonForeignState

3. cp -T exanho/eis44/ds/generateds_config.py /home/kks/git/exanho/venv/bin/generateds_config.py

4. python /home/kks/git/exanho/venv/bin/generateDS.py -f --one-file-per-xsd --output-directory="/home/kks/git/exanho/exanho/eis44/ds/contracts" --use-source-file-as-module-name --use-getter-setter="none" --enable-slots --member-specs="dict" --export="" --silence /home/kks/git/exanho/exanho/eis44/ds/contracts/xsd/fcsExport.xsd

Command line options:
  ('-f', '')
  ('--one-file-per-xsd', '')
  ('--output-directory', '/home/kks/git/exanho/exanho/eis44/ds/contracts')
  ('--use-source-file-as-module-name', '')
  ('--use-getter-setter', 'none')
  ('--enable-slots', '')
  ('--member-specs', 'dict')
  ('--export', '')
  ('--silence', '')
Command line arguments:
  /home/kks/git/exanho/exanho/eis44/ds/contracts/xsd/fcsExport.xsd

5. Replace 

5.1 in all generated py-files
from generatedssuper import GeneratedsSuper
with
from ..generatedssuper import GeneratedsSuper

5.2.1 IntegrationTypes.py
#
# Data representation classes.
#

from ...
...

with

#
#. Data representation classes.
#

from .BaseTypes import *
from .CommonTypes import *

5.2.2 CommonTypes.py
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

5.2.3 BaseTypes.py
#
# Data representation classes.
#

from ...
...

with

#
# Data representation classes.
#