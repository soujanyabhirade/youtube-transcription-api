@echo off
echo Starting YouTube Transcription Server...
echo.

REM Activate virtual environment if it exists
if exist .venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Check if cookies.txt exists
if not exist cookies.txt (
    echo WARNING: cookies.txt not found!
    echo Please export cookies from your browser first.
    echo See README.md for instructions.
    echo.
    pause
    exit /b 1
)

REM Start the server
echo Starting server on http://127.0.0.1:8000
echo Press Ctrl+C to stop
echo.
python main.py

pause
