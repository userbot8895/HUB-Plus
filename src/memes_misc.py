# memes (miscellaneous)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from telethon.events import NewMessage
from os.path import basename

import asyncio
import random
import re
import time

import requests
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from cowpy import cow
from pyfiglet import Figlet

ehandler = EventHandler()
VERSION = "2021.7" 

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
        if len(args) == 0:  # Let bot decide action and time
            scam_action = random.choice(options)
            scam_time = random.randint(30, 60)
        elif len(args) == 1:  # User decides time/action
            try:
                scam_action = str(args[0]).lower()
                scam_time = random.randint(30, 60)
            except ValueError:
                scam_action = random.choice(options)
                scam_time = int(args[0])
        elif len(args) == 2:  # User decides both action and time
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
async def scam(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        await event.edit("`Downloading resource 1/2`")
        r = requests.get("https://github.com/userbot8895/rsrc/blob/main/ded.png", allow_redirects=True)
        open('ded.png', 'wb').write(r.content)
        await event.edit("`Downloading resource 2/2`")
        r = requests.get("https://github.com/userbot8895/rsrc/blob/main/mc.ttf", allow_redirects=True)
        open('mc.ttf', 'wb').write(r.content)

register_module_desc("Memes! This module contains random commands.")
register_cmd_usage("f", "<emoji/character>", "Pay respect.")
register_cmd_usage("lol", "<emoji/character>", "Laugh out loud.")
register_cmd_usage("lfy", "<query>", "Let me Google that for you real quick!")
register_cmd_usage("say", "<what to say>", "Say something.")
register_cmd_usage("scam", "<action> <time>", "Create fake chat actions, for fun.\nAvailable actions: `typing` (default)`, contact, game, location, voice, round, video, photo, document, cancel`")
register_module_info(
    name="Memes - random",
    authors="githubcatw, @BottomTextBot, Watn3y, Haklerman",
    version=VERSION
)
