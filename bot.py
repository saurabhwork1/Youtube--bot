def main():

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(filters.TEXT, handle_message)
    )

    print("BOT STARTED")

    app.run_polling()


if __name__ == "__main__":
    try:
       