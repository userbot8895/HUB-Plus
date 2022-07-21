# memes (animated)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from os.path import basename

import asyncio
import random
import time

ehandler = EventHandler()
VERSION = "2022.2.1" 

@ehandler.on(command="oof", hasArgs=False, outgoing=True)
async def Oof(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Oof"
        for j in range(15):
            t = t[:-1] + "of"
            await e.edit(t)
            
@ehandler.on(command="hmm", hasArgs=False, outgoing=True)
async def Hmm(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Hmm"
        for j in range(10):
            t = t[:-1] + "mm"
            await e.edit(t)
            
@ehandler.on(command="ree", hasArgs=False, outgoing=True)
async def Ree(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Ree"
        for j in range(15):
            t = t[:-1] + "ee"
            await e.edit(t)

@ehandler.on(command="lool", hasArgs=False, outgoing=True)
async def Lol(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "LOL"
        for j in range(15):
            t = t[:-1] + "OL"
            await e.edit(t)
            
@ehandler.on(command="gay", hasArgs=False, outgoing=True)
async def Gay(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Gay"
        for j in range(15):
            t = t[:-1] + "ay"
            await e.edit(t)

@ehandler.on(command="brr", hasArgs=False, outgoing=True)
async def Brr(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Brr"
        for j in range(15):
            t = t + "r"
            await e.edit(t)
            
@ehandler.on(command="x", hasArgs=True, outgoing=True)
async def Extend(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        if not " " in e.text:
            await e.edit("`What should I extend?`")
            return
        # get the requested text
        paytext = e.text.split(" ")[1]
        # return if text is too short
        if len(paytext) < 3:
            await e.edit("`Too short!`")
            return
        # to make the copy-pasted code work fine
        t = paytext
        # get the string start (1st character)
        ts = t[0]
        # get the string end (last character)
        te = t[-1]
        # get the string middle
        tm = t[1:-1]
        # do 15 times
        for j in range(15):
            # transform the text to previous text without the last character + middle + end
            t = t[:-1] + tm + te
            # edit the message with the new text
            await e.edit(t)

register_module_desc("Memes! This module contains various animations.")
register_cmd_usage("oof", "", "Oooooof")
register_cmd_usage("hmm", "", "Hmmmmmm")
register_cmd_usage("lool", "", "LOOOOOOL")
register_cmd_usage("gay", "", "Gaaaaay")
register_cmd_usage("ree", "", "Reeeeee")
register_cmd_usage("brr", "", "Brrrrrr")
register_cmd_usage("x", "<text to extend, preferrably 3 characters>", "Like the above commands but customizable.")
register_module_info(
    name="Memes - animated",
    authors="githubcatw, @BottomTextBot, Haklerman, help from prototype74",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')