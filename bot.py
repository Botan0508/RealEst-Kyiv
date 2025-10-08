import os
import threading
from flask import Flask
import telebot

# токен из переменной окружения (Render), если нет — fallback
TOKEN = os.getenv("BOT_TOKEN", "YOUR_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(name)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! Бот работает на Render 🚀")

def run_flask():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

def run_bot():
    bot.infinity_polling()

if name == "main":
    t1 = threading.Thread(target=run_flask)
    t1.start()
    run_bot()
