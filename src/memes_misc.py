# memes (miscellaneous)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
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

@tgclient.on(NewMessage(outgoing=True, pattern=r"^.f (.*)"))
async def payf(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        paytext = event.pattern_match.group(1)
        pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
            paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
            paytext * 2, paytext * 2)
        await event.edit(pay)

@tgclient.on(NewMessage(outgoing=True, pattern=r"^.lol (.*)"))
async def payf(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        paytext = event.pattern_match.group(1)
        pay = "```{}\n{}\n{}\n{}\n{}\n\n  {}\n {}\n{}\n {}\n  {}\n\n{}\n{}\n{}\n{}\n{}```".format(
            paytext, paytext, paytext, paytext, paytext * 4,
            paytext * 3, paytext + "    " + paytext, paytext + "      " + paytext, paytext + "    " + paytext, paytext * 3,
            paytext, paytext, paytext, paytext, paytext * 4)
        await event.edit(pay)

@tgclient.on(NewMessage(outgoing=True, pattern="^.lfy (.*)"))
async def let_me_google_that_for_you(lmgtfy_q):  # img.gtfy
    if not lmgtfy_q.text[0].isalpha() and lmgtfy_q.text[0] in ("."):
        textx = await lmgtfy_q.get_reply_message()
        qry = lmgtfy_q.pattern_match.group(1)
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


@tgclient.on(NewMessage(pattern=r".scam(?: |$)(.*)", outgoing=True))
async def scam(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        options = [
            'typing', 'contact', 'game', 'location', 'voice', 'round', 'video',
            'photo', 'document', 'cancel']
        input_str = event.pattern_match.group(1)
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

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Memes! This module contains random commands."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".f <emoji/character>\
    \nUsage: Pay Respects.\
    \n\n.lol <emoji/character>\
    \nUsage: Laugh out loud.\
    \n\n.lfy <query>\
    \nUsage: Let me Google that for you real quick!\
    \n\n.scam <action> <time>\
    \n(Available actions: `typing, contact, game, location, voice, round, video, photo, document, cancel`)\
    \nUsage: Create fake chat actions, for fun. (Default action: `typing`)"
})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Memes (miscellaneous)', version='1.0')})