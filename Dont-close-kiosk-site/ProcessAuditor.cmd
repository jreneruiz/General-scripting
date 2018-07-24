@echo off
:inicio

set process=chrome.exe
set processKiosk=chrome.exe --kiosk https://kiosk-site/
set ERRORLEVEL=
tasklist | findstr %process%
if ERRORLEVEL==1 start %processKiosk%

set process2=explorer.exe
set ERRORLEVEL=
tasklist | findstr %process2%
if NOT ERRORLEVEL==1 Taskkill /F /IM %process2%

rem delay de 5 sg
@ping -n 5 127.0.0.1 > null
goto inicio