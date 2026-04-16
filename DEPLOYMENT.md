# 🚀 Deployment Guide - Bot va Web'ni Deploy Qilish

## 1️⃣ WEB QUIZ'NI DEPLOY QILISH

### Variant A: GitHub Pages (Bepul + Simple)

1. **Git o'rnatish** (agar o'rnatilmagan bo'lsa)
   ```bash
   # GitHub Desktop yoki git CLI'dan foydalaning
   ```

2. **GitHub reposini yaratish**
   - github.com ga kirib yangi repo yarating
   - Repo nomi: `ai-quiz`
   - Public tanlang

3. **Fayllarni yuklash**
   ```bash
   # Terminal'da
   git clone https://github.com/YOURNAME/ai-quiz.git
   cd ai-quiz
   
   # index.html va quiz_data.json'ni qo'ying
   
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

4. **GitHub Pages'ni yoqish**
   - Repo settings ga kirib
   - Pages bo'limiga o'tib
   - Main branch'ni tanlang
   - Save qiling
   - 5 minut kutib, link olish: `https://YOURNAME.github.io/ai-quiz`

---

### Variant B: Netlify (Eng Oson)

1. **Netlify'ga kirib signup qiling**
   - netlify.com ga o'ting
   - GitHub account bilan login qiling

2. **New site yaratish**
   - "Add new site" tugmasini bosing
   - GitHub repo'ni tanlang
   - Deploy qiling (avtomatik!)
   - Link olish: `https://random-name.netlify.app`

3. **Auto Deploy**
   - GitHub'ga push qil
   - Netlify avtomatik deploy qiladi

---

### Variant C: Vercel (Premium Option)

1. **Vercel'ga signup**
   - vercel.com ga o'ting
   - GitHub bilan login

2. **Import project**
   - GitHub repo'ni tanlang
   - Deploy qiling
   - Custom domain ulang opsional

---

## 2️⃣ TELEGRAM BOT'NI DEPLOY QILISH

### Variant A: Heroku (Oson, Cloud Server)

1. **Heroku accounti yaratish**
   - heroku.com ga o'ting
   - Email va parol orqali register

2. **Heroku CLI o'rnatish**
   ```bash
   # Windows:
   chocolatey install heroku-cli
   
   # Mac:
   brew tap heroku/brew && brew install heroku
   
   # Linux:
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

3. **Heroku'ga login**
   ```bash
   heroku login
   ```

4. **Deployment setup**
   ```bash
   # Bot katalogiga o'tish
   cd suniy\ intelekt
   
   # Git repo'ni initialize qilish
   git init
   git add .
   git commit -m "Initial commit"
   
   # Heroku app yaratish
   heroku create ai-quiz-bot
   
   # Environment variable o'rnating
   heroku config:set TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
   
   # Deploy qilish
   git push heroku main
   ```

5. **Procfile yaratish** (kerak!)
   ```
   worker: python telegram_bot.py
   ```
   
6. **Dyno'ni yoqish**
   ```bash
   heroku ps:scale worker=1
   ```

---

### Variant B: Railway (Yangi va Oson)

1. **Railway'ga signup**
   - railway.app ga o'ting
   - GitHub bilan login

2. **New project**
   - GitHub repo'ni ulang
   - Environment variables o'rnating
   - Deploy qiling

---

### Variant C: PythonAnywhere (Pul bilan, Stable)

1. **PythonAnywhere'ga signup**
   - pythonanywhere.com

2. **Bot upload qilish**
   - Fayllarni upload qiling
   - Bot'ni Web tab'da ishga tushuring

---

## 3️⃣ LOCAL'DA TESTING QILISH

### Web Quiz

```bash
# Python simple server ishga tushurish
python -m http.server 8000

# Brauzerdagi www.localhost:8000
```

### Bot

```bash
# Token o'rnating
set TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE  # Windows
export TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE  # Linux/Mac

# Kutubxonalarni o'rnatish
pip install -r requirements.txt

# Bot'ni ishga tushurish
python telegram_bot.py
```

---

## 4️⃣ CUSTOM DOMAIN ULASH

### GoDaddy/Namecheap'dan domain sotib olish

1. Domain tanlang va sotib oling
2. DNS settings'ga o'tib
3. Netlify/Vercel'da ko'rsatilgan records'ni qo'ying
4. 24 soat kutib, custom domain'ni ishlatish

---

## 5️⃣ TELEGRAM BOT REKLAMA QILISH

1. **BotList'larda roʻyxatga olish**
   - botlist.me
   - botsarchive.com
   - storebot.me

2. **Telegram Channel'larda e'lon**
   - @botlist_uz
   - @uzbot
   - @uzpython_chat

3. **Social Media'da Share**
   - Instagram
   - Twitter/X
   - Facebook

---

## 6️⃣ DEBUGGING

### Web Issues
```javascript
// Browser console'ni oching (F12)
// Errors ko'rsatiladi
```

### Bot Issues
```bash
# Verbose logging
python -c "import logging; logging.basicConfig(level=logging.DEBUG)" telegram_bot.py
```

---

## 📊 Performance Tips

### Web
- Image optimization
- CSS minification
- JavaScript bundling
- CDN/Caching

### Bot
- Message queuing
- Error handling
- Rate limiting
- Database caching

---

## 🔒 Security

### Environment Variables
- Token'larni `.env` faylda saqlang
- `.gitignore` ga qo'ying
- Qayta rotate qiling har 3 oyda

### API Keys
- Public deploy'larida rahasia datas bo'lmaydi
- Backend server'da xavfsiz saqlang

---

## 📞 Support

Muammo bo'lsa:
- Stack Overflow'da savolish
- GitHub Issues'da ticket ochish
- Telegram support gruppasiga yozish

---

**Yurifiy salom! Bot va Web'ingiz deploy qilindi! 🎉**
