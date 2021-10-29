# systools (extension)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler

ehandler = EventHandler()
VERSION = "2021.8"

@ehandler.on(command="logoff", hasArgs=False, outgoing=True)
async def logoff(event):  # bot shutdown
    if not event.text[0].isalpha() and event.text[0] in ("."):
        await event.edit("`Farewell!`")
        await event.client.log_out()

register_module_desc("Extra commands for the systools module.")
register_cmd_usage("logoff", "", "Log off.")
register_module_info(
    name="Systools (extension)",
    authors="githubcatw, Haklerman",
    version=VERSION
)