from GPBot import Stark
from telethon import events, Button

PM_START_TEXT = """
**Hi {}**
I can manage your group and i will promise and protect your group Hit /help.

**Click the below button for help menu!**
"""

@Stark.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.inline("Help And Commands", data="help")],
        [Button.url("Support", "https://t.me/JackSparrowSupport")]])
       return

    if event.is_group:
       await event.reply("**I am alive!**")
       return
