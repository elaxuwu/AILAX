@echo off
REM ============================================================
REM AILAX Setup Script
REM ============================================================
REM This script will:
REM 1. Check if Ollama is installed
REM 2. Pull required Ollama models
REM 3. Install all required Python packages from requirements.txt
REM 4. Download the openwakeword models
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

REM Check if Ollama is installed
echo [INFO] Checking for Ollama installation...
ollama --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Ollama is not installed or not in PATH!
    echo.
    echo Please install Ollama first:
    echo   1. Visit https://ollama.com/download
    echo   2. Download and install Ollama for Windows
    echo   3. Run this setup script again
    echo.
    pause
    exit /b 1
)

echo [SUCCESS] Ollama is installed:
ollama --version
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

REM Step 1: Pull Ollama models
echo ============================================================
echo   Step 1: Pulling Ollama AI Models
echo ============================================================
echo.
echo This may take a while depending on your internet connection...
echo.
echo Pulling qwen3-vl:235b-instruct-cloud (General mode model)...
ollama pull qwen3-vl:235b-instruct-cloud

if errorlevel 1 (
    echo.
    echo [WARNING] Failed to pull qwen3-vl:235b-instruct-cloud
    echo You may need to pull it manually later:
    echo   ollama pull qwen3-vl:235b-instruct-cloud
    echo.
) else (
    echo [SUCCESS] qwen3-vl:235b-instruct-cloud pulled successfully!
)

echo.
echo Pulling qwen3-coder-next:cloud (Coding mode model)...
ollama pull qwen3-coder-next:cloud

if errorlevel 1 (
    echo.
    echo [WARNING] Failed to pull qwen3-coder-next:cloud
    echo You may need to pull it manually later:
    echo   ollama pull qwen3-coder-next:cloud
    echo.
) else (
    echo [SUCCESS] qwen3-coder-next:cloud pulled successfully!
)

REM Step 2: Install requirements
echo ============================================================
echo   Step 2: Installing Python Packages
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

REM Step 3: Download openwakeword models
echo.
echo ============================================================
echo   Step 3: Downloading OpenWakeWord Models
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

REM Step 4: Summary
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

