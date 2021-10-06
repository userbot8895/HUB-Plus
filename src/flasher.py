# flasher
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import time
import random

from userbot import tgclient
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from telethon.events import NewMessage

ehandler = EventHandler()
VERSION = "2021.8"

@ehandler.on(command="flash", hasArgs=True, outgoing=True)
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
 
register_module_desc("\"Flash\" a ZIP file.")
register_cmd_usage("flash", "<zip name>", "\"Flash\" a ZIP file.")
register_module_info(
    name="Flasher",
    authors="githubcatw, Haklerman, help from prototype74",
    version=VERSION
)