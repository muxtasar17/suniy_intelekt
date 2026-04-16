#!/bin/bash
# 🚀 Quick Start Script - Bot va Web'ni tez boshlash

echo "🤖 AI Quiz - Quick Setup"
echo "========================"
echo ""

# Step 1: Files Check
echo "✅ Step 1: Fayllarni tekshirilmoqda..."
if [ -f "index.html" ] && [ -f "quiz_data.json" ] && [ -f "telegram_bot.py" ]; then
    echo "✓ Barcha fayllar topildi!"
else
    echo "✗ Ba'zi fayllar topilmadi!"
    exit 1
fi
echo ""

# Step 2: Python Check
echo "✅ Step 2: Python tekshirmoqda..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ $PYTHON_VERSION o'rnatilgan"
else
    echo "✗ Python o'rnatilmagan! https://python.org'dan o'rnating"
    exit 1
fi
echo ""

# Step 3: Install Requirements
echo "✅ Step 3: Kutubxonalarni o'rnatilmoqda..."
pip install -r requirements.txt
echo "✓ Kutubxonalar o'rnatildi!"
echo ""

# Step 4: Bot Token
echo "✅ Step 4: Bot Token'ni kiriting"
echo "   BotFather (@BotFather) dan token oling: https://t.me/botfather"
read -p "   TELEGRAM_BOT_TOKEN: " BOT_TOKEN

if [ -z "$BOT_TOKEN" ]; then
    echo "✗ Token kiritilmadi!"
    exit 1
fi
echo ""

# Step 5: Export Token
export TELEGRAM_BOT_TOKEN=$BOT_TOKEN
echo "✓ Token o'rnatildi!"
echo ""

# Step 6: Menu
echo "🎯 Qanday ishga tushurmoqchisiz?"
echo "1. Web Quiz'ni ishga tushurish (localhost:8000)"
echo "2. Telegram Bot'ni ishga tushurish"
echo "3. Ikkalasini ham ishga tushurish"
read -p "Tanlang (1/2/3): " CHOICE

case $CHOICE in
    1)
        echo "🌐 Web Quiz ishga tushurilmoqda..."
        python3 -m http.server 8000
        ;;
    2)
        echo "🤖 Bot ishga tushurilmoqda..."
        python3 telegram_bot.py
        ;;
    3)
        echo "🌐 Web Quiz fonda ishga tushurilmoqda..."
        python3 -m http.server 8000 &
        echo "🤖 Bot ishga tushurilmoqda..."
        python3 telegram_bot.py
        ;;
    *)
        echo "❌ Noto'g'ri tanlov!"
        exit 1
        ;;
esac

echo ""
echo "✅ Tayyor!"
