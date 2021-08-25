# scramble
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import random
import re

from telethon.events import NewMessage
from os.path import basename
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler

ehandler = EventHandler()
VERSION = "2021.8 beta 1" 

@ehandler.on(command="scramble", hasArgs=True, outgoing=True)
async def scramble_message(e):
    reply_message = await e.get_reply_message()
    text = e.split(" ")[1] or reply_message.text
    words = re.split(r"\s", text)
    scrambled = map(scramble_word, words)
    text = ' '.join(scrambled)
    await e.edit(text)


def scramble_word(word):
    if len(word) < 4:
        return word

    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = list(word[1:-1])
    random.shuffle(middle_letters)

    return first_letter + ''.join(middle_letters) + last_letter

register_module_desc("Scramble text.")
register_cmd_usage("scramble", "<text>", "Scramble text.")
register_module_info(
    name="Scramble",
    authors="githubcatw, help from prototype74",
    version=VERSION
)