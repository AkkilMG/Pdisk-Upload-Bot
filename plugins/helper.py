# (c) HeimanPictures
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START = """
Start Message
"""

HELP = """
Help Message
"""

NON_OWNER = "You Can't Use Me Ask My [Owner](tg://user?id={})"


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📮 Update 📮', url='https://telegram.dog/HeimanSupports/'),
        InlineKeyboardButton('🛠️ Support 🛠️', url='https://telegram.dog/HeimanSupport/'),
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )



@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=START,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )


@Client.on_message(filters.command('help') & filters.private)
async def help(bot, message):
        await message.reply_chat_action("typing")
        await message.reply_text(
            text=HELP,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
