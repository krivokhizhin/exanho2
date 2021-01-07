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