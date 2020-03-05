echo off
REM Default is Python 3.7

if "%1"=="3.6" goto py_36
if "%1"=="3.8" goto py_38

:py_37
venv-ideas3.7\scripts\activate
goto end

:py_36
venv-ideas3.6\scripts\activate
goto end

:py_38
venv-ideas3.8\scripts\activate

:end
