from telegram.ext import ApplicationBuilder


class TelegramBot:
    def __init__(self, token: str):
        self.application = ApplicationBuilder().token(token).build()
