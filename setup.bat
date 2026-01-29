@echo off
:: FinFlow - Automated Setup Script
:: This script sets up the development environment for FinFlow

setlocal EnableDelayedExpansion

echo.
echo ============================================================
echo                    FinFlow Setup Script
echo ============================================================
echo.

:: Check if Python is installed
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version
echo       Python found!
echo.

:: Check if MongoDB is installed
echo [2/6] Checking MongoDB installation...
where mongod >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] MongoDB is not found in PATH.
    echo.
    echo MongoDB is required to run this application.
    echo Please install MongoDB Community Server from:
    echo https://www.mongodb.com/try/download/community
    echo.
    echo After installation, ensure MongoDB service is running.
    echo You can start MongoDB service with: net start MongoDB
    echo.
    set /p CONTINUE="Do you want to continue anyway? (y/n): "
    if /i "!CONTINUE!" neq "y" (
        pause
        exit /b 1
    )
) else (
    echo       MongoDB found!
)
echo.

:: Check if MongoDB service is running
echo [3/6] Checking if MongoDB service is running...
sc query MongoDB >nul 2>&1
if %errorlevel% equ 0 (
    sc query MongoDB | find "RUNNING" >nul 2>&1
    if %errorlevel% neq 0 (
        echo       Starting MongoDB service...
        net start MongoDB >nul 2>&1
        if %errorlevel% neq 0 (
            echo [WARNING] Could not start MongoDB service automatically.
            echo Please start MongoDB manually before running the application.
        ) else (
            echo       MongoDB service started!
        )
    ) else (
        echo       MongoDB service is running!
    )
) else (
    echo [WARNING] MongoDB service not found. Make sure MongoDB is running.
)
echo.

:: Create virtual environment
echo [4/6] Creating virtual environment...
if exist venv (
    echo       Virtual environment already exists, skipping creation.
) else (
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo       Virtual environment created!
)
echo.

:: Activate virtual environment and install requirements
echo [5/6] Installing dependencies...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)

pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)
echo       Dependencies installed successfully!
echo.

:: Create .env file if it doesn't exist
echo [6/6] Checking environment configuration...
if not exist .env (
    echo SECRET_KEY=your-super-secret-key-change-in-production> .env
    echo MONGO_URI=mongodb://localhost:27017/finflow>> .env
    echo FLASK_CONFIG=development>> .env
    echo       Created .env file with default configuration.
    echo       [NOTE] Update SECRET_KEY in .env for production use.
) else (
    echo       .env file already exists.
)
echo.

:: Setup complete
echo ============================================================
echo                    Setup Complete!
echo ============================================================
echo.
echo To start the application:
echo   1. Ensure MongoDB is running
echo   2. Run: venv\Scripts\activate
echo   3. Run: python run.py
echo.
echo The application will be available at: http://localhost:5000
echo.
echo ============================================================
pause
