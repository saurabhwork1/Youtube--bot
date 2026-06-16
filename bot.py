import os
import logging
import traceback

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


from config import BOT_TOKEN
from downloader import download_video



logging.basicConfig(
    level=logging.INFO
)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 YouTube Downloader Bot\n\n"
        "Send YouTube link and I will download it."
    )




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = update.message.text


    if "youtube.com" not in url and "youtu.be" not in url:

        await update.message.reply_text(
            "❌ Valid YouTube link bhejo"
        )
        return


    msg = await update.message.reply_text(
        "⏳ Download start..."
    )


    try:

        file = download_video(url)


        await msg.edit_text(
            "📤 Uploading..."
        )


        await update.message.reply_document(
            document=open(file,"rb"),
            caption="✅ Done"
        )


        os.remove(file)


        await msg.delete()



    except Exception as e:

        logging.error(e)

        await msg.edit_text(
            "❌ Error aaya download me"
        )




def main():

    try:

        app = Application.builder().token(
            BOT_TOKEN
        ).build()

        app.add_handler(
            CommandHandler(
                "start",
                start
            )
        )


        app.add_handler(
            MessageHandler(
                filters.TEXT,
                handle_message
            )
        )


        print("BOT START")

        app.run_polling(
            drop_pending_updates=True
        )


    except Exception as e:

        print("bot error")
        traceback.print_exc()

        
    app.run_polling(

        drop_pending_updates=True
    )



if __name__ == "__main__":
    main()