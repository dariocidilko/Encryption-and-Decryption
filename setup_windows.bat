@echo off

REM Check if Python is installed.
python --version >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Installing Python.
    
    REM Download the Python installer.
    curl -L -o python-installer.exe https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe

    REM Run the installer with default settings.
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

    echo Waiting for Python installation to complete.
)

REM Wait until Python is available in PATH.
:WAIT_LOOP

REM Check again if Python is installed.
python --version >nul 2>&1

REM If not installed, wait and check again.
IF %ERRORLEVEL% NEQ 0 (
    timeout /t 2 >nul
    goto WAIT_LOOP
)

echo Python is installed.

REM Install the cryptography package and upgrade pip
python -m pip install --upgrade pip
python -m pip install cryptography

echo The setup is complete.
