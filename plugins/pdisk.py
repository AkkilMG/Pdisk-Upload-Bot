
# (c) HeimanPictures


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import requests

from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.regex('http') & filters.private)
async def pdisk(bot, message):
        text = message.text
        if 'cofilink.com' in text or 'www.cofilink.com' in text or 'pdisk.me' in text or 'www.pdisk.me' in text:
            spl = link.split('=')
            vd_id = spl[-1]
            auth = "http://linkapi.net/open/clone_item/?api_key="+Config.API_KEY+"&item_id="+vd_id
        else:
            try:
            # Solved https://github.com/HeimanPictures/Pdisk-Upload-Bot/issues/1#issue-1018422275
                spl = text.split(' | ')
                url = spl[0]
                title = spl[1]
                thumb = spl[2]
                try:
                    auth = "http://linkapi.net/open/create_item/?api_key="+Config.API_KEY+"&content_src="+url+"&link_type=link"+"&title="+title+"&cover_url="+thumb 
                except Exception:
                    auth = "http://linkapi.net/open/create_item/?api_key="+Config.API_KEY+"&content_src="+url+"&link_type=link"+"&title="+title
            except Exception:
                url = text
                auth = "http://linkapi.net/open/create_item/?api_key="+Config.API_KEY+"&content_src="+url+"&link_type=link"+"&title=None"
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(auth,headers)
            res = r.json()
            #print(res)
            id = res["data"]["item_id"]
            await message.reply_chat_action("typing")
            pdisk = "https://cofilink.com/share-video?videoid="+id      
            await message.reply_photo(
                photo="https://static10.tgstat.ru/channels/_0/f3/f3218a8a0d195d12e73f6b69e51bbb4f.jpg",
                caption="**URL:** `"+pdisk+"`\n\n**The PDisk Link Is Below The Provided Link Will Be Uploaded in few minutes.\nThank You**\n\n**@HeimanSupports**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔗 PDisk 🔗", url=f"{pdisk}")]
                ])
            )

