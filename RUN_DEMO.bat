@echo off
setlocal
cd /d "%~dp0"
echo Installing the lightweight EpiScope demo dependencies...
py -m pip install -r requirements-demo.txt
if errorlevel 1 (
  echo.
  echo Setup failed. Install Python 3.11 or 3.12 from python.org, then run this file again.
  pause
  exit /b 1
)
set EPISCOPE_HASH_SALT=local-demo-only-change-before-real-use
echo.
echo Building the synthetic demo data and dashboard export...
py run.py --scale 0.001 --seed 2026
if errorlevel 1 (
  echo.
  echo The pipeline failed. Copy the error text and send it for troubleshooting.
  pause
  exit /b 1
)
echo.
echo Starting the dashboard at http://localhost:8080
echo Keep this window open while using the dashboard.
py -m http.server 8080 --directory dashboard
