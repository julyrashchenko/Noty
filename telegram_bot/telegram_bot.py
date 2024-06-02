from enum import Enum

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters,
                          CallbackQueryHandler)

from smart_notes.memory_storage import MemoryStorage


class Command(Enum):
    START = 'start'


class CommandHandlersFactory:
    # todo for commands and buttons
    pass


class TelegramBot:
    def __init__(self, token: str):
        self._application = ApplicationBuilder().token(token).build()

        # todo perhaps need to modify callback data (with descriptive strings)
        self._button_search = InlineKeyboardButton('Search', callback_data='1')
        self._button_record = InlineKeyboardButton('Record', callback_data='2')
        self._button_delete = InlineKeyboardButton('Delete', callback_data='3')
        self._button_show_random = InlineKeyboardButton('Show', callback_data='4')
        self._button_reset = InlineKeyboardButton('Reset', callback_data='5')
        self._keyboard_markup = InlineKeyboardMarkup([
            [self._button_record, self._button_search],
            [self._button_show_random, self._button_delete],
            [self._button_reset]
        ])

        self._application.add_handler(CommandHandler(Command.START.value, self.command_handler))
        self._application.add_handler(MessageHandler(filters.TEXT, self.text_handler))
        self._application.add_handler(CallbackQueryHandler(self.button_handler))
        self._memory_storage = MemoryStorage()

    def run_polling(self):
        print('Bot started.')
        self._application.run_polling()

    async def text_handler(self, update: Update, context: CallbackContext):
        input_text = update.message.text
        self._memory_storage.store(input_text)
        user_id = update.message.from_user.first_name
        answer = f'Got {input_text}, user {user_id}!'
        await update.message.reply_text(answer)

    async def command_handler(self, update: Update, context: CallbackContext):
        if update.message.text == f'/{Command.START.value}':
            await update.message.reply_text('Hi! Hello, world :)', reply_markup=self._keyboard_markup)

    async def button_handler(self, update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=f"Selected option: {query.data}")
