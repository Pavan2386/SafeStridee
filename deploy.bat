@echo off
echo ========================================
echo SafeStride Deployment Validation
echo ========================================

echo.
echo Checking Python version...
"C:\Users\Pavan\AppData\Local\Programs\Python\Python311\python.exe" --version

echo.
echo Checking dependencies...
"C:\Users\Pavan\AppData\Local\Programs\Python\Python311\python.exe" check_dependencies.py

if errorlevel 1 (
    echo Dependency validation failed.
    exit /b 1
)

echo.
echo Running automated tests...
"C:\Users\Pavan\AppData\Local\Programs\Python\Python311\python.exe" -m pytest

if errorlevel 1 (
    echo Tests failed.
    exit /b 1
)

echo.
echo ========================================
echo Deployment validation successful.
echo ========================================
exit /b 0