import os

from dotenv import load_dotenv

from telegram_bot.telegram_bot import TelegramBot

load_dotenv()
TelegramBot(token=os.environ['TELEGRAM_BOT_ACCESS_TOKEN']).run_polling()
print()
