from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
import os.path
from os import path
import os
import json
from os.path import basename

@tgclient.on(NewMessage(pattern=r"^\.save(?: |$)(\w+)(.*)", outgoing=True))
async def save(event):
    name = event.pattern_match.group(1)
    text = event.pattern_match.group(2).lstrip()
    textx = await event.get_reply_message()
    npath = "notes/" + name + ".txt"
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

@tgclient.on(NewMessage(pattern=r"^\.note (.*)", outgoing=True))
async def note(event):
    name = event.pattern_match.group(1)
    npath = "notes/" + name + ".txt"
    if not path.exists(npath):
        await event.edit(f"Note `{name}` doesn't exist.\n"+
                           f"Type `.save {name} <text> to create the note.")
        return
    f=open(npath,"r+")
    await event.edit(f.read())

@tgclient.on(NewMessage(pattern=r"^\.n (.*)", outgoing=True))
async def note_short(event):
    name = event.pattern_match.group(1)
    npath = "notes/" + name + ".txt"
    if not path.exists(npath):
        await event.edit(f"Note `{name}` doesn't exist.\n"+
                           f"Type `.save {name} <text> to create the note.")
        return
    f=open(npath,"r+")
    await event.edit(f.read())

@tgclient.on(NewMessage(pattern=r"^\.notes", outgoing=True))
async def notes(mention):
    reply = "You have these notes:\n\n"
    allnotes = os.listdir("notes/")
    if not allnotes:
        reply = "You have no notes."
    else:
        for n in allnotes:
            reply = reply + f"- {n.split('.')[0]}\n"
        reply = reply + "\nGet any of these notes by typing `.note <notename>`"
    await mention.edit(reply)
    
@tgclient.on(NewMessage(pattern=r"^\.delnote (.*)", outgoing=True))
async def delnote(event):
    name = event.pattern_match.group(1)
    notes = [name]
    if " " in name:
        notes = name.split()
    deleted = 0
    delnames = ""
    for n in notes:
        npath = "notes/" + n + ".txt"
        if not path.exists(npath):
            await event.edit(f"Note `{n}` doesn't exist.\n"+
                               f"Type `.save {n} <text> to create the note.")
            return
        os.remove(npath)
        deleted = deleted + 1
        delnames = delnames + n + ", "
    await event.edit(f"Deleted note{'s:' if deleted > 1 else ''} `{delnames.rstrip(', ')}`.")
    
MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Save text and quickly send it later."})
MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".note <notename>\
    \nUsage: Send a note.\
    \n\n.save <notename> <text>\
    \nUsage: Save a note.\
    \n\n.notes\
    \nUsage: Get all of your notes.\
    \n\n.delnote <notename>\
    \nUsage: Delete a note."})