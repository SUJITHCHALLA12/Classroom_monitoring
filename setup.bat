@echo off
REM Classroom & Timetable Monitoring System - Quick Setup Script (Windows)

echo.
echo ===============================================
echo Classroom Timetable Monitoring System
echo Quick Setup Script
echo ===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [STEP 1] Installing Dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed successfully

echo.
echo [STEP 2] Initializing Sample Data (Optional)
set /p SAMPLE="Do you want to load sample data? (y/n): "
if /i "%SAMPLE%"=="y" (
    python init_sample_data.py
    if %errorlevel% neq 0 (
        echo ERROR: Failed to initialize sample data
        pause
        exit /b 1
    )
    echo ✓ Sample data loaded successfully
)

echo.
echo ===============================================
echo ✓ Setup Complete!
echo ===============================================
echo.
echo Starting the application...
echo.
echo Once the server starts, open your browser to:
echo   http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
pause

python app.py
