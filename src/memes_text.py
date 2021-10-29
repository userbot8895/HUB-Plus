# memes (text)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from os.path import basename

import asyncio
import random
import re

from cowpy import cow
from pyfiglet import Figlet
from .memes_common import *

ehandler = EventHandler()
VERSION = "2021.8"

@ehandler.on(command="vapor", hasArgs=True, outgoing=True)
async def vapor(vpr):  # vapor
    if not vpr.text[0].isalpha() and vpr.text[0] in ("."):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(vpr.text.split(" ")) > 1:
            message = ' '.join(vpr.text.split(" ")[1:])
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

@ehandler.on(command="str", hasArgs=True, outgoing=True)
async def stretch(stret):  # stretch
    if not stret.text[0].isalpha() and stret.text[0] in ("."):
        textx = await stret.get_reply_message()
        message = stret.text
        message = "vpr.pattern_match.group(1)"
        if len(stret.text.split(" ")) > 1:
            message = ' '.join(stret.text.split(" ")[1:])
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return
        count = random.randint(3, 10)
        reply_text = re.sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count), message)
        await stret.edit(reply_text)

@ehandler.on(command="zal", hasArgs=True, outgoing=True)
async def zal(zgfy):  # chaotic
    if not zgfy.text[0].isalpha() and zgfy.text[0] in ("."):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(zgfy.text.split(" ")) > 1:
            message = ' '.join(zgfy.text.split(" ")[1:])
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
        
@ehandler.on(command="point", hasArgs=True, outgoing=True)
async def Fingers(e):
    if len(e.text.split(" ")) > 1:
        message = ' '.join(e.text.split(" ")[1:])
    else:
        await e.edit("Give some text!")
        return
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

@ehandler.on(command="cowsay", hasArgs=True, outgoing=True)
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if len(e.text.split(" ")) < 2:
        return

    splits = e.text.split(" ")
    arg = splits[1]
    tch = splits

    if arg == "cow":
        arg = "default"
    elif arg not in cow.COWACTERS:
        arg = "default"
    else:
        tch = splits[1:]
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(' '.join(tch)).replace('`', '´')}`")
    
@ehandler.on(command="cowthink", hasArgs=True, outgoing=True)
async def think(cowmsg):
    """ For .cowthink module, userbot wrapper for cow which thinks of things. """
    if len(e.text.split(" ")) < 2:
        return

    splits = e.text.split(" ")
    arg = splits[1]
    tch = splits

    if arg == "cow":
        arg = "default"
    elif arg not in cow.COWACTERS:
        arg = "default"
    else:
        tch = splits[1:]
    cheese = cow.get_cow(arg)
    cheese = cheese(thoughts=True)

    await cowmsg.edit(f"`{cheese.milk(' '.join(tch)).replace('`', '´')}`")
    
@ehandler.on(command="figlet", hasArgs=True, outgoing=True)
async def figlet(figletmsg):
    """ For .figlet module. """
    if len(e.text.split(" ")) < 2:
        return

    splits = e.text.split(" ")
    arg = splits[1]
    tch = splits

    if arg not in Figlet.getFonts(Figlet()):
        arg = "slant"
    else:
        tch = splits[1:]

    f = Figlet(font=arg)
    ft =  f.renderText(' '.join(tch))
    await figletmsg.edit(f"`\n{ft}`")
    
@ehandler.on(command="mock", hasArgs=True, outgoing=True)
async def spongemocktext(mock):
    if not mock.text[0].isalpha() and mock.text[0] in ("."):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(mock.text.split(" ")) > 1:
            message = ' '.join(mock.text.split(" ")[1:])
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

@ehandler.on(command="clap", hasArgs=True, outgoing=True)
async def claptext(memereview):  # clap
    if not memereview.text[0].isalpha() and memereview.text[0] in ("."):
        textx = await memereview.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(memereview.text.split(" ")) > 1:
            message = ' '.join(memereview.text.split(" ")[1:])
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)

@ehandler.on(command="type", hasArgs=True, outgoing=True)
async def typewriter(typew):
    if not typew.text[0].isalpha() and typew.text[0] in ("."):
        textx = await typew.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(typew.text.split(" ")) > 1:
            message = ' '.join(typew.text.split(" ")[1:])
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

@ehandler.on(command="rs", hasArgs=True, outgoing=True)
async def retard(dum):
    if not dum.text[0].isalpha() and dum.text[0] in ("."):
        try:
            from .correction import DUM_LIST
        except:
            await dum.edit("`u retar? pls geb correction modul!`")
            return
        textx = await dum.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(dum.text.split(" ")) > 1:
            message = ' '.join(dum.text.split(" ")[1:])
        elif textx:
            message = textx.text
        else:
            await typew.edit("`gib text to turn eet to retard spik!`")
            return
        # reverse DUM_LIST
        MUD_LIST = {}
        for k in DUM_LIST:
            if not DUM_LIST[k] in MUD_LIST:
                MUD_LIST[DUM_LIST[k]] = k
        print(MUD_LIST)
        fixedtext = ""
        for word in textx.text.split():
            if word in MUD_LIST:
                word = MUD_LIST[word]
            fixedtext = f"{fixedtext} {word}"
        fixedtext = fixedtext.lstrip()
        if fixedtext != textx:
            await dum.edit(fixedtext)
        else:
            await dum.edit("`dis message is in retard spik alredy!`")

@ehandler.on(command="shout", hasArgs=True, outgoing=True)
async def shout(request):
    if not request.text[0].isalpha() and request.text[0] in ("."):
        textx = await request.get_reply_message()
        message = "vpr.pattern_match.group(1)"
        if len(request.text.split(" ")) > 1:
            message = ' '.join(request.text.split(" ")[1:])
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

register_module_desc("Memes! This module contains text-based stuff.")
register_cmd_usage("vapor", "<text or reply>", "Vaporize everything!")
register_cmd_usage("str", "<text or reply>", "Stretch it.")
register_cmd_usage("zal", "<text or reply>", "Invoke the feeling of chaos.")
register_cmd_usage("point", "<text>", "Point at something with a nice emoji gradient.")
register_cmd_usage("cowsay", "<optional: character> <text>", "Cow which says things.")
register_cmd_usage("cowthink", "<optional: character> <text>", "Cow which thinks of things.")
register_cmd_usage("figlet", "<optional: font> <text>", "Large text.")
register_cmd_usage("mock", "<text or reply>", "Do it and find the real fun.")
register_cmd_usage("clap", "<text or reply>", "Praise people!")
register_cmd_usage("shout", "<text or reply>", "A little piece of fun wording! Give a loud shout out in the chatroom.")
register_module_info(
    name="Memes - text",
    authors="githubcatw, @BottomTextBot, Haklerman",
    version=VERSION
)