from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Это команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой виртуальный менеджер 🏙")

# Основная функция запуска бота
def main():
    # 🔸 Сюда вставь свой токен от @BotFather
    app = ApplicationBuilder().token("8280351864:AAFfzR0DtQS06Q0oGdP41sWbMQc6A25ba30").build()

    # Регистрируем команду /start
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
bot.py
main.py
app.py
