def main():

    async def run():
        app = Application.builder().token(
            BOT_TOKEN
        ).build()

        app.add_handler(
            CommandHandler("start", start)
        )

        app.add_handler(
            MessageHandler(filters.TEXT, handle_message)
        )

        print("BOT STARTED")

        await app.run_polling()


    asyncio.run(run())