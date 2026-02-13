@echo off
REM ============================================================
REM AILAX Setup Script
REM ============================================================
REM This script will:
REM 1. Install all required Python packages from requirements.txt
REM 2. Download the openwakeword models
REM
REM Run this script before using AILAX for the first time.
REM ============================================================

color 0A
title AILAX Setup Script

echo.
echo ============================================================
echo   AILAX Setup Script v1.0
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.7+ and try again.
    echo.
    pause
    exit /b 1
)

echo [INFO] Python found:
python --version
echo.

REM Check if requirements.txt exists
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found!
    echo Please make sure requirements.txt is in the same directory as this script.
    echo.
    pause
    exit /b 1
)

REM Step 1: Install requirements
echo ============================================================
echo   Step 1: Installing Python Packages
echo ============================================================
echo.
echo Installing packages from requirements.txt...
echo.

python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo [WARNING] Package installation failed!
    echo Please check the error messages above.
    echo.
    set /p continue="Do you want to continue anyway? (Y/N): "
    if /i not "%continue%"=="Y" (
        echo Setup cancelled.
        pause
        exit /b 1
    )
) else (
    echo.
    echo [SUCCESS] All packages installed successfully!
)

REM Step 2: Download openwakeword models
echo.
echo ============================================================
echo   Step 2: Downloading OpenWakeWord Models
echo ============================================================
echo.
echo Downloading openwakeword models...
echo.

python -c "from openwakeword.utils import download_models; download_models()"

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to download OpenWakeWord models.
    echo You can try manually running:
    echo   python -c "from openwakeword.utils import download_models; download_models()"
    echo.
) else (
    echo.
    echo [SUCCESS] OpenWakeWord models downloaded successfully!
)

REM Step 3: Summary
echo.
echo ============================================================
echo   Setup Complete!
echo ============================================================
echo.
echo [SUCCESS] All setup steps have been completed.
echo.
echo You can now run AILAX with:
echo   python main.py
echo.
echo Or simply double-click main.py
echo.
echo ============================================================
echo.

pause

