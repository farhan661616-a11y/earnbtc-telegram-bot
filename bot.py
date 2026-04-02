from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8635225417:AAEjiMEq9Q2LXeN7a0bq8om32lVmELA3cBI"
APP_URL = "https://magenta-narwhal-50c884.netlify.app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """/start - Button ke saath link"""
    
    keyboard = [[InlineKeyboardButton(
        text="🚀 OPEN MINI APP 🚀",
        url=APP_URL  # Direct link
    )]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👇 Click below to open EarnBTC Mini App:",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()