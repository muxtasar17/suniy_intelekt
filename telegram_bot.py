#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 AI Quiz Bot - Telegram Bot
Sun'iy Intellekt bo'yicha Quiz testini Telegram da o'ynang
"""

import json
import random
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Quiz ma'lumotlarini topish
QUIZ_DATA_PATH = "quiz_data.json"

# Emoji'lar
EMOJI = {
    'robot': '🤖',
    'quiz': '📝',
    'score': '🏆',
    'start': '▶️',
    'next': '⏭️',
    'result': '📊',
    'telegram': '📱',
    'fire': '🔥',
    'star': '⭐',
    'perfect': '🎉',
    'good': '👏',
    'ok': '😊',
    'sad': '😢',
    'book': '📚',
    'time': '⏱️'
}

def load_quiz_data():
    """Quiz ma'lumotlarini JSON fayldan o'qish"""
    try:
        with open(QUIZ_DATA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['quizzes']
    except FileNotFoundError:
        return []

def shuffle_questions(questions):
    """Savollarni random tartiblashda"""
    shuffled = questions.copy()
    random.shuffle(shuffled)
    return shuffled[:50]  # Birinchi 50 ta savolni tanlash

def shuffle_options(options, correct_index):
    """Javoblarni random tartiblash va to'g'ri javob indexini qaytarish"""
    options_with_index = [(opt, i == correct_index) for i, opt in enumerate(options)]
    random.shuffle(options_with_index)
    
    shuffled_options = [opt for opt, _ in options_with_index]
    new_correct_index = next(i for i, (_, is_correct) in enumerate(options_with_index) if is_correct)
    
    return shuffled_options, new_correct_index

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Quiz ni boshlash"""
    user_data = context.user_data
    
    quiz_data = load_quiz_data()
    if not quiz_data:
        await update.message.reply_text(f"{EMOJI['sad']} Quiz ma'lumotlarini yuklab olishda xatolik!")
        return
    
    user_data['questions'] = shuffle_questions(quiz_data)
    user_data['current_question'] = 0
    user_data['score'] = 0
    user_data['answers'] = []
    user_data['start_time'] = datetime.now()
    
    await show_question(update, context)

