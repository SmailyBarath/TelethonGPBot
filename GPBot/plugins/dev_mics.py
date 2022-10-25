from telethon import events, Button
from GPBot import Stark

@Stark.on(events.callbackquery.CallbackQuery(data="dev"))
async def _(event):

    await event.edit(DEV_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

DEV_TEXT = """
**✘ A module of Dev on only use Owner and Developer**

‣ `?eval`: Run a code
‣ `?leave`: Left the group
‣ `?logs`: Sent bot logs
""" 



