from telegram.ext import Application
from config import TOKEN


def main():
    app = Application.builder().token(TOKEN).build()

    print("BOT STARTED")

    app.run_polling()


if __name__ == "__main__":
    main()