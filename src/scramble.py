# scramble
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

import random
import re

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
from os.path import basename

@tgclient.on(NewMessage(pattern=r"^.scramble(\s+[\S\s]+|$)", outgoing=True))
async def scramble_message(e):
    reply_message = await e.get_reply_message()
    text = e.pattern_match.group(1) or reply_message.text
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

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Scrambles text."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
        ".scramble <text>\
    \nUsage: Scrambles text."})
