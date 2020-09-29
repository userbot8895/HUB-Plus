# disease
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

import time
import random

from userbot import tgclient, MODULE_DESC, MODULE_DICT
from telethon.events import NewMessage
from os.path import basename
import os

def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

# temporary, until nuno says how to add stuff to config
HOMIES = []
VIRUS = "televirus"

@tgclient.on(NewMessage(outgoing=True, pattern=r"^.infect"))
async def infect(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		replymsg = await event.get_reply_message()
		if replymsg:
			open('patients.txt', 'a').close()
			if replymsg.sender.id == event.sender.id:
				await event.edit("Decided to end your life? I won't let you.")
				return
			rf=open("patients.txt", "r", encoding="utf-8")
			read=rf.read()
			rf.close()
			if f"[{replymsg.sender.first_name}](tg://user?id={replymsg.sender.id})" in read:
				await event.edit(f"{replymsg.sender.first_name} was already infected by you or someone you merged patients with!")
				return
			if replymsg.sender.id in HOMIES:
				await event.edit(f"Your homies have natural immunity against the {VIRUS}.")
				return
			f=open("patients.txt","a+", encoding="utf-8")
			f.write(f"[{replymsg.sender.first_name}](tg://user?id={replymsg.sender.id})\n")
			f.close()
			await replymsg.reply(f"{replymsg.sender.first_name}, you are now infected with the {VIRUS}!")
			await event.delete()
		else:
			await event.edit("I don't know whom to infect!")
		
@tgclient.on(NewMessage(outgoing=True, pattern=r"^.infshare"))
async def share(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		await event.client.send_file(
			event.chat_id,
			"patients.txt",
			caption=f"This is a list of patients infected with the {VIRUS}.\
			\nReply with .infmerge to add the {VIRUS}'s patients to your own virus' patient list."
        )
		await event.delete()
		
@tgclient.on(NewMessage(outgoing=True, pattern=r"^.infmerge"))
async def infmerge(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		replymsg = await event.get_reply_message()
		if replymsg:
			if replymsg.media:
				await event.edit("`Downloading file...`")

				downloaded_file_name = await bot.download_media(
					replymsg,
					"deldog_temp",
					progress_callback=progress
				)
				their_list = None
				with open(downloaded_file_name, "r", encoding="utf-8") as fd:
					their_list = fd.readlines()
				os.remove(downloaded_file_name)

				await event.edit("`Reading list...`")
				open('patients.txt', 'a').close()
				with open ("patients.txt", "r", encoding="utf-8") as rf:
					ours=rf.read()
				await event.edit("`Merging...`")
				pats = 0;
				with open ("patients.txt", "a", encoding="utf-8") as app:
					for pat in their_list:
						await event.respond(pat)
						if not pat in ours:
							app.write(pat)
							pats = pats + 1
				if pats != 0:
					await event.edit(f"The {VIRUS} just infected {pats} more patients from {replymsg.sender.first_name}'s list!")
				else:
					await event.edit(f"Everyone who was infected by {replymsg.sender.first_name} were already in the list!")
			else:
				await event.edit("Reply to a message containing patients.txt!")
		else:
			await event.edit("I don't know whom to merge lists with!")

@tgclient.on(NewMessage(outgoing=True, pattern=r"^.infstats"))
async def infected(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		rf=open("patients.txt", "r", encoding="utf-8")
		read=rf.read()
		rf.close()
		reply = f"List of people infected with the {VIRUS}:\n{read}"
		await event.edit(reply[0:4090])

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Spread your own plague across Telegram!"})
MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".infect\
    \nUsage: Infect someone\
	.infstats\
    \nUsage: Stats on the people you infected\
	.infmerge\
    \nUsage: Merge a patient list\
	.infshare\
    \nUsage: Share a patient listy"})