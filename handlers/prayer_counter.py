from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from database import increment_prayer

async def prayer_counter(update, context):
    query = update.callback_query
    await query.answer()

    prayer_id = int(query.data.split("_")[1])
    count = increment_prayer(prayer_id)

    await query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"I Prayed 🙏 ({count})", callback_data=f"prayed_{prayer_id}")]
        ])
    )