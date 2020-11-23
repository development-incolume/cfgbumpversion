# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import toml
import subprocess
from pathlib import Path
import sys
root_project = Path(__file__).parent.parent.parent
fpipenv = root_project/'Pipfile'

parsed_toml = toml.loads(fpipenv.read_text())
pkgdev = [x for x in parsed_toml.get('dev-packages')]
pkg = [x for x in parsed_toml.get('packages')]
print(sys.path)

for i in pkgdev:
    print(i)
    subprocess.Popen(f'poetry add -D {i}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# for i in pkg:
#     subprocess.Popen('poetry', 'add', i)
