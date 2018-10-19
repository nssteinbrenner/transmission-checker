#!/usr/bin/env python

import subprocess
import psutil
import sys

for proc in psutil.process_iter():
    try: 
        pinfo = proc.as_dict(attrs=['name'])
    except psutil.NoSuchProcess:
        pass
    else:
        if 'transmission-daemon' in pinfo['name']:
            sys.exit(0)

subprocess.call(['/usr/bin/transmission-daemon', '--port', '9091', '--allowed', '127.0.0.1'])
