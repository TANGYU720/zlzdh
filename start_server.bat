@echo off
chcp 65001 >nul
title Django Development Server
cd /d "d:\TRAE\TRAR_TEST\QYGW"

echo ================================
echo    企业官网开发服务器启动器
echo ================================
echo.

set "VENV_PYTHON=d:\TRAE\TRAR_TEST\QYGW\.venv\Scripts\python.exe"
set "MANAGE_PY=d:\TRAE\TRAR_TEST\QYGW\qygw_website\manage.py"

echo 检查虚拟环境Python...
if not exist "%VENV_PYTHON%" (
    echo ERROR: 虚拟环境不存在!
    pause
    exit /b 1
)

echo 检查端口占用...
netstat -ano | findstr ":8000" >nul
if %errorlevel% equ 0 (
    echo WARNING: 端口 8000 可能被占用
    echo 尝试终止占用进程...
    for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":8000"') do (
        taskkill /F /PID %%a >nul 2>&1
    )
    echo 端口已释放
)

echo.
echo = 启动Django后端服务 =
echo 访问地址: http://127.0.0.1:8000/
echo 管理后台: http://127.0.0.1:8000/admin/
echo.
echo 按 Ctrl+C 停止服务器
echo ================================
echo.

"%VENV_PYTHON%" "%MANAGE_PY%" runserver 127.0.0.1:8000

echo.
echo 服务器已停止
pause
