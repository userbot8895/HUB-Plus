# memes (animated)
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT
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

@tgclient.on(NewMessage(outgoing=True, pattern="^.oof$"))
async def Oof(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Oof"
        for j in range(15):
            t = t[:-1] + "of"
            await e.edit(t)
            
@tgclient.on(NewMessage(outgoing=True, pattern="^.hmm$"))
async def Hmm(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Hmm"
        for j in range(10):
            t = t[:-1] + "mm"
            await e.edit(t)
            
@tgclient.on(NewMessage(outgoing=True, pattern="^.ree$"))
async def Ree(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Ree"
        for j in range(15):
            t = t[:-1] + "ee"
            await e.edit(t)

@tgclient.on(NewMessage(outgoing=True, pattern="^.lool$"))
async def Lol(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "LOL"
        for j in range(15):
            t = t[:-1] + "OL"
            await e.edit(t)
            
@tgclient.on(NewMessage(outgoing=True, pattern="^.gay$"))
async def Gay(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        t = "Gay"
        for j in range(15):
            t = t[:-1] + "ay"
            await e.edit(t)
            
@tgclient.on(NewMessage(outgoing=True, pattern="^.x (.*)$"))
async def Extend(e):
    if not e.text[0].isalpha() and e.text[0] in ("."):
        # get the requested text
        paytext = e.pattern_match.group(1)
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

@tgclient.on(NewMessage(outgoing=True, pattern="^:/$"))
async def kek(keks):
    """ Check yourself ;)"""
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])
        

@tgclient.on(NewMessage(outgoing=True, pattern="^-_-$"))
async def blink(wut):
	uio = ["-", "o"]
	for i in range(1, 15):
		time.sleep(0.3)
		await wut.edit(uio[i % 2] + "_" + uio[i % 2])
		
@tgclient.on(NewMessage(outgoing=True, pattern="^×_×$"))
async def dead(ded):
	uio = ["×", "+"]
	for i in range(1, 15):
		time.sleep(0.3)
		await ded.edit(uio[i % 2] + "_" + uio[i % 2])
        
@tgclient.on(NewMessage(outgoing=True, pattern="^x_x$"))
async def dead(ded):
	uio = ["×", "+"]
	for i in range(1, 15):
		time.sleep(0.3)
		await ded.edit(uio[i % 2] + "_" + uio[i % 2])
		
@tgclient.on(NewMessage(outgoing=True, pattern="^O.o$"))
async def Oo(o):
	uio1 = ["O", "o"]
	uio2 = ["o", "O"]
	for i in range(1, 15):
		time.sleep(0.3)
		await o.edit(uio1[i % 2] + "." + uio2[i % 2])

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Memes! This module contains various animations."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".oof\
    \nUsage: Ooooof\
    \n\n.hmm\
    \nUsage: Hmmmmmm\
    \n\n.lool\
    \nUsage: Loooool\
    \n\n.gay\
    \nUsage: Gaaaaay\
    \n\n.ree\
    \nUsage: Reeeeee\
    \n\n.x <text>\
    \nUsage: Like .oof/.hmm but customizable.\
    \n\n:/\
    \nUsage: Check yourself ;)\
    \n\n-_-\
    \nUsage: wut?\
    \n\n×_×\
    \nUsage: ded\
    \n\nx_x\
    \nUsage: same as ×_×\
    \n\nO.o\
    \nUsage: o.O"
})
