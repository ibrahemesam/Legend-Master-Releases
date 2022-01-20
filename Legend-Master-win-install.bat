@echo off

rem create an empty folder
set app_dir=Legend-Master-win
IF exist %app_dir% (
:loop
:someRoutine
setlocal
%@Try%
  REM Normal code goes here
  rem try rename folder if exists
  rename Legend-Master-win Legend-Master-win.old%RANDOM%
%@EndTry%
:@Catch
  REM Exception handling code goes here
  goto loop
:@EndCatch
) ELSE ( echo app_dir is ok )
mkdir %app_dir%

rem get cpu bits length
IF %PROCESSOR_ARCHITECTURE%==x86 (set bits=32) ELSE (bits=64)

rem wget required files
rem unzip.exe
powershell -c "Invoke-WebRequest -Uri 'https://github.com/ibrahemesam/Legend-Master-Releases/releases/download/Python-Runtime/unzip.exe' -OutFile unzip.exe"
rem wenv-*
powershell -c "Invoke-WebRequest -Uri 'https://github.com/ibrahemesam/Legend-Master-Releases/releases/download/Python-Runtime/wenv-%bits%.zip' -OutFile wenv-%bits%.zip"
rem install_script.py
powershell -c "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/ibrahemesam/Legend-Master-Releases/main/install_script.py' -OutFile install_script.py"

rem unzip wenv-%bits%.zip
unzip.exe wenv-%bits%.zip -d %app_dir%\wenv-%bits%

rem run install_script.py with install_script.exe
%app_dir%\wenv-%bits%\python.exe install_script.py
