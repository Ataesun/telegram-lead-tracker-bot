import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("7584622126:AAEWINHkA9s1k9bbaEw8yxulc_Df1l2QnHg")
ADMIN_ID = int(os.getenv("1649363870", "0"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    source = context.args[0] if context.args else "неизвестно"
    await update.message.reply_text(f"Привет! Ты пришёл из: {source}")

    # Уведомление админу
    text = f"👤 @{user.username or user.full_name}\n📌 Источник: {source}"
    await context.bot.send_message(chat_id=ADMIN_ID, text=text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен.")
    app.run_polling()
