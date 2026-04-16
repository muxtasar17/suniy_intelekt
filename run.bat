@echo off
REM 🚀 Quick Start Script - Windows

echo 🤖 AI Quiz - Quick Setup
echo ========================
echo.

REM Step 1: Files Check
echo ✅ Step 1: Fayllarni tekshirmoqda...
if exist "index.html" (
    if exist "quiz_data.json" (
        if exist "telegram_bot.py" (
            echo ✓ Barcha fayllar topildi!
        ) else (
            echo ✗ telegram_bot.py topilmadi!
            exit /b 1
        )
    ) else (
        echo ✗ quiz_data.json topilmadi!
        exit /b 1
    )
) else (
    echo ✗ index.html topilmadi!
    exit /b 1
)
echo.

REM Step 2: Python Check
echo ✅ Step 2: Python tekshirmoqda...
python --version >nul 2>&1
if %errorlevel%==0 (
    for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
    echo ✓ !PYTHON_VERSION! o'rnatilgan
) else (
    echo ✗ Python o'rnatilmagan! https://python.org'dan o'rnating
    exit /b 1
)
echo.

REM Step 3: Install Requirements
echo ✅ Step 3: Kutubxonalarni o'rnatilmoqda...
pip install -r requirements.txt
if %errorlevel%==0 (
    echo ✓ Kutubxonalar o'rnatildi!
) else (
    echo ✗ Kutubxonalarni o'rnatishda xatolik!
    exit /b 1
)
echo.

REM Step 4: Bot Token
echo ✅ Step 4: Bot Token'ni kiriting
echo    BotFather (@BotFather) dan token oling: https://t.me/botfather
set /p BOT_TOKEN="    TELEGRAM_BOT_TOKEN: "

if "%BOT_TOKEN%"=="" (
    echo ✗ Token kiritilmadi!
    exit /b 1
)
echo.

REM Step 5: Export Token
set TELEGRAM_BOT_TOKEN=%BOT_TOKEN%
echo ✓ Token o'rnatildi!
echo.

REM Step 6: Menu
echo 🎯 Qanday ishga tushurmoqchisiz?
echo 1. Web Quiz'ni ishga tushurish (localhost:8000)
echo 2. Telegram Bot'ni ishga tushurish
echo 3. Ikkalasini ham ishga tushurish
set /p CHOICE="Tanlang (1/2/3): "

if "%CHOICE%"=="1" (
    echo 🌐 Web Quiz ishga tushurilmoqda...
    python -m http.server 8000
) else if "%CHOICE%"=="2" (
    echo 🤖 Bot ishga tushurilmoqda...
    python telegram_bot.py
) else if "%CHOICE%"=="3" (
    echo 🌐 Web Quiz fonda ishga tushurilmoqda...
    start python -m http.server 8000
    echo 🤖 Bot ishga tushurilmoqda...
    python telegram_bot.py
) else (
    echo ❌ Noto'g'ri tanlov!
    exit /b 1
)

echo.
echo ✅ Tayyor!
pause
