import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from attendance import checkin, checkout
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8961677036:AAFYAxV27GAvOumg9wN-1v994MhOtNlGtW8")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 DaDing Bot Ready")


async def cmd_checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    checkin(user_id)
    await update.message.reply_text("✅ Check In Success")


async def cmd_checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    checkout(user_id)
    await update.message.reply_text("✅ Check Out Success")


def run():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("checkin", cmd_checkin))
    app.add_handler(CommandHandler("checkout", cmd_checkout))

    app.run_polling()