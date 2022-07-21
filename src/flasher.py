# flasher
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import time
import random

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler

ehandler = EventHandler()
VERSION = "2022.2.1"

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
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')