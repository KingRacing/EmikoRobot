import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from TianaBot.events import register
from TianaBot import telethn as tbot


PHOTO = "https://telegra.ph/file/22fdd1bbe77bc86669b5d.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hai [{event.sender.first_name}](tg://user?id={event.sender.id}), Saya Eiko Robot.** \n\n"
  TEXT += "⚪ **Saya Bekerja Dengan Benar** \n\n"
  TEXT += f"⚪ **Pengembangku: [Az](https://t.me/tth_kiya98)** \n\n"
  TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Terima Kasih Telah Menambahkanku Disini ❤️**"
  BUTTON = [[Button.url("Bantuan", "https://t.me/EikoManager_Bot?start=help"), Button.url("Support", "https://t.me/eiko_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)