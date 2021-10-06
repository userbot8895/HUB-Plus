# memes (RNG)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
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

ehandler = EventHandler()
VERSION = "2021.8"

@ehandler.on(command="punch", hasArgs=True, outgoing=True)
async def who(event): #punch
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if event.fwd_from:
            return
        if len(event.text.split(" ")) > 1:
            await event.edit("`Too many arguments!`")
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
    elif len(event.text.split(" ")) != 1:
        # punch the sender as a form of punisjment
        self_user = await event.client.get_me()
        user = self_user.id
    else:
        user = event.text.split(" ")[1]
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


@ehandler.on(command="slap", hasArgs=True, outgoing=True)
async def who(event):  # slap
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if event.fwd_from:
            return
        if len(event.text.split(" ")) > 1:
            await event.edit("`Too many arguments!`")
        replied_user = await get_user(event)
        caption = await slap(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id
        if not message_id_to_reply:
            message_id_to_reply = None
        try:
            await event.edit(caption)
        except BaseException:
            await event.edit("`Can't slap this person, loading 12 gauge buckshot in my shotgun!!`")

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


@ehandler.on(command="decide", hasArgs=True, outgoing=True)
async def decide(event):  # yes/no
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if event.fwd_from:
            return
        message = None
        if len(event.text.split(" ")) > 0:
            message = event.text.split(" ")[1]
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

@ehandler.on(command="react", hasArgs=False, outgoing=True)
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(random.choice(FACEREACTS))

@ehandler.on(command="shg", hasArgs=False, outgoing=True)
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(random.choice(SHGS))
    
@ehandler.on(command="doubt", hasArgs=False, outgoing=True)
async def doubt(shg):
    await shg.edit(random.choice(DOUBT))
    
@ehandler.on(command="cry", hasArgs=False, outgoing=True)
async def cry(e):
    """ y u du dis, i cry everytime !! """
    await e.edit(random.choice(CRI))

register_module_desc("Memes! This module contains stuff involving randomness.")
register_cmd_usage("punch", "", "Punch 'em!")
register_cmd_usage("slap", "", "Reply to slap them with random objects!")
register_cmd_usage("decide", "[optional: yes, no, maybe]", "Make a quick decision.")
register_cmd_usage("react", "", "Make your userbot react to everything.")
register_cmd_usage("shg", "", "Shrug at it.")
register_cmd_usage("cry", "", "y u du dis, i cri.")
register_module_info(
    name="Memes - RNG",
    authors="githubcatw, @BottomTextBot, Haklerman",
    version=VERSION
)
