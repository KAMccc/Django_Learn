#!f:\sakura\hsma\qa\KAM\django\hello_django\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rstcheck==3.3.1','console_scripts','rstcheck'
__requires__ = 'rstcheck==3.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rstcheck==3.3.1', 'console_scripts', 'rstcheck')()
    )
