#!/usr/bin/python3
#NOTE: python3 is already in all linux distros, so: no need for shell (:
p = print
from subprocess import Popen as popen
import sys, os
from random import randint
try: import requests
except:
    p('installing missing pkg: python3-requests')
    popen([sys.executable, '-m', 'pip', 'install', 'requests']).wait()

# create an empty folder
p('creating app_dir')
app_dir = "Legend-Master-unix"
if os.path.exists(app_dir):
    while True:
        try:
            os.rename(app_dir, f"{app_dir}.old{randint(0,999999)}")
        except: continue
else: print("app_dir is ok")
os.mkdir(app_dir)

#wget and install miniconda3
p('wget miniconda3')
popen(['wget', 'https://github.com/ibrahemesam/Legend-Master-Releases/releases/download/Python-Runtime/Miniconda3-py3.9.5-Linux-x86_64.sh']).wait()
p('installing miniconda3')
popen(['chmod', '+x', './Miniconda3-py3.9.5-Linux-x86_64.sh']).wait()
popen(['bash', './Miniconda3-py3.9.5-Linux-x86_64.sh', '-b', '-p', f'{app_dir}/lenv-64']).wait()

##install_script.py##
#get unix64.zip
p('wget unix64.zip')
popen(['wget', 'https://github.com/ibrahemesam/Legend-Master-Releases/releases/download/latest/unix64.zip']).wait()
#unzip it to app_dir/unix64
import zipfile
with zipfile.ZipFile('unix64.zip', 'r') as zip_ref:
    p('unzipping unix64.zip')
    zip_ref.extractall(f"{app_dir}/unix64")
#run the app (popen new session)
p('running app')
popen(['chmod', '+x', f'{app_dir}/unix64/run.sh']).wait()
popen(['bash', os.path.abspath(f'{app_dir}/unix64/run.sh')], start_new_session=True, cwd=f'{app_dir}/unix64')
#clean: rm Miniconda3*sh && rm unix64.zip && rm this .py file
p('cleaning this miss')
os.remove("Miniconda3-py3.9.5-Linux-x86_64.sh")
os.remove("unix64.zip")
os.remove(sys.argv[0])
