#!/usr/bin/python3

#TODO: convert this file to py && continue
#NOTE: python3 is already in all linux distros, so: no need for shell (:

from subprocess import Popen as popen
import sys, os, randint
try: import requests
except: popen([sys.executable, '-m', 'pip', 'install', 'requests']).wait()

# create an empty folder
app_dir = "Legend-Master-unix"
if os.path.exists(app_dir):
    while True:
        try:
            os.rename(app_dir, f"{app_dir}.old{randint(0,999999)}")
        except: continue
else: print("app_dir is ok")
os.mkdir(app_dir)

#wget and install miniconda3
popen(['wget', 'https://github.com/ibrahemesam/Legend-Master-Releases/releases/download/Python-Runtime/Miniconda3-py3.9.5-Linux-x86_64.sh']).wait()
popen(['chmod', '+x', './Miniconda3-py3.9.5-Linux-x86_64.sh']).wait()
popen(['bash', './Miniconda3-py3.9.5-Linux-x86_64.sh', '-b', '-p', f'{app_dir}/unix-64']).wait()

##install_script.py##
