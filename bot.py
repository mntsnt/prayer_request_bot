from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    filters
)

from config import BOT_TOKEN
from database import init_db

from handlers.start import start
from handlers.menu import menu_handler, CATEGORY, MESSAGE
from handlers.submission import category_selected, save_message
from handlers.admin import admin_actions
from handlers.prayer_counter import prayer_counter

def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(menu_handler, pattern="^(submit|pray)$")],
        states={
            CATEGORY: [CallbackQueryHandler(category_selected)],
            MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_message)],
        },
        fallbacks=[]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(CallbackQueryHandler(admin_actions, pattern="^(approve|reject)_"))
    app.add_handler(CallbackQueryHandler(prayer_counter, pattern="^prayed_"))

    app.run_polling()

if __name__ == "__main__":
    main()