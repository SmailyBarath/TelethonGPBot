from telethon import events, Button
from GPBot import Stark
from Configs import Config

btn = [
        [Button.inline("Admin", data="admin"), Button.inline("Ban", data="ban")],
        [Button.inline("Pin", data="pin"), Button.inline("Pugres", data="purges")],
        [Button.inline("Locks", data="locks"), Button.inline("Mention All", data="mention")],
        [Button.inline("Zombies", data="zombies"), Button.inline("Info", data="info")]
]

HELP_TEXT = """
**Heya {} help menu here:**

/start - To Start Me ;)
/help - To Get Available Help Menu

__Report Bugs At--->__ **@JackSparrowSupport**
All cammond can be used with ! or ? or /.
""".format(Config.BOT_US)


@Stark.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):

    if event.is_group:
       await event.reply("Contact me in PM to get available help menu!", buttons=[
       [Button.url("Help And Commands!", "T.me/{}?start=help".format(Config.BOT_US))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Stark.on(events.NewMessage(pattern="^/start help"))
async def _(event):

    await event.reply(HELP_TEXT, buttons=btn)

@Stark.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):

     await event.edit(HELP_TEXT, buttons=btn)
