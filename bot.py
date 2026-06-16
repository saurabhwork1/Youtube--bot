import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot Started")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Link received ✅"
    )


def main():

    print("BOT STARTED")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT,
            message
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()