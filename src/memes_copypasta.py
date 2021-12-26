# memes (copypasta)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from os.path import basename

import asyncio
import time

ehandler = EventHandler()
VERSION = "2022.1" 

@ehandler.on(command="bt", hasArgs=False, outgoing=True)
async def bluetext(bt_e):
    if not bt_e.text[0].isalpha() and bt_e.text[0] in ("."):
        if await bt_e.get_reply_message() and bt_e.is_group:
            await bt_e.edit(
                "/BLUE /TEXT /MUST /CLICK\n"
                "/ARE /YOU /A /STUPID /COW /WHICH /IS /ATTRACTED /TO /COLORS ?"
            )

@ehandler.on(command="gei", hasArgs=False, outgoing=True)
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

@ehandler.on(command="uno", hasArgs=False, outgoing=True)
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
                           
@ehandler.on(command="fortnite", hasArgs=False, outgoing=True)
async def uno(gei):
    if not gei.text[0].isalpha() and gei.text[0] in ("."):
        if await gei.get_reply_message() and gei.is_group or gei.to_id:
            await gei.edit("⠀⠀⠀⣀⣤\n"+
                           "⠀⠀⠀⠀⣿⠿⣶\n"+
                           "⠀⠀⠀⠀⣿⣿⣀\n"+
                           "⠀⠀⠀⣶⣶⣿⠿⠛⣶\n"+
                           "⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤\n"+
                           "⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀\n"+
                           "⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿\n"+
                           "⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉\n"+
                           "⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿\n"+
                           "⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿\n"+
                           "⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤\n"+
                           "⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿\n"+
                           "⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿\n"+
                           "⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿\n"+
                           "⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿\n"+
                           "⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿\n"+
                           "⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿\n"+
                           "⠀⠀⠀⠛⠛\n"+
                           "\n"+
                           "\n"+
                           "⠀⠀⠀⣀⣶⣀\n"+
                           "⠀⠀⠀⠒⣛⣭\n"+
                           "⠀⠀⠀⣀⠿⣿⣶\n"+
                           "⠀⣤⣿⠤⣭⣿⣿\n"+
                           "⣤⣿⣿⣿⠛⣿⣿⠀⣀\n"+
                           "⠀⣀⠤⣿⣿⣶⣤⣒⣛\n"+
                           "⠉⠀⣀⣿⣿⣿⣿⣭⠉\n"+
                           "⠀⠀⣭⣿⣿⠿⠿⣿\n"+
                           "⠀⣶⣿⣿⠛⠀⣿⣿\n"+
                           "⣤⣿⣿⠉⠤⣿⣿⠿\n"+
                           "⣿⣿⠛⠀⠿⣿⣿\n"+
                           "⣿⣿⣤⠀⣿⣿⠿\n"+
                           "⠀⣿⣿⣶⠀⣿⣿⣶\n"+
                           "⠀⠀⠛⣿⠀⠿⣿⣿\n"+
                           "⠀⠀⠀⣉⣿⠀⣿⣿\n"+
                           "⠀⠶⣶⠿⠛⠀⠉⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⣀⣿\n"+
                           "⠀⠀⠀⠀⠀⣶⣿⠿\n"+
                           "\n"+
                           "⠀⠀⠀⠀⠀⠀     ⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿\n"+
                           "⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿\n"+
                           "\n"+
                           "⠀⠀⣀\n"+
                           "⠀⠿⣿⣿⣀\n"+
                           "⠀⠉⣿⣿⣀\n"+
                           "⠀⠀⠛⣿⣭⣀⣀⣤\n"+
                           "⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀\n"+
                           "⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶\n"+
                           "⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉\n"+
                           "⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿\n"+
                           "⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿\n"+
                           "⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿\n"+
                           "⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿\n"+
                           "⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀\n"+
                           "⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶\n"+
                           "⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿\n"+
                           "⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉\n"+
                           "⣀⣶⣿⠛\n"+
                           "\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣀⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉\n"+
                           "⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉\n"+
                           "⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿\n"+
                           "⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤\n"+
                           "⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉\n"+
                           "\n"+
                           "⠀⠀⠀⠀⠀⠀⣤⣶⣶\n"+
                           "⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀\n"+
                           "⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿\n"+
                           "⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿\n"+
                           "⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛\n"+
                           "⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀\n"+
                           "⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⣀⣿⣿\n"+
                           "⠀⠀⠀⠀⠤⣿⠿⠿⠿\n"+
                           "\n"+
                           "⠀⠀⠀⠀⣀\n"+
                           "⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤\n"+
                           "⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀\n"+
                           "⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀\n"+
                           "⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉\n"+
                           "\n"+
                           "⠀⠀⠀⠀⠀⠀⣶⣿⣶\n"+
                           "⠀⠀⠀⣤⣤⣤⣿⣿⣿\n"+
                           "⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶\n"+
                           "⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶\n"+
                           "⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿\n"+
                           "⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶\n"+
                           "⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤\n"+
                           "⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿\n"+
                           "⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉\n"+
                           "⠀⠀⠀⣿⣿⣿⣿⣿⣶\n"+
                           "⠀⠀⠀⠀⣿⠉⠿⣿⣿\n"+
                           "⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿\n"+
                           "⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉\n"+
                           "\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶\n"+
                           "⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶\n"+
                           "⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤\n"+
                           "⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀\n"+
                           "⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿\n"+
                           "⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶\n"+
                           "⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒\n"+
                           "⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉\n"+
                           "⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛\n"+
                           "⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⣿⠛\n"+
                           "⠀⠀⠀⠀⠀⠀⣭⣶\n"+
                           "\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿\n"+
                           "⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀\n"+
                           "⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀\n"+
                           "⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿\n"+
                           "⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛\n"+
                           "\n"+
                           "⠀⠀⠀⣶⣿⣶\n"+
                           "⠀⠀⠀⣿⣿⣿⣀\n"+
                           "⠀⣀⣿⣿⣿⣿⣿⣿\n"+
                           "⣶⣿⠛⣭⣿⣿⣿⣿\n"+
                           "⠛⠛⠛⣿⣿⣿⣿⠿\n"+
                           "⠀⠀⠀⠀⣿⣿⣿\n"+
                           "⠀⠀⣀⣭⣿⣿⣿⣿⣀\n"+
                           "⠀⠤⣿⣿⣿⣿⣿⣿⠉\n"+
                           "⠀⣿⣿⣿⣿⣿⣿⠉\n"+
                           "⣿⣿⣿⣿⣿⣿\n"+
                           "⣿⣿⣶⣿⣿\n"+
                           "⠉⠛⣿⣿⣶⣤\n"+
                           "⠀⠀⠉⠿⣿⣿⣤\n"+
                           "⠀⠀⣀⣤⣿⣿⣿\n"+
                           "⠀⠒⠿⠛⠉⠿⣿\n"+
                           "⠀⠀⠀⠀⠀⣀⣿⣿\n"+
                           "⠀⠀⠀⠀⣶⠿⠿⠛")

@ehandler.on(command="nou", hasArgs=False, outgoing=True)
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
                           
                           
@ehandler.on(command="say", hasArgs=True, outgoing=True)
async def say(sae):
    if not sae.text[0].isalpha() and sae.text[0] in ("."):
    	text = sae.text.split(" ")[1]
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

register_module_desc("Memes! This module contains copypasta.")
register_cmd_usage("bt", "", "Believe me, you will find this useful.")
register_cmd_usage("gei", "", "Use this as a reply if your friend does something gei.")
register_cmd_usage("nou", "", "Return whatever someone said to themself.")
register_cmd_usage("say", "<what to say>", "Say something.")
register_cmd_usage("uno", "", "Reverse card! Like .nou, for the unaware.")
register_cmd_usage("fortnite", "", "Cringydance.exe. Created by Watn3y.")
register_module_info(
    name="Memes - copypasta",
    authors="githubcatw, @BottomTextBot, Watn3y, Haklerman",
    version=VERSION
)

_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')