# memes (RNG)
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

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
from .memes_common import *

@tgclient.on(NewMessage(outgoing=True, pattern=r"^.coinflip$"))
async def coin(event):  # coinflip
    if not event.text[0].isalpha() and event.text[0] in ("."):
        r = random.randint(1, 10000)
        await event.edit("`Throwing the coin...`")
        time.sleep(3)
        if r % 2 == 1:
            await event.edit("`The coin landed on: Heads`")
        elif r % 2 == 0:
            await event.edit("`The coin landed on: Tails`")
        else:
            await event.edit("`Mate, this is a beer bottle cap, give me a coin!`")
            
@tgclient.on(NewMessage(pattern="^.punch(?: |$)(.*)", outgoing=True))
async def who(event): #punch
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if event.fwd_from:
            return
        replied_user = await get_user(event)
        caption = await punch(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id
        if not message_id_to_reply:
            message_id_to_reply = None
        try:
            await event.edit(caption)
        except BaseException:
            await event.edit("`Can't punch this person, loading 12 gauge buckshot in my shotgun!!`")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError):
            await event.edit("`This dude doesn't even exist`")
            return None
    return replied_user

async def punch(replied_user, event): #builds the punch msg itself
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        punched = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"
    temp = random.choice(PUNCH_TEMPLATES)
    punch = random.choice(PUNCH)
    gun = random.choice(GUN)
    caption = "..." + temp.format(victim=punched, punches=punch, gun=gun)
    return caption


@tgclient.on(NewMessage(pattern="^.slap(?: |$)(.*)", outgoing=True))
async def who(event):  # slap
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if event.fwd_from:
            return
        replied_user = await get_user(event)
        caption = await slap(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id
        if not message_id_to_reply:
            message_id_to_reply = None
        try:
            await event.edit(caption)
        except BaseException:
            await event.edit("`Can't slap this person, loading 12 gauge buckshot in my shotgun!!`")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.sender_id))
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))
        except (TypeError, ValueError):
            await event.edit("`This dude doesn't even exist`")
            return None
    return replied_user

async def slap(replied_user, event):  # builds the slap msg itself
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username
    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"
    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)
    emoji = random.choice(EMOJI)
    caption = "..." + temp.format(victim=slapped, item=item, hits=hit, throws=throw, emoji=emoji)
    return caption


@tgclient.on(NewMessage(outgoing=True, pattern="^.decide(?: |$)(.*)"))
async def decide(event):  # yes/no
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if event.fwd_from:
            return
        message = event.pattern_match.group(1)
        message_id = None
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        if not message:
            r = requests.get("https://yesno.wtf/api").json()
        else:
            try:
                r = requests.get(f"https://yesno.wtf/api?force={message.lower()}").json()
            except BaseException:
                await event.edit("`Available decisions:` *yes*, *no*, *maybe*")
                return
        await event.client.send_message(event.chat_id, str(r["answer"]).upper(), reply_to=message_id, file=r["image"])
        await event.delete()

@tgclient.on(NewMessage(outgoing=True, pattern="^\.react$"))
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(random.choice(FACEREACTS))

@tgclient.on(NewMessage(outgoing=True, pattern="^\.shg$"))
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(random.choice(SHGS))
    
@tgclient.on(NewMessage(outgoing=True, pattern="^\.doubt$"))
async def doubt(shg):
    await shg.edit(random.choice(DOUBT))
    
@tgclient.on(NewMessage(outgoing=True, pattern="^\.cry$"))
async def cry(e):
    """ y u du dis, i cry everytime !! """
    await e.edit(random.choice(CRI))

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Memes! This module contains stuff involving randomness."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
    "\n\n.hi\
    \nUsage: Greet everyone!\
    \n\n.coinflip <heads/tails>\
    \nUsage: Flip a coin!\
    \n\n.punch\
    \nUsage: Punch 'em!\
    \n\n.slap\
    \nUsage: reply to slap them with random objects!\
    \n\n.decide [Optional: (yes, no, maybe)]\
    \nUsage: Make a quick decision.\
    \n\n.react\
    \nUsage: Make your userbot react to everything.\
    \n\n.shg\
    \nUsage: Shrug at it !!\
    \n\n.cry\
    \nUsage: y u du dis, i cri."
})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Memes (RNG)', version='1.0')})