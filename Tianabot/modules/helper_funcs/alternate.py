from telegram.error import BadRequest
from functools import wraps
from telegram import ChatAction


def send_message(message, text, *args, **kwargs):
    try:
        return message.reply_text(text, *args, **kwargs)
    except BadRequest as err:
        if str(err) == "Pesan balasan tidak ditemukan":
            return message.reply_text(text, quote=False, *args, **kwargs)


def typing_action(func):
    """Mengirim tindakan pengetikan saat memproses perintah func."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING
        )
        return func(update, context, *args, **kwargs)

    return command_func
