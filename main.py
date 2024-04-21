import os

from dotenv import load_dotenv

from telegram_bot.telegram_bot import TelegramBot

load_dotenv()
bot = TelegramBot(token=os.environ['TELEGRAM_BOT_ACCESS_TOKEN'])
print()
