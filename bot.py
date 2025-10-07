from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой виртуальный менеджер по недвижимости!")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен и ожидает команды...")
    app.run_polling()

if name == "main":
    main()



