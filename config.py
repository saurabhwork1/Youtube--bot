import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8632272810:AAE5ABa0amwLYIbiUKKFSGgT7WZe2RytTB8")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN missing")