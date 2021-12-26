# correction
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from telethon.events import NewMessage
import re
from sre_constants import error as sre_err
from os.path import basename
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler

ehandler = EventHandler()
VERSION = "2022.1" 

DUM_LIST = {
    "wut": "what",
    "wat": "what",
    "sed": "sad",
    "wen": "when",
    "gib": "give",
    "sur": "sir",
    "sar": "sir",
    "nao": "now",
    "bes": "best",
    "gab": "gave",
    "bess": "best",
    "dat": "that",
    "da": "the",
    "naice": "nice",
    "dis": "this",
    "hab": "have",
    "eet": "it",
    "et": "it",
    "der": "there",
    "eva": "ever",
    "hao": "how",
    "pls": "please",
    "peru": "pro",
    "nub": "noob",
    "pru": "pro",
    "hemlo": "hello",
    "laik": "like",
    "luv": "love",
    "gud": "good",
    "welcum": "welcome",
    "whalecum": "welcome",
    "plox": "please",
    "meni": "many",
    "ppl": "people",
    "tat": "that",
    "yu": "you",
    "yems": "yes",
}

DELIMITERS = ("/", ":", "|", "_")

@ehandler.on(command="dum", hasArgs=False, outgoing=True)
async def didyoumean(dum):
	if not dum.text[0].isalpha() and dum.text[0] in ("."):
		textx = await dum.get_reply_message()
		if not textx:
			await dum.edit("Reply to a message to correct it!")
			return
		fixedtext = ""
		for word in textx.text.split():
			if word in DUM_LIST:
				word = f"**{DUM_LIST[word]}**"
			fixedtext = f"{fixedtext} {word}"
		fixedtext = fixedtext.lstrip()
		if fixedtext != textx:
			await dum.edit(f"__Did you mean:__\n\n{fixedtext}")
		else:
			await dum.edit("The message is spelled correctly!")

async def separate_sed(sed_string):
    """ Separate sed arguments. """

    if len(sed_string) < 2:
        return

    if (len(sed_string) >= 2 and sed_string[2] in DELIMITERS
            and sed_string.count(sed_string[2]) >= 2):
        delim = sed_string[2]
        start = counter = 3
        while counter < len(sed_string):
            if sed_string[counter] == "\\":
                counter += 1

            elif sed_string[counter] == delim:
                replace = sed_string[start:counter]
                counter += 1
                start = counter
                break

            counter += 1

        else:
            return None

        while counter < len(sed_string):
            if (sed_string[counter] == "\\" and counter + 1 < len(sed_string)
                    and sed_string[counter + 1] == delim):
                sed_string = sed_string[:counter] + sed_string[counter + 1:]
            elif sed_string[counter] == delim:
                replace_with = sed_string[start:counter]
                counter += 1
                break
            counter += 1
        else:
            return replace, sed_string[start:], ""
        flags = ""
        if counter < len(sed_string):
            flags = sed_string[counter:]
        return replace, replace_with, flags.lower()
    return None


@ehandler.on_Pattern(outgoing=True, events=NewMessage, pattern="^\.s", name="s")
async def sed(command):
    if not command.text[0].isalpha() and command.text[0] in ("."):
        sed_result = await separate_sed(command.text)
        textx = await command.get_reply_message()
        if sed_result:
            if textx:
                to_fix = textx.text
            else:
                await command.edit("`Master, I don't have brains. Well you too don't I guess.`")
                return
            repl, repl_with, flags = sed_result

            if not repl:
                await command.edit("`Master, I don't have brains. Well you too don't I guess.`")
                return
            try:
                check = re.match(repl, to_fix, flags=re.IGNORECASE)
                if check and check.group(0).lower() == to_fix.lower():
                    await command.edit("`Boi!, that's a reply. Don't use sed`")
                    return

                if "i" in flags and "g" in flags:
                    text = re.sub(repl, repl_with, to_fix, flags=re.I).strip()
                elif "i" in flags:
                    text = re.sub(repl, repl_with, to_fix, count=1,
                                  flags=re.I).strip()
                elif "g" in flags:
                    text = re.sub(repl, repl_with, to_fix).strip()
                else:
                    text = re.sub(repl, repl_with, to_fix, count=1).strip()
            except sre_err:
                await command.edit("B O I! [Learn Regex](https://regexone.com)")
                return
            if text:
                await command.edit(f"Did you mean? \n\n{text}")

register_module_desc("Correct people.")
register_cmd_usage("s","<delimiter><old word(s)><delimiter><new word(s)>", "Replaces a word or words using sed. No space between .s and argument.\nDelimiters: `/, :, |, _`")
register_cmd_usage("dum", "", "An automated version of .s that replaces common chat slang.")
register_module_info(
    name="Corrections",
    authors="githubcatw, nunopenim, help from prototype74",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')