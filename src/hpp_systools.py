# systools (extension)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler

ehandler = EventHandler()
VERSION = "2022.2"

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
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')