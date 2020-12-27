# memes multi-installer
# HyperBot++
# Licensed under the DBBPL
# Uses code from HyperUBot's package_manager, which is licensed under PEL
# (C) 2020 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO, OS
from userbot.include.aux_funcs import module_info
import userbot.include.git_api as git
from telethon.events import NewMessage
from logging import getLogger
import sys
import requests
import os
import time

log = getLogger(__name__)

MODULE_LIST = []

if OS and OS.startswith("win"):
    USER_MODULES_DIR = ".\\userbot\\modules_user\\"
else:
    USER_MODULES_DIR = "./userbot/modules_user/"

if " " not in sys.executable:
    EXECUTABLE = sys.executable
else:
    EXECUTABLE = '"' + sys.executable + '"'

def list_updater():
    global MODULE_LIST
    MODULE_LIST = []
    assets = git.getAssets(git.getReleaseData(git.getData("userbot8895/HyperBot_Plus"), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        assetSize = git.getSize(asset)
        if "memes_" in assetName:
            MODULE_LIST.append({"filename": assetName, "link": assetURL, "size": assetSize})
    print(MODULE_LIST)
    return MODULE_LIST

@tgclient.on(NewMessage(pattern=r"^\.memes", outgoing=True))
async def flash(event):
    await event.edit("Fetching all memes modules...")
    list_updater()
    await event.edit(f"Installing 0/{len(MODULE_LIST)}")
    installed = 0
    for i in MODULE_LIST:
        request = requests.get(i['link'], allow_redirects=True)
        if os.path.exists(USER_MODULES_DIR + i['filename']):
        	os.remove(USER_MODULES_DIR + i['filename'])
        open(USER_MODULES_DIR + i['filename'], 'wb').write(request.content)
        log.info(f"Meme module '{i['filename'][:-3]}' has been installed")
        installed = installed + 1
        await event.edit(f"Installing {installed}/{len(MODULE_LIST)}")

    await event.edit(f"Rebooting...")
    time.sleep(1)  # just so we can actually see a message
    await event.edit(f"Userbot rebooted. You have become a true memelord.\
    \nThis installer module has self-destructed. If you need it again, just re-install and re-run it.")
    os.remove(USER_MODULES_DIR + "memes.py")
    args = [EXECUTABLE, "-m", "userbot"]
    os.execle(sys.executable, *args, os.environ)
    await msg.client.disconnect()

MODULE_DESC.update({"memes": "Memes! This module installs **every meme module in HyperBot++**, so you have all meme commands with one command."})
MODULE_DICT.update({"memes": ".memes\nUsage: Install all meme modules.\
\nIf you don't want all read the [Installing Extra Commands]\
(https://github.com/githubcatw/HyperBot_Plus/blob/master/guides/Installing_Old_Extra_Commands.md) guide."})
MODULE_INFO.update({"memes": module_info(name='Memes (installer)', version='1.0')})