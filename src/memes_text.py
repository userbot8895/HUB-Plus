# memes (text)
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

@tgclient.on(NewMessage(outgoing=True, pattern="^.vapor(?: |$)(.*)"))
async def vapor(vpr):  # vapor
    if not vpr.text[0].isalpha() and vpr.text[0] in ("."):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return
        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)
        await vpr.edit("".join(reply_text))

@tgclient.on(NewMessage(outgoing=True, pattern="^.str(?: |$)(.*)"))
async def stretch(stret):  # stretch
    if not stret.text[0].isalpha() and stret.text[0] in ("."):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return
        count = random.randint(3, 10)
        reply_text = re.sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), message)
        await stret.edit(reply_text)

@tgclient.on(NewMessage(outgoing=True, pattern="^.zal(?: |$)(.*)"))
async def zal(zgfy):  # chaotic
    if not zgfy.text[0].isalpha() and zgfy.text[0] in ("."):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await zgfy.edit("`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`")
            return
        for charac in message:
            if not charac.isalpha():
                reply_text.append(charac)
                continue
            for _ in range(0, 3):
                randint = random.randint(0, 2)
                if randint == 0:
                    charac = charac.strip() + random.choice(ZALG_LIST[0]).strip()
                elif randint == 1:
                    charac = charac.strip() + random.choice(ZALG_LIST[1]).strip()
                else:
                    charac = charac.strip() + random.choice(ZALG_LIST[2]).strip()
            reply_text.append(charac)
        await zgfy.edit("".join(reply_text))
        
@tgclient.on(NewMessage(outgoing=True, pattern="^.point (.*)$"))
async def Fingers(e):
    text = e.pattern_match.group(1)
    await e.edit(f"👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿{'👇🏿'*len(text)}👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿\n"+
                 f"👉🏿👊🏾👇🏾👇🏾👇🏾👇🏾{'👇🏾'*len(text)}👇🏾👇🏾👇🏾👇🏾👊🏾👈🏿\n"+
                 f"👉🏿👉🏾👊🏽👇🏽👇🏽👇🏽{'👇🏽'*len(text)}👇🏽👇🏽👇🏽👊🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👊🏼👇🏼👇🏼{'👇🏼'*len(text)}👇🏼👇🏼👊🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👉🏼👊🏻👇🏻{'👇🏻'*len(text)}👇🏻👊🏻👈🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👉🏼👉🏻👊{'👇'*len(text)}👊👈🏻👈🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👉🏼👉🏻👉` {text} `👈👈🏻👈🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👉🏼👉🏻👊{'👆'*len(text)}👊👈🏻👈🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👉🏼👊🏻👆🏻{'👆🏻'*len(text)}👆🏻👊🏻👈🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👉🏽👊🏼👆🏼👆🏼{'👆🏼'*len(text)}👆🏼👆🏼👊🏼👈🏽👈🏾👈🏿\n"+
                 f"👉🏿👉🏾👊🏽👆🏽👆🏽👆🏽{'👆🏽'*len(text)}👆🏽👆🏽👆🏽👊🏽👈🏾👈🏿\n"+
                 f"👉🏿👊🏾👆🏾👆🏾👆🏾👆🏾{'👆🏾'*len(text)}👆🏾👆🏾👆🏾👆🏾👊🏾👈🏿\n"+
                 f"👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿{'👆🏿'*len(text)}👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿\n")

@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.(\w+)say (.*)"))
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")
    
@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.(\w+)think (.*)"))
async def think(cowmsg):
    """ For .cowthink module, userbot wrapper for cow which thinks of things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese(thoughts=True)

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")
    
@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.figlet(\w+) (.*)"))
async def figlet(figletmsg):
    """ For .figlet module. """
    arg = figletmsg.pattern_match.group(1).lower()
    text = figletmsg.pattern_match.group(2).lower()
    if arg == "":
        arg = "slant"
    if arg not in Figlet.getFonts(Figlet()):
        return
    f = Figlet(font=arg)
    ft =  f.renderText(text)
    await figletmsg.edit(f"`\n{ft}`")
    
@tgclient.on(NewMessage(outgoing=True, pattern="^.mock(?: |$)(.*)"))
async def spongemocktext(mock):
    if not mock.text[0].isalpha() and mock.text[0] in ("."):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return
        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)
        await mock.edit("".join(reply_text))

@tgclient.on(NewMessage(outgoing=True, pattern="^.clap(?: |$)(.*)"))
async def claptext(memereview):  # clap
    if not memereview.text[0].isalpha() and memereview.text[0] in ("."):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)

@tgclient.on(NewMessage(pattern=r".type(?: |$)(.*)", outgoing=True))
async def typewriter(typew):
    if not typew.text[0].isalpha() and typew.text[0] in ("."):
        textx = await typew.get_reply_message()
        message = typew.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await typew.edit("`Give a text to type!`")
            return
        sleep_time = 0.1
        typing_symbol = "|"
        old_text = ""
        await typew.edit(typing_symbol)
        await asyncio.sleep(sleep_time)
        for character in message:
            old_text = old_text + "" + character
            typing_text = old_text + "" + typing_symbol
            await typew.edit(typing_text)
            await asyncio.sleep(sleep_time)
            await typew.edit(old_text)
            await asyncio.sleep(sleep_time)

@tgclient.on(NewMessage(outgoing=True, pattern=r"^.shout(?: |$)([\s\S]*)"))
async def shout(request):
    if not request.text[0].isalpha() and request.text[0] in ("."):
        textx = await request.get_reply_message()
        message = request.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await request.edit("`Usage: .shout <text>`")
            return
        msg = "```"
        result = []
        result.append(' '.join([s for s in message]))
        for pos, symbol in enumerate(message[1:]):
            result.append(symbol + ' ' + '  ' * pos + symbol)
        result = list("\n".join(result))
        result[0] = message[0]
        result = "".join(result)
        msg = "```\n" + result + "```"
        await request.edit(msg)

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Memes! This module contains text-based stuff."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".vapor\
    \nUsage: Vaporize everything!\
    \n\n.str\
    \nUsage: Stretch it.\
    \n\n.zal\
    \nUsage: Invoke the feeling of chaos.\
    \n\n.point <text>\
    \nUsage: Point at something with a nice emoji gradient.\
    \n\n.cowsay\
    \nUsage: Cow which says things.\
    \n\n.cowthink\
    \nUsage: Cow which thinks of things.\
    \n\n.figlet\
    \nUsage: Large text.\
    \n\n.mock\
    \nUsage: Do it and find the real fun.\
    \n\n.clap\
    \nUsage: Praise people!\
    \n\n.shout <text>\
    \nUsage: A little piece of fun wording! Give a loud shout out in the chatroom.\
    \n\n.clap\
    \nUsage: Praise people!"
})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Memes (text)', version='1.0')})