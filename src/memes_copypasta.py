# memes (copypasta)
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

@tgclient.on(NewMessage(outgoing=True, pattern="^.bt$"))
async def bluetext(bt_e):
    if not bt_e.text[0].isalpha() and bt_e.text[0] in ("."):
        if await bt_e.get_reply_message() and bt_e.is_group:
            await bt_e.edit(
                "/BLUE /TEXT /MUST /CLICK\n"
                "/ARE /YOU /A /STUPID /COW /WHICH /IS /ATTRACTED /TO /COLORS ?"
            )

@tgclient.on(NewMessage(outgoing=True, pattern="^.gei$"))
async def isgei(gei):
    if not gei.text[0].isalpha() and gei.text[0] in ("."):
        if await gei.get_reply_message() and gei.is_group or gei.to_id:
            await gei.edit("`┈┈┈╭━━━━━╮┈┈┈┈┈\n"
                           "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
                           "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
                           "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
                           "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
                           "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
                           "┈┈┈┃┊┃╰━━┫┈NIGGA U GEY\n"
                           "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈`")

@tgclient.on(NewMessage(outgoing=True, pattern="^.uno$"))
async def uno(gei):
    if not gei.text[0].isalpha() and gei.text[0] in ("."):
        if await gei.get_reply_message() and gei.is_group or gei.to_id:
            await gei.edit("```⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆\n"+
                           "⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿\n"+
                           "⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹\n"+
                           "⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"+
                           "⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷\n"+
                           "⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟\n"+
                           "⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃\n"+
                           "⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠\n"+
                           "⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾\n"+
                           "⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿\n"+
                           "⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿\n"+
                           "⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿\n"+
                           "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿\n"+
                           "⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿\n"+
                           "⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿\n"+
                           "⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿\n"+
                           "⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟```")

@tgclient.on(NewMessage(outgoing=True, pattern="^.nou$"))
async def isgei(gei):
    if not gei.text[0].isalpha() and gei.text[0] in ("."):
        if await gei.get_reply_message() and gei.is_group or gei.to_id:
            await gei.edit("`┈╭╮╭╮\n"
                           "┈┃┃┃┃\n"
                           "╭┻┗┻┗╮\n"
                           "┃┈▋┈▋┃\n"
                           "┃┈╭▋━╮━╮\n"
                           "┃┈┈╭╰╯╰╯╮\n"
                           "┫┈┈  NoU\n"
                           "┃┈╰╰━━━━╯\n"
                           "┗━━┻━┛`")
                           
                           
@tgclient.on(NewMessage(outgoing=True, pattern="^.say (.*)"))
async def say(sae):
    if not sae.text[0].isalpha() and sae.text[0] in ("."):
    	text = sae.pattern_match.group(1)
    	if len(text) > 19:
        	await sae.edit("`I can't say that.`")
    	if len(text) < 20:
        	await sae.edit(f"`|^^^^^|<({text})\n"
                                           "| x x |\n"
                                           "|  o  |\n"
                                           "|_____|\n"
                                           "==| |==\n"
                                           "  | |\n"
                                           "  W W`")

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Memes! This module contains copy-pasta."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".bt\
    \nUsage: Believe me, you will find this useful.\
    \n\n.gei\
    \nUsage: Use this as a reply if your friend does something gei.\
    \n\n.nou\
    \nUsage: Return whatever someone said to themself.\
    \n\n.say\
    \nUsage: Say something.\
    \n\n.uno\
    \nUsage: Reverse card! Like .nou, for the unaware."
})
MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Memes (copypasta)', version='1.0')})