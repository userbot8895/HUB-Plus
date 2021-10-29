# plusinfo
# HUB++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from os.path import basename

ehandler = EventHandler()
VERSION = "2021.8"

@ehandler.on(command="plusver", hasArgs=True, outgoing=True)
async def plus(event): #punch
    if not event.text[0].isalpha() and event.text[0] in ("."):
        await event.edit(f"You're running HUB++ version {VERSION}.\n__Note: this is the version of plusinfo, other modules might have different versions. We recommend users to update every module they have installed.__")