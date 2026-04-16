# 🤖 AI Quiz - Sun'iy Intellekt Quiz Testi

Bu loyiha sun'iy intellekt bo'yicha **200 ta savolni** o'z ichiga olgan Telegram bot va web quiz platforma hisoblanadi.

## 🎯 Xususiyatlar

✅ **200 ta savol** - Sun'iy intellekt bo'yicha to'liq kurs
✅ **Responsive Design** - Telefonalarda optimal ko'rinish
✅ **Random Tartib** - Har safar boshqacharoq savollar
✅ **Real-time Natija** - Darhol natija bilan feedback
✅ **Telegram Bot** - Botda ham o'ynash imkoniyati
✅ **Statistika** - O'z natijalaringizni kuzatish
✅ **Share Funksiya** - Natijalarni ulashish

---

## 📁 Fayl Tuzilishi

```
suniy intelekt/
├── index.html          # Web quiz (responsive)
├── quiz_data.json      # 200 ta savol-javoblar
├── telegram_bot.py     # Telegram bot kodi
└── README.md          # Bu fayl
```

---

## 🚀 Web Quiz Ishlatish

### 1. Fayllarni Yuklab Olish
```bash
# Ushbu 3 ta fayl kerak:
- index.html
- quiz_data.json
```

### 2. Brauzerdagi Ishlatish
- `index.html` ni brauzerdagi ochish yoki nomuvoziy serverda joylashtirish
- Quiz avtomatik yo'klanaladi va boshlanadi

### 3. Особенности
- **Responsive** - Barcha qurilmalarda ishlaydi (phone, tablet, desktop)
- **Offline** - Internet bilan ishlashadi
- **Shareble** - Telegram, Twitter, Facebook'ga ulashish
- **Fast** - JavaScript bilan local'da ishlaydi

---

## 🤖 Telegram Bot Ishlatish

### 1. Python O'rnatish
```bash
# Python 3.10+ kerak
python --version
```

### 2. Kutubxonalarni O'rnatish
```bash
pip install python-telegram-bot --upgrade
```

### 3. Bot Token Olish
1. Telegram'da [@BotFather](https://t.me/botfather) ga yozing
2. `/newbot` komandasini ishlatib yangi bot yarating
3. Olingan **Token**ni saqlab oling

### 4. Bot Ishga Tushurish
```bash
# Windows'da:
set TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
python telegram_bot.py

# Linux/Mac:
export TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
python telegram_bot.py
```

### 5. Bot Komandalari
```
/start  - Quiz boshlash
/help   - Yordam olish
/stats  - Statistika ko'rsatish
```

---

## 📊 Quiz Tasvifi

### Mavzular:
1. **Sun'iy Intellekt Asoslari** (50-99 savol)
2. **Mashinali O'qitish** (50-99 savol)
3. **Neyron Tarmoqlar** (50-99 savol)
4. **Tabiiy Til Qayta Ishlash** (50-99 savol)

### Qiyinchilik Darajalari:
- 🟢 **Oson** (20%)
- 🟡 **O'rta** (50%)
- 🔴 **Qiyin** (30%)

---

## 🎨 Customization

### Web Quiz'ni Rings O'zgartirish

`index.html` faylida:

**Rang o'zgartirish:**
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* Yangi rangni o'rnating */
```

**Savollar chiqish soni:**
```javascript
shuffledQuestions = shuffle([...quizData]).slice(0, 50);
/* 50 o'rniga boshqa raqam qo'ying */
```

### Bot Sozlamalari

`telegram_bot.py` faylida:

**Savollar chiqish soni:**
```python
return shuffled[:50]  # Birinchi 50 ta savolni tanlash
```

---

## 📈 Natija Tahlili

### Darajalar:

| Foiz | Daraja | Emoji |
|------|--------|-------|
| 100% | Mutaxassis | 🏆 |
| 80-99% | Zo'ravor | ⭐ |
| 60-79% | Yaxshi | 👏 |
| 40-59% | Sinab Ko'ring | 🤔 |
| <40% | O'rganish Kerak | 📚 |

---

## 🌐 Server'ga Joylashtirish

### Replit'da:
1. Replit.com'ga kirib yangi loyiha yarating
2. Fayllarni yuklab oling
3. `index.html' ni Run tugmasi orqali ishlatish
4. Bot'ni terminal'da ishga tushurish

### Vercel'da (Web):
1. GitHub'ga repo yarating
2. Vercel'da ulang
3. Avtomatik deploy bo'ladi

### Heroku'da (Bot):
1. Heroku accounti yarating
2. `Procfile` fayl yarating:
```
worker: python telegram_bot.py
```
3. Deploy qiling

---

## 🔧 Xatoliklarni Yechish

### "Quiz ma'lumotlarini yuklab olishda xatolik"
- `quiz_data.json` fayli `index.html` bilan bir joyda ekanligini tekshiring
- Fayl nomini to'g'ri kiriting

### Bot javob bermayapti
- Token to'g'ri ekanligini tekshiring
- `python-telegram-bot` kutubxonasi o'rnatilganligini tekshiring
- Bot Father'dan token-ni yangilang

### Web Quiz telefonada yomon ko'rinishda
- Browser'ni refresh qiling (F5)
- Kesh tozalang
- Boshqa browser ishlatib ko'ring

---

## 📝 Savollarni Qo'shish

New savollarni JSON'da qo'shish uchun `quiz_data.json` faylini edit qiling:

```json
{
  "id": 201,
  "question": "Yangi savol?",
  "options": [
    "Javob 1",
    "Javob 2",
    "Javob 3",
    "Javob 4"
  ],
  "correct": 0
}
```

"correct" = to'g'ri javob indexi (0, 1, 2, yoki 3)

---

## 📢 Kontakt

- 📧 Email: yourmail@gmail.com
- 👤 Telegram: @yourtelegram
- 🐙 GitHub: github.com/yourname

---

## ⚖️ Litsenziya

MIT License - Erkin foydalanish!

---

## 🎓 O'rganish Manbalari

- [Python Telegram Bot Docs](https://python-telegram-bot.readthedocs.io/)
- [HTML/CSS Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [JavaScript JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

---

**Yaratilgan:** 2026-yil
**Versiya:** 1.0.0
**Status:** ✅ Yashil
