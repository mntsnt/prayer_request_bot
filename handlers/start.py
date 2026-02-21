from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Submit Prayer Request", callback_data="submit")],
        [InlineKeyboardButton("Pray for Someone", callback_data="pray")]
    ]
    await update.message.reply_text(
        "Welcome 🙏\n\nSubmit your prayer requests anonymously and let others pray for you.\n\n“Therefore confess your sins to each other and pray for each other so that you may be healed. The prayer of a righteous person is powerful and effective.”\n\n — James 5:16\n\nYour identity will never be shared publicly.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    