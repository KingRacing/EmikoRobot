import random
from EikoBot.events import register
from EikoBot import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Au ah ga paham",
                 "Apa iya?",
                 "Tanya aja sama pak presiden"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
