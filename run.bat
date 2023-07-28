@echo off
if exist "venv" (
    call "venv\Scripts\activate"
) else (
    py -m venv "venv"
    call "venv\Scripts\activate"
    pip install -r "REQUIREMENTS.txt"
    cls
)
py "main.py"
pause
