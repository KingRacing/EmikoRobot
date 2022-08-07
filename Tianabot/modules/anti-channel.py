import asyncio
from pyrogram import filters
from Tianabot import pbot as app
from pyrogram.types import Message
from Tianabot import eor
from Tianabot.utils.errors import capture_err

active_channel = []

async def channel_toggle(db, message: Message):
    status = message.text.split(None, 1)[1].lower()
    chat_id = message.chat.id
    if status == "on":
        if chat_id not in db:
            db.append(chat_id)
            text = "**Mode Anti Channel `diaktifkan` ✅. Saya akan menghapus semua pesan yang dikirim dengan nama saluran.**"
            return await eor(message, text=text)
        await eor(message, text="antichannel telah Diaktifkan.")
    elif status == "off":
        if chat_id in db:
            db.remove(chat_id)
            return await eor(message, text="antichannel Dinonaktifkan!")
        await eor(message, text=f"**Mode Anti Channel Berhasil dinonaktifkan di obrolan** {message.chat.id} ❌")
    else:
        await eor(message, text="Saya hanya faham `/antichannel on` dan `/antichannel off` saja")


# Enabled | Disable antichannel


@app.on_message(filters.command("antichannel") & ~filters.edited)
@capture_err
async def antichannel_status(_, message: Message):
    if len(message.command) != 2:
        return await eor(message, text="Saya hanya faham `/antichannel on` dan `/antichannel off` saja")
    await channel_toggle(active_channel, message)



@app.on_message(
    (
        filters.document
        | filters.photo
        | filters.sticker
        | filters.animation
        | filters.video
        | filters.text
    )
    & ~filters.private,
    group=41,
)
async def anitchnl(_, message):
  chat_id = message.chat.id
  if message.sender_chat:
    sender = message.sender_chat.id 
    if message.chat.id not in active_channel:
        return
    if chat_id == sender:
        return
    else:
        await message.delete()
        ti = await message.reply_text("**Pesan anti channel terdeteksi. Saya menghapusnya..!**")
        await asyncio.sleep(7)
        await ti.delete()        

__mod_name__ = "Aɴᴛɪ-Cʜᴀɴɴᴇʟ"
__help__ = """
Grup Anda untuk menghentikan saluran anonim mengirim pesan ke obrolan Anda. 
**Tipe pesan**
        - dokumen
        - foto
        - stiker
        - animasi
        - video
        - teks
        
**Perintah Admin:**
 - /antichannel [on / off] - Fungsi Anti channel
**Catatan** : Jika saluran tertaut, kirim karakter yang berisi apa pun dalam jenis ini saat pada fungsi no del
 """
