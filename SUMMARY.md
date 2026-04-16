# 🎉 AI QUIZ PROJECT - YAKUNIY SUMMARY

## ✅ Yaratilgan Fayllar

### 1. 📝 **index.html** (17.9 KB)
**Nima?** Responsive web quiz sayt
**Xususiyatlar:**
- ✨ Zamonaviy UI/UX design
- 📱 Mobile-friendly (iPhone, Android va PC'da)
- 🎨 Gradient background va smooth animations
- 🚀 JavaScript orqali local'da ishlaydi (offline)
- 📊 Real-time progress bar
- 🏆 Natija Ko'rsatish
- 📤 Telegram/Twitter/Facebook share

**Qanday Ishlatish?**
```bash
# 1. Brauzerdagi o'tish
http://localhost:8000

# 2. Faylni direct o'tish
C:\Users\Muhiddin\Desktop\suniy intelekt\index.html
```

---

### 2. 📚 **quiz_data.json** (43.2 KB)
**Nima?** 200 ta sun'iy intellekt bo'yicha savol-javob
**Struktura:**
```json
{
  "id": 1,
  "question": "Savol?",
  "options": ["A", "B", "C", "D"],
  "correct": 0
}
```
**Mavzular:**
- Sun'iy Intellekt Asoslari (25 ta)
- Mashinali O'qitish (50 ta)
- Neyron Tarmoqlar (50 ta)
- Tabiiy Til Qayta Ishlash (50 ta)
- Kompyuter Ko'rish (25 ta)

---

### 3. 🤖 **telegram_bot.py** (10.1 KB)
**Nima?** Telegram Bot kodi
**Komandalari:**
```
/start  - Quiz boshlash
/help   - Yordam
/stats  - Statistika
```

**Xususiyatlar:**
- 🎯 Inline buttons orqali Javob berish
- 📊 Live natija ko'rsatish
- 💾 User data saqlab olish
- ⏱️ Vaqt o'lchash
- 📈 Statistika

**O'rnatish va Ishlatish:**
```bash
# 1. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 2. Bot Token o'rnating
set TELEGRAM_BOT_TOKEN=YOUR_TOKEN

# 3. Bot ishga tushurish
python telegram_bot.py

# 4. Telegram'da @BotFather orqali bot yarating
# 5. Token olip o'rnating
# 6. @yourbot'ni Telegram'da toping va /start bosing
```

---

### 4. 📖 **README.md** (5.1 KB)
Full dokumentasiya:
- 🎯 Xususiyatlar
- 📁 Fayl tuzilishi
- 🚀 Web quiz ishlatish
- 🤖 Bot ishlatish
- 📊 Quiz tasvifi
- 🎨 Customization
- 🔧 Xatoliklarni yechish

---

### 5. 🚀 **DEPLOYMENT.md** (5.0 KB)
Deploy qilish bo'yicha to'liq guide:

**Web Deploy Sitlari:**
- GitHub Pages (Bepul)
- Netlify (Oson)
- Vercel (Premium)

**Bot Deploy Sitlari:**
- Heroku (Cloud Server)
- Railway (Yangi)
- PythonAnywhere (Paid)

---

### 6. 📋 **requirements.txt** (45 B)
Python kutubxonalari:
```
python-telegram-bot==20.5
requests==2.31.0
```

**O'rnatish:**
```bash
pip install -r requirements.txt
```

---

### 7. 🔧 **run.sh** (1.9 KB)
Linux/Mac uchun quick start script

**Ishlatish:**
```bash
chmod +x run.sh
./run.sh
```

---

### 8. 🔧 **run.bat** (2.2 KB)
Windows uchun quick start script

**Ishlatish:**
```cmd
run.bat
```

---

## 🎯 QUICK START GUIDE

### Web Quiz'ni Ishlatish (5 minut)

**1-qadam:** Fayllarni yuklab oling
```
- Desktop\suniy intelekt\index.html
- Desktop\suniy intelekt\quiz_data.json
```

**2-qadam:** Brauzerdagi o'tish
```
http://localhost:8000
# Yoki Excel'da double-click
```

**3-qadam:** Quiz boshlang!
- Savollarga javob bering
- Random tartiblashda (har safar boshqacharoq)
- Natijalarni ulashing (Telegram/Twitter/Facebook)

---

### Bot'ni Ishlatish (10 minut)

**1-qadam:** BotFather'dan bot yaratish
```
1. Telegram'da @BotFather'ga yozing
2. /newbot komandasini bosing
3. Bot nomi kiriting
4. Username kiriting (@...)
5. Token olip saqlab oling
```

**2-qadam:** Token o'rnating
```bash
# Windows:
set TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE

# Linux/Mac:
export TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
```

**3-qadam:** Bot ishga tushurish
```bash
# Option 1: Quick script
run.bat  # Windows
./run.sh # Linux/Mac

# Option 2: Manual
python telegram_bot.py
```

**4-qadam:** Telegram'da @yourbot'ni toping
```
/start - Quiz boshlash
/help - Yordam
/stats - Statistika
```

---

## 📊 QUIZ STATISTIKASI

| Parametr | Qiymat |
|----------|--------|
| **Jami Savol** | 200 ta |
| **Davomiyligi** | ~50-100 minut |
| **Qiyinchilik** | O'rta |
| **Mavzular** | 5 ta |
| **Javob Variantlari** | 4 ta |

---

## 🌐 DEPLOY QILISH (OPTIONAL)

### Web Sitni Deploy Qilish (GitHub Pages - Bepul)

```bash
# 1. GitHub'ga kirib yangi repo yarating
# 2. Fayllarni yuklab oling
git clone https://github.com/YOUR_USERNAME/ai-quiz.git
cd ai-quiz

# 3. Fayllarni qo'ying
# ... index.html, quiz_data.json'ni qo'ying ...

# 4. Push qiling
git add .
git commit -m "Initial commit"
git push origin main

# 5. GitHub Settings → Pages → Deploy (Main)
# 6. Link: https://YOUR_USERNAME.github.io/ai-quiz
```

### Bot'ni Deploy Qilish (Heroku - Cloud)

```bash
# 1. Heroku'dan signup qiling
# 2. CLI o'rnating: heroku.com/cli
# 3. Token o'rnating
heroku config:set TELEGRAM_BOT_TOKEN=YOUR_TOKEN

# 4. Deploy
git push heroku main

# 5. https://dashboard.heroku.com'da monitor qiling
```

---

## 🎨 CUSTOMIZATION

### Rang O'zgartirish
`index.html` faylida 32-qatorni o'zgartiring:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Yangi rangni o'rnating */
```

### Savollar Chiqish Soni
`index.html` faylida 290-qatorni o'zgartiring:
```javascript
shuffledQuestions = shuffle([...quizData]).slice(0, 50);
/* 50 o'rniga boshqa raqam qo'ying (99 hammasi) */
```

### Yeni Savol Qo'shish
`quiz_data.json'ga yangi object qo'ying:
```json
{
  "id": 201,
  "question": "Yangi savol?",
  "options": ["A", "B", "C", "D"],
  "correct": 0
}
```

---

## 🔒 SECURITY TIPS

1. ✅ Bot Token'ni public'da ekmang
2. ✅ `.gitignore` ga `.env' qo'ying
3. ✅ Environment variables ishlatib Token saqlab oling
4. ✅ Token'larni har 3 oyda rotate qiling

---

## 📞 SUPPORT VA DEBUGGING

### Web Issues
```
1. Browser console'ni oching (F12)
2. Errors ko'rish
3. JavaScript console'da test qiling
```

### Bot Issues
```bash
# Debugging
python telegram_bot.py --debug

# Check Token
echo %TELEGRAM_BOT_TOKEN%  # Windows
echo $TELEGRAM_BOT_TOKEN   # Linux/Mac
```

---

## 📈 NEXT STEPS (Ixtiyoriy)

- ✨ Database ulang (MongoDB/PostgreSQL)
- 🎯 Leaderboard yaratish
- 🔐 User accounts qo'shish
- 📧 Email notifications
- 🌍 Multi-language support
- 📱 Mobile App (Flutter/React Native)

---

## 📝 LICENSE

MIT License - Erki foydalanish va o'zgartirish

---

## 👨‍💻 DEVELOPER INFO

**Project Nam:** AI Quiz Test
**Version:** 1.0.0
**Created:** 2026
**Status:** ✅ Active
**Files:** 8 ta
**Total Size:** ~85 KB

---

## 🎓 O'RGANISH RESURSLARI

- 📖 [Python Docs](https://python.org/docs)
- 📖 [Telegram Bot API](https://core.telegram.org/bots/api)
- 📖 [HTML/CSS](https://html.com)
- 📖 [JavaScript](https://javascript.info)

---

## ✨ OXIRGI SO'Z

Tabriklayman! Siz hozir **to'liq ishchi AI Quiz platformasiga** egaisiz! 🎉

**Web Quiz** telefonalarda optimal, **Telegram Bot** esa real-time interactive.

Har ikkalasini ham deploy qilsa, mahalliy foydalanuvchilar yoki to'liq dunyo qayta o'yna oladi!

**Happy Quizzing! 🚀**

---

*Yaratilgan: 2026-yil
Ushbu loyiha MIT License ostida erkindan foydalanish mumkin.*
