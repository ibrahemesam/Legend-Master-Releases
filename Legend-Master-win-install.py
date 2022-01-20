
#a script to auto-download the app
from subprocess import Popen as popen
import sys, os, ctypes

def get_windows_bit_length():
    size = ctypes.sizeof(ctypes.c_voidp)
    if size == 4: return 32
    elif size == 8: return 64
    else: raise Exception("Windows is not 32 or 64. Fuck!")

##install_script.py##
bits = get_windows_bit_length()
#get win*.zip
popen(['powershell', '-c', f'''"Invoke-WebRequest -Uri 'https://github.com/ibrahemesam/Legend-Master-Releases/releases/download/latest/win{bits}.zip' -OutFile win{bits}.zip"''']).wait()

#unzip it to app_dir/win{bits}
import zipfile
with zipfile.ZipFile(f'win{bits}.zip', 'r') as zip_ref:
    zip_ref.extractall(f"{app_dir}/win{bits}")
#run the app (popen new session)
popen([f'{app_dir}/win{bits}/run.exe'], start_new_session=True, cwd=f'{app_dir}/win{bits}')

#clean: rm Miniconda3*sh && rm unix64.zip && rm this .py file
def rm(f): os.remove(f)
[rm(f) for f in ['unzip.exe', f'wenv-{bits}.zip', sys.argv[0], 'Legend-Master-win-install.bat', f'win{bits}.zip']]

