from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from database import get_random_request

CATEGORY, MESSAGE = range(2)

async def menu_handler(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "submit":
        keyboard = [
            [InlineKeyboardButton("Health", callback_data="Health")],
            [InlineKeyboardButton("Exams", callback_data="Exams")],
            [InlineKeyboardButton("Family", callback_data="Family")],
            [InlineKeyboardButton("Financial", callback_data="Financial")],
            [InlineKeyboardButton("Spiritual", callback_data="Spiritual")],
        ]
        await query.message.reply_text(
            "Select a category:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return CATEGORY

    elif query.data == "pray":
        request = get_random_request()

        if not request:
            await query.message.reply_text("No approved prayer requests yet.")
            return ConversationHandler.END

        prayer_id = request[0]
        category = request[2]
        message = request[3]
        count = request[5]

        keyboard = [
            [InlineKeyboardButton(f"I Prayed 🙏 ({count})", callback_data=f"prayed_{prayer_id}")]
        ]

        await query.message.reply_text(
            f"🙏 Anonymous — {category}\n\n{message}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

        return ConversationHandler.END