# systools (extension)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage
from os.path import basename

@tgclient.on(NewMessage(outgoing=True, pattern="^\.logoff$"))
async def logoff(event):  # bot shutdown
    if not event.text[0].isalpha() and event.text[0] in ("."):
        await event.edit("`Farewell!`")
        if BOTLOG:
            await event.client.send_message(BOTLOG_CHATID, "logoff")
        await event.client.log_out()

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Extra commands for the systools module."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
        ".logoff\
    \nUsage: Log off."})

MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Systools (extension)', version='1.0')})