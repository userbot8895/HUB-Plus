# memes multi-installer
# HyperBot++
# Licensed under the DBBPL
# Uses code from HyperUBot's package_manager, which is licensed under PEL
# (C) 2021 githubcatw

import userbot.include.git_api as git
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from logging import getLogger
import sys
import requests
import os
import time

log = getLogger(__name__)

MODULE_LIST = []

from userbot.sysutils.sys_funcs import isWindows

if isWindows():
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
    assets = git.getAssets(git.getReleaseData(git.getData("userbot8895/HUB-Plus"), 0))
    for asset in assets:
        assetName = git.getReleaseFileName(asset)
        assetURL = git.getReleaseFileURL(asset)
        assetSize = git.getSize(asset)
        if "memes_" in assetName:
            MODULE_LIST.append({"filename": assetName, "link": assetURL, "size": assetSize})
    print(MODULE_LIST)
    return MODULE_LIST

ehandler = EventHandler()
VERSION = "2022.1.2" 

@ehandler.on(command="memes", hasArgs=False, outgoing=True)
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

register_module_desc("Memes! This module installs **every meme module in HyperBot++**, so you have all meme commands with one command.")
register_cmd_usage("memes", "", "Install all meme modules")
register_module_info(
    name="Memes - installer",
    authors="githubcatw",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')