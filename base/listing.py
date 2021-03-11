from subprocess import Popen, PIPE
import sys
try:
    import json
except ImportError:
    import simplejson as json


RESULT = {}
RESULT['all'] = {}
PIPE = Popen(['cat', '/opt/Ansible/base/inventory'], stdout=PIPE, universal_newlines=True)
RESULT['all']['hosts'] = []

for line in PIPE.stdout.readlines():
    s = line.splitlines()
    RESULT['all']['hosts'] += s

RESULT['all']['vars'] = {}

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(RESULT))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({RESULT['all']}))
else:
    print("Requires an argument. Please use --list or --hosts")
