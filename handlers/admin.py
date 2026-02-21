from config import ADMIN_ID, GROUP_CHAT_ID
from database import approve_request, get_request
from telegram.ext import ContextTypes

async def admin_actions(update, context):
    query = update.callback_query
    await query.answer()

    if query.from_user.id != ADMIN_ID:
        return

    action, prayer_id = query.data.split("_")
    prayer_id = int(prayer_id)

    if action == "approve":
        approve_request(prayer_id)
        request = get_request(prayer_id)

        category = request[2]
        message = request[3]

        await context.bot.send_message(
            chat_id=GROUP_CHAT_ID,
            text=f"🙏 Prayer Request\nAnonymous — {category}\n\n{message}"
        )

        await query.edit_message_text("Approved and posted.")

    elif action == "reject":
        await query.edit_message_text("Rejected.")