from telethon.errors.rpcerrorlist import YouBlockedUserError
from Tianabot import telethn as tbot
from Tianabot.events import register
from Tianabot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


@register(pattern="^/sg ?(.*)")
async def lastname(steal):
    steal.pattern_match.group(1)
    puki = await steal.reply("```Mengambil Informasi Pengguna Tersebut..```")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("```Mohon Balas Ke Pesan Pengguna.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("```Balas Ke Pesan Pengguna Asli.```")
        return
    await puki.edit("```Mohon Tunggu...```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Error, hubungi @eiko_support```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                ) 
                return
            if response.text.startswith("Tidak Ada Jejak") or r.text.startswith(
                "Tidak Ada Jejak"
            ):
                await puki.edit("```Saya Tidak Dapat Menemukan Informasi Pengguna Ini, Pengguna Ini Belum Pernah Mengubah Namanya Sebelumnya.```")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"```{response.message}```")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("`Saya Lelah Maaf...`")
