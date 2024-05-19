from enum import Enum

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters


class Command(Enum):
    START = 'start'


class CommandHandlersFactory:
    # todo
    pass


class TelegramBot:
    def __init__(self, token: str):
        self.application = ApplicationBuilder().token(token).build()
        self.application.add_handler(CommandHandler(Command.START.value, self.command_handler))
        self.application.add_handler(MessageHandler(filters.TEXT, self.text_handler))

    def run_polling(self):
        print('Bot started.')
        self.application.run_polling()

    async def text_handler(self, update: Update, context: CallbackContext):
        input_text = update.message.text
        user_id = update.message.from_user.first_name
        answer = f'Got {input_text}, user {user_id}!'
        await update.message.reply_text(answer)

    async def command_handler(self, update: Update, context: CallbackContext):
        if update.message.text == f'/{Command.START.value}':
            await update.message.reply_text('Hi! Hello, world :)')
