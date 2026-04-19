@echo off
setlocal

echo ==========================================
echo Magdi-AI Installer (Windows)
echo ==========================================

docker info >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Docker Desktop is not running.
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

if not exist ".env" (
    echo Creating .env from .env.example...
    copy .env.example .env >nul
    echo.
    echo WARNING: Please update the .env file with your API keys and settings.
    echo Press any key to continue once ready...
    pause >nul
)

echo.
echo ==========================================
echo Stopping existing Magdi-AI containers...
echo ==========================================
docker compose down >nul 2>&1

echo.
echo ==========================================
echo Starting Magdi-AI...
echo ==========================================
docker compose up -d

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start containers.
    echo Port 3000 may already be in use by another application or container.
    echo Please stop the conflicting service and try again.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo SUCCESS: Magdi-AI is running!
echo Open: http://localhost:3000
echo ==========================================

pause
endlocal