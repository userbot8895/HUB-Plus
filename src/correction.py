# correction
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
import re
from sre_constants import error as sre_err
from os.path import basename

DUM_LIST = {
	"wut": "what",
	"wat": "what",
	"sed": "sad",
	"wen": "when",
	"gib": "give",
	"sar": "sir",
	"nao": "now"
}

DELIMITERS = ("/", ":", "|", "_")

@tgclient.on(NewMessage(outgoing=True, pattern="^.dum"))
async def didyoumean(dum):
	if not dum.text[0].isalpha() and dum.text[0] in ("."):
		textx = await dum.get_reply_message()
		if not textx:
			await dum.edit("Reply to a message to correct it!")
			return
		fixedtext = textx.text
		for word in DUM_LIST:
			fixedtext = fixedtext.replace(word, f"**{DUM_LIST[word]}**")
		print(f"fix:\n{fixedtext}\norig:\n{textx}")
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


@tgclient.on(NewMessage(outgoing=True, pattern="^\.s"))
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


MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Correct people."})
MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".s<delimiter><old word(s)><delimiter><new word(s)>\
    \nUsage: Replaces a word or words using sed.\
    \nDelimiters: `/, :, |, _`\
    \n\n.dum\
    \nUsage: An automated version of .s that replaces common chat slang."})