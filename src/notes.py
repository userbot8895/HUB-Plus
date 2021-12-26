# notes
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import os.path
from os import path
import os
import json
from os.path import basename
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from os.path import join as pathjoin
from userbot import getConfig

ehandler = EventHandler()
VERSION = "2021.8"

if getConfig("USERDATA") == None:
    raise Exception("notes requires a user data folder. Please set USERDATA in your config.")

FILES = pathjoin(getConfig("USERDATA"),"plus")

if not os.path.isdir(FILES):
    os.makedirs(FILES)

@ehandler.on(command="save", hasArgs=True, outgoing=True)
async def save(event):
    name = event.text.split(" ")[1]
    text = event.text.split(" ")[2]
    textx = await event.get_reply_message()
    npath = pathjoin(FILES,name + ".txt")
    if not os.path.isdir("notes/"):
        os.makedirs("notes/")
    if path.exists(npath):
        await event.edit(f"Note `{name}` already exists.")
        return
    f=open(npath,"w+")
    if text:
        f.write(text)
        await event.edit(f"Saved note `{name}`.\n"+
                         f"Type `.note {name}` to get it.")
    if textx:
        f.write(parse_markdown(textx.message, textx.entities) if textx.entities is not None else textx.message)
        await event.edit(f"Saved note `{name}`.\n"+
                         f"Type `.note {name}` to get it.")

def parse_markdown(message, entities):
    parsed = message
    goffset = 0
    for e in entities:
        offset = e.offset + goffset
        length = offset+e.length
        if str(type(e)) == "<class 'telethon.tl.types.MessageEntityBold'>":
            parsed = parsed[0:offset]+"**"+parsed[offset:length]+"**"+parsed[length:len(parsed)]
            goffset = goffset + 4
        elif str(type(e)) == "<class 'telethon.tl.types.MessageEntityItalic'>":
            parsed = parsed[0:offset]+"__"+parsed[offset:length]+"__"+parsed[length:len(parsed)]
            goffset = goffset + 4
        elif str(type(e)) == "<class 'telethon.tl.types.MessageEntityCode'>":
            parsed = parsed[0:offset]+"`"+parsed[offset:length]+"`"+parsed[length:len(parsed)]
            goffset = goffset + 2
        elif str(type(e)) == "<class 'telethon.tl.types.MessageEntityStrike'>":
            parsed = parsed[0:offset]+"~~"+parsed[offset:length]+"~~"+parsed[length:len(parsed)]
            goffset = goffset + 4
    return parsed

@ehandler.on(command="note", hasArgs=True, outgoing=True)
async def note(event):
    notes = event.text.split(" ")
    if len(notes) < 2:
        await event.edit("Specify the note name.")
        return
    npath = pathjoin(FILES,notes[1] + ".txt")
    if not path.exists(npath):
        await event.edit(f"Note `{name}` doesn't exist.\n"+
                           f"Type `.save {name} <text> to create the note.")
        return
    f=open(npath,"r+")
    await event.edit(f.read())

@ehandler.on(command="n", hasArgs=True, outgoing=True)
async def note_short(event):
    notes = event.text.split(" ")
    if len(notes) < 2:
        await event.edit("Specify the note name.")
        return
    npath = pathjoin(FILES,notes[1] + ".txt")
    if not path.exists(npath):
        await event.edit(f"Note `{name}` doesn't exist.\n"+
                           f"Type `.save {name} <text> to create the note.")
        return
    f=open(npath,"r+")
    await event.edit(f.read())

@ehandler.on(command="notes", hasArgs=True, outgoing=True)
async def notes(mention):
    reply = "You have these notes:\n\n"
    allnotes = os.listdir(FILES)
    if not allnotes:
        reply = "You have no notes."
    else:
        for n in allnotes:
            reply = reply + f"- {n.split('.')[0]}\n"
        reply = reply + "\nGet any of these notes by typing `.note <notename>` or `.n <notename>`."
    await mention.edit(reply)
    
@ehandler.on(command="delnote", hasArgs=False, outgoing=True)
async def delnote(event):
    notes = event.text.split(" ")
    deleted = 0
    delnames = ""
    for n in notes:
        npath = pathjoin(FILES,n + ".txt")
        if not path.exists(npath):
            await event.edit(f"Note `{n}` doesn't exist.")
            return
        os.remove(npath)
        deleted = deleted + 1
        delnames = delnames + n + ", "
    await event.edit(f"Deleted note{'s:' if deleted > 1 else ''} `{delnames if deleted > 1 else delnames.rstrip(', ')}`.")

register_module_desc("Save text and quickly send it later.")
register_cmd_usage("note", "<notename>", "Send a note.")
register_cmd_usage("n", "<notename>", "Send a note.")
register_cmd_usage("save", "<notename> <text>", "Save a note.")
register_cmd_usage("notes", "", "Get all of your notes.")
register_cmd_usage("delnote", "<notename>", "Delete a note.")
register_module_info(
    name="Notes",
    authors="githubcatw, help from prototype74",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')