async def show_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Savolni ko'rsatish"""
    user_data = context.user_data
    
    if 'questions' not in user_data:
        await update.message.reply_text(f"{EMOJI['robot']} Avval /start komandasini bosing!")
        return
    
    current_idx = user_data['current_question']
    questions = user_data['questions']
    
    if current_idx >= len(questions):
        await show_results(update, context)
        return
    
    question = questions[current_idx]
    options, correct_index = shuffle_options(question['options'], question['correct'])
    
    # Qoshimcha ma'lumotlar saqlab olish (to'g'ri javob indexi)
    user_data['current_correct_index'] = correct_index
    user_data['current_options'] = options
    
    # Savol matni
    progress = f"({current_idx + 1}/{len(questions)})"
    question_text = f"{EMOJI['quiz']} <b>Savol {progress}</b>\n\n{question['question']}"
    
    # Tugmalar
    keyboard = []
    for i, option in enumerate(options):
        button = InlineKeyboardButton(
            f"{'✓ ' if i == correct_index else ''}{option}",
            callback_data=f"answer_{i}"
        )
        keyboard.append([button])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.callback_query:
        await update.callback_query.edit_text(question_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        await update.message.reply_text(question_text, reply_markup=reply_markup, parse_mode='HTML')

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Javob tanlandi"""
    query = update.callback_query
    user_data = context.user_data
    
    await query.answer()
    
    selected_index = int(query.data.split('_')[1])
    correct_index = user_data.get('current_correct_index', -1)
    
    # Javobni saqlab olish
    is_correct = selected_index == correct_index
    if is_correct:
        user_data['score'] += 1
    
    user_data['answers'].append({
        'question': user_data['questions'][user_data['current_question']]['question'],
        'selected': user_data['current_options'][selected_index],
        'correct': user_data['questions'][user_data['current_question']]['options'][correct_index],
        'is_correct': is_correct
    })
    
    # Cavobning to'g'risini ko'rsatish
    response_text = f"{'✓ To\'g\'ri!' if is_correct else '✗ Noto\'g\'ri!'}\n"
    response_text += f"<b>To'g'ri javob:</b> {user_data['questions'][user_data['current_question']]['options'][correct_index]}"
    
    await query.edit_text(response_text, parse_mode='HTML')
    
    # Keyingi savolni ko'rsatish
    keyboard = [[InlineKeyboardButton("Keyingi →", callback_data="next_question")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text("Keyingi savolga bosing:", reply_markup=reply_markup)

async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Keyingi savolga o'tish"""
    user_data = context.user_data
    user_data['current_question'] += 1
    
    await show_question(update, context)

async def show_results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Natijalarni ko'rsatish"""
    user_data = context.user_data
    
    total_questions = len(user_data['questions'])
    score = user_data['score']
    percentage = (score / total_questions) * 100
    
    # Vaqt hisoblash
    start_time = user_data.get('start_time', datetime.now())
    time_spent = (datetime.now() - start_time).seconds
    
    # Xabar
    if percentage == 100:
        message = f"{EMOJI['perfect']} <b>JUD AJOYIB!</b>\nSiz javoblarning barchasiga to'g'ri javob berdingiz!\n"
        emoji_result = f"{EMOJI['perfect']}"
    elif percentage >= 80:
        message = f"{EMOJI['star']} <b>ZORAVOR!</b>\nSiz AI bo'yicha yaxshi bilimga egasiz!\n"
        emoji_result = f"{EMOJI['star']}"
    elif percentage >= 60:
        message = f"{EMOJI['ok']} <b>YAXSHI!</b>\nYana oz o'rganib chiqmoqchi bo'ling.\n"
        emoji_result = f"{EMOJI['ok']}"
    elif percentage >= 40:
        message = f"{EMOJI['book']} <b>SINAB KO'RING!</b>\nMavzuni yana o'qib chiqishga harakat qiling.\n"
        emoji_result = f"{EMOJI['book']}"
    else:
        message = f"{EMOJI['sad']} <b>USHBU MAVZUNI CHUQUR O'RGANISH KERAK!</b>\nHarakat qiling!\n"
        emoji_result = f"{EMOJI['sad']}"
    
    result_text = f"""
{emoji_result} <b>NATIJA</b> {emoji_result}

<b>Natija:</b> {percentage:.1f}%
<b>To'g'ri:</b> {score}/{total_questions}
<b>Noto'g'ri:</b> {total_questions - score}/{total_questions}
<b>Vaqt:</b> {time_spent} soniya

{message}

🔄 <b>/start</b> - Qayta boshlash
📊 <b>/stats</b> - Statistika ko'rsatish
"""
    
    keyboard = [
        [InlineKeyboardButton("🔄 Qayta Boshlash", callback_data="restart")],
        [InlineKeyboardButton("📤 Telegram Kanalida Ulashish", url="https://t.me/share/url?url=https://yoursite.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_text(result_text, reply_markup=reply_markup, parse_mode='HTML')

async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Qayta boshlash"""
    await start(update, context)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Yordam"""
    help_text = f"""
{EMOJI['robot']} <b>AI QUIZ BOT</b>

<b>Qanday ishlatish:</b>
1. /start - Quiz-ni boshlash
2. Savollarni javob berish
3. Natijalarni ko'rish

<b>Komandalemr:</b>
/start - Quiz boshlash
/help - Bu xbari ko'rsatish
/stats - Shaxsiy statistika

{EMOJI['quiz']} <b>200 ta savol!</b>
{EMOJI['rocket']} <b>Random tartibda!</b>
{EMOJI['score']} <b>Real-time natija!</b>

<b>Qiziqarli bo'lmaydimi?</b>
👉 @yourbot ni qo'shimcha sozlamalar uchun bosing!
"""
    await update.message.reply_text(help_text, parse_mode='HTML')

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Statistika"""
    user_data = context.user_data
    
    if 'score' not in user_data:
        await update.message.reply_text(f"{EMOJI['sad']} Siz hali quiz o'ynamamadingiz!")
        return
    
    total = len(user_data['questions'])
    score = user_data['score']
    percentage = (score / total) * 100
    
    stats_text = f"""
{EMOJI['result']} <b>SIZNING STATISTIKANGIZ</b>

<b>Jami natija:</b> {percentage:.1f}%
<b>To'g'ri javoblar:</b> {score}/{total}
<b>Noto'g'ri javoblar:</b> {total - score}/{total}

<b>Daraja:</b>
{'⭐⭐⭐ Mutaxassis' if percentage >= 90 else '⭐⭐ Yaxshi' if percentage >= 70 else '⭐ Boshlang\'ich'}
"""
    await update.message.reply_text(stats_text, parse_mode='HTML')

def main():
    """Bot ishga tushurish"""
    # Token o'rnatish (environment variabldan yoki to'g'ridan-to'g'ri)
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
    
    if TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ Iltimos, TELEGRAM_BOT_TOKEN environment variable'ni o'rnating!")
        return
    
    # Application yaratish
    app = Application.builder().token(TOKEN).build()
    
    # Handlerlar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CallbackQueryHandler(answer, pattern="^answer_"))
    app.add_handler(CallbackQueryHandler(next_question, pattern="^next_question$"))
    app.add_handler(CallbackQueryHandler(restart, pattern="^restart$"))
    
    # Bot ishga tushurish
    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
