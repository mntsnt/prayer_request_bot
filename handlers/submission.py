from telegram.ext import ContextTypes, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import ADMIN_ID
from database import insert_request

CATEGORY, MESSAGE = range(2)

async def category_selected(update, context):
    query = update.callback_query
    await query.answer()

    context.user_data["category"] = query.data
    await query.message.reply_text("Type your prayer request:")
    return MESSAGE

async def save_message(update, context):
    user_id = update.message.from_user.id
    category = context.user_data["category"]
    message = update.message.text.strip()

    if len(message) < 10:
        await update.message.reply_text("Please write at least 10 characters.")
        return MESSAGE

    prayer_id = insert_request(user_id, category, message)

    keyboard = [
        [
            InlineKeyboardButton("Approve", callback_data=f"approve_{prayer_id}"),
            InlineKeyboardButton("Reject", callback_data=f"reject_{prayer_id}")
        ]
    ]

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"New Prayer Request\n\nCategory: {category}\n\n{message}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    await update.message.reply_text(
        "Your request has been submitted anonymously. 🙏"
    )

    return ConversationHandler.END