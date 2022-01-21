# exec
# HUB++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import time
import random

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
import subprocess as sub

ehandler = EventHandler()
VERSION = "2022.1.2"

@ehandler.on(command="exec", hasArgs=True, outgoing=True)
async def doexec(event):
	codearr = event.text.split(" ")
	code = ' '.join(codearr[1:])
	ev = exec(code)
	event.edit(f"Input:\n`{code}`\n\nResult:\n`{ev}`")

@ehandler.on(command="eval", hasArgs=True, outgoing=True)
async def doeval(event):
	codearr = event.text.split(" ")
	code = ' '.join(codearr[1:])
	ev = eval(code)
	event.edit(f"Input:\n`{code}`\n\nResult:\n`{ev}`")
 
register_module_desc("Execute commands.\n**You are responsible for any damage done by using these commands.**")
register_cmd_usage("exec", "command", "Execute a Python command.")
register_cmd_usage("eval", "command", "Execute a Python command using eval.\n**You are responsible for any damage done by using these commands.**")
register_module_info(
    name="Execute",
    authors="githubcatw",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')