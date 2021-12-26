# memes (miscellaneous)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from os.path import basename, isfile
from os.path import join as pathjoin
from pathlib import Path as lPath

import asyncio
import random
import re
import time

import requests
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from PIL import Image, ImageDraw, ImageFont

ehandler = EventHandler()
VERSION = "2021.8"

@ehandler.on(command="f", hasArgs=True, outgoing=True)
async def payf(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if not " " in event.text:
            await e.edit("`Give something to make an F out of.`")
            return
        paytext = event.pattern_match.group(1)
        pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
            paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
            paytext * 2, paytext * 2)
        await event.edit(pay)

@ehandler.on(command="lol", hasArgs=True, outgoing=True)
async def payf(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if not " " in event.text:
            await e.edit("`Give something to make a LOL out of.`")
            return
        paytext = event.text.split(" ")[1]
        pay = "```{}\n{}\n{}\n{}\n{}\n\n  {}\n {}\n{}\n {}\n  {}\n\n{}\n{}\n{}\n{}\n{}```".format(
            paytext, paytext, paytext, paytext, paytext * 4,
            paytext * 3, paytext + "    " + paytext, paytext + "      " + paytext, paytext + "    " + paytext, paytext * 3,
            paytext, paytext, paytext, paytext, paytext * 4)
        await event.edit(pay)

@ehandler.on(command="lfy", hasArgs=True, outgoing=True)
async def let_me_google_that_for_you(lmgtfy_q):  # img.gtfy
    if not lmgtfy_q.text[0].isalpha() and lmgtfy_q.text[0] in ("."):
        textx = await lmgtfy_q.get_reply_message()
        qry = lmgtfy_q.text.split(" ")[1]
        if qry:
            query = str(qry)
        elif textx:
            query = textx
            query = query.message
        query_encoded = query.replace(" ", "+")
        lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
        payload = {'format': 'json', 'url': lfy_url}
        r = requests.get('http://is.gd/create.php', params=payload)
        await lmgtfy_q.edit(f"[{query}]({r.json()['shorturl']})")


@ehandler.on(command="scam", hasArgs=True, outgoing=True)
async def scam(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        options = [
            'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
            'photo', 'document', 'cancel']
        input_str = event.text
        args = input_str.split()
        if len(args) == 1:  # Let bot decide action and time
            scam_action = random.choice(options)
            scam_time = random.randint(30, 60)
        elif len(args) == 2:  # User decides time/action
            try:
                scam_action = str(args[0]).lower()
                scam_time = random.randint(30, 60)
            except ValueError:
                scam_action = random.choice(options)
                scam_time = int(args[0])
        elif len(args) == 3:  # User decides both action and time
            scam_action = str(args[0]).lower()
            scam_time = int(args[1])
        else:
            await event.edit("`Invalid Syntax !!`")
            return
        try:
            if (scam_time > 0):
                await event.delete()
                async with event.client.action(event.chat_id, scam_action):
                    await asyncio.sleep(scam_time)
        except BaseException:
            return

@ehandler.on(command="kill", hasArgs=True, outgoing=True)
async def kill(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if getConfig("USERDATA") == None:
                raise Exception("kill requires a user data folder. Please set USERDATA in your config.")

        FILES = pathjoin(getConfig("USERDATA"),"plus", "killRsrc")
        Path(FILES).mkdir(parents=True, exist_ok=True)

        if not isfile(pathjoin(FILES,'ded.png')):
            await event.edit("`Downloading resource 1/2`")
            r = requests.get("https://github.com/userbot8895/rsrc/raw/main/ded.png", allow_redirects=True)
            open(pathjoin(FILES,'ded.png'), 'wb').write(r.content)

        if not isfile(pathjoin(FILES,'mc.ttf')):
            await event.edit("`Downloading resource 2/2`")
            r = requests.get("https://github.com/userbot8895/rsrc/raw/main/mc.ttf", allow_redirects=True)
            open(pathjoin(FILES,'mc.ttf'), 'wb').write(r.content)

        await dokill(event)
        reply = await event.get_reply_message() 
        await event.client.send_file(event.chat_id,'kill.webp', reply_to=reply)
        await event.delete()
        

async def dokill(event):
    FILES = pathjoin(getConfig("USERDATA"),"plus", "killRsrc")
    punched = None
    reply = await event.get_reply_message() 
    if reply:
        punched = reply.sender
    else:
        # kill the sender
        punched = event.sender
    # generate /kill message
    name = punched.first_name
    if punched.username:
        name = punched.username
    W,H = (512,288)
    msg = f"{name} fell out of the world"
    img = Image.open(pathjoin(FILES,'ded.png'))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(pathjoin(FILES,'mc.ttf'), 12)
    w, h = draw.textsize(msg, font=font)
    draw.text(((W-w)/2,((H-h)/2)-42),msg,(255,255,255),font=font)
    img.save('kill.webp')

register_module_desc("Memes! This module contains random commands.")
register_cmd_usage("f", "<emoji/character>", "Pay respect.")
register_cmd_usage("lol", "<emoji/character>", "Laugh out loud.")
register_cmd_usage("lfy", "<query>", "Let me Google that for you real quick!")
register_cmd_usage("scam", "<action> <time>", "Create fake chat actions, for fun.\nAvailable actions: `typing` (default)`, contact, game, location, voice, round, video, photo, document, cancel`")
register_module_info(
    name="Memes - random",
    authors="githubcatw, @BottomTextBot, Watn3y, Haklerman",
    version=VERSION
)

_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')