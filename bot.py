import os
import traceback
import logging


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
        "Link bhejo aur video milega."
    )



async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    url = update.message.text


    if "youtu" not in url:

        await update.message.reply_text(
            "❌ YouTube link bhejo"
        )

        return



    msg = await update.message.reply_text(
        "⏳ Downloading..."
    )


    try:

        file = download_video(url)


        await msg.edit_text(
            "📤 Sending..."
        )


        await update.message.reply_video(
            video=open(file,"rb")
        )


        os.remove(file)


        await msg.delete()


    except Exception:

        traceback.print_exc()

        await msg.edit_text(
            "❌ Download failed"
        )




def main():

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


    print("BOT STARTED")


    app.run_polling(
        drop_pending_updates=True
    )



if __name__=="__main__":
    main()