# flasher
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import time
import random

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
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
 
MODULE_DESC.update({"flasher": "Flash a ZIP file."})
MODULE_DICT.update({"flasher": ".flash <file_name>\nUsage: Flash `file_name.zip`"})
MODULE_INFO.update({"flasher": module_info(name='Flasher', version='1.0')})