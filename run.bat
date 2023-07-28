@echo off

if exist "venv" (
    call "venv\Scripts\activate"
) else (
    py -m venv "venv"
    call "venv\Scripts\activate"

    pip install -r "REQUIREMENTS.txt"
)

if exist "token.txt" (
    set BOT_TOKEN < "token.txt"
) else (
    set /p BOT_TOKEN = Veuillez entrer votre token :
    echo %BOT_TOKEN% > "token.txt"
)

cls
py "main.py"
pause
