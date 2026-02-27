@echo off
:: 1. Clear the system path so RVC is 'blind' to other programs
set PATH=%CONDA_PREFIX%\Library\bin;%CONDA_PREFIX%\Scripts;%CONDA_PREFIX%;%SystemRoot%\system32;%SystemRoot%

:: 2. Run the WebUI
python infer-web.py
pause