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
VERSION = "2021.8"

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

@ehandler.on(command="sh", hasArgs=True, outgoing=True)
async def execsh(event):
	codearr = event.text.split(" ")
	sub.run(codearr[1:], stdout=sub.PIPE)
	event.edit(f"Input:\n`{code}`\n\nResult:\n`{ev}`")
 
register_module_desc("Execute commands.\n**You are responsible for any damage done by using these commands.**")
register_cmd_usage("exec", "command", "Execute a Python command.")
register_cmd_usage("sh", "command", "Execute a shell command.")
register_cmd_usage("eval", "command", "Execute a Python command using eval.\n**You are responsible for any damage done by using these commands.**")
register_module_info(
    name="Execute",
    authors="githubcatw",
    version=VERSION
)