import time
import random

from userbot import tgclient
from telethon.events import NewMessage

@tgclient.on(NewMessage(pattern=r"^\.flash (.*)", outgoing=True))
async def flash(event):
    r = random.randint(1, 10000)
	text = event.pattern_match.group(1)
	if len(text.split(" ")) > 1:
		await event.edit("`Cannot flash file!`")
		return
	await event.edit(f"`Flashing` {text}.zip`...`")
	time.sleep(4)
	if r % 2 == 1:
		await event.edit(f"`Successfully flashed` {text}.zip`!`")
	elif r % 2 == 0:
		await event.edit(f"`Flashing` {text}.zip `failed successfully!`")