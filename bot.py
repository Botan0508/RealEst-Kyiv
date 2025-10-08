import telebot
import os
from flask import Flask

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(name)

@app.route('/')
def home():
    return "Bot is running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Бот работает на Render 🚀")

if name == "main":
    import threading
    threading.Thread(target=bot.polling, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
