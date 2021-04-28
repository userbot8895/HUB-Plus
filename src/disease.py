# disease
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import time
import random

from userbot import tgclient
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage
from os.path import basename
from os.path import join as pathjoin
import os
from userbot.config import PlusConfig as pc
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from userbot.config import TEMP_DL_DIR

ehandler = EventHandler()
VERSION = "2021.4 for HUB 4.x"

if not os.path.isdir("plus/"):
    os.makedirs("plus/")

def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

@ehandler.on(command="infect", hasArgs=True, outgoing=True)
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
			if replymsg.sender.id in pc.HOMIES:
				await event.edit(f"Your homies have natural immunity against the {pc.VIRUS}.")
				return
			f=open(pathjoin("plus","patients.txt"),"a+", encoding="utf-8")
			f.write(f"[{replymsg.sender.first_name}](tg://user?id={replymsg.sender.id})\n")
			f.close()
			await replymsg.reply(f"{replymsg.sender.first_name}, you are now infected with the {pc.VIRUS}!")
			await event.delete()
		else:
			await event.edit("I don't know whom to infect!")
		
@ehandler.on(command="infshare", hasArgs=False, outgoing=True)
async def share(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		await event.client.send_file(
			event.chat_id,
			"patients.txt",
			caption=f"This is a list of patients infected with the {pc.VIRUS}.\
			\nReply with .infmerge to add the {pc.VIRUS}'s patients to your own virus' patient list."
        )
		await event.delete()
		
@ehandler.on(command="infmerge", hasArgs=True, outgoing=True)
async def infmerge(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		replymsg = await event.get_reply_message()
		if replymsg:
			if replymsg.media:
				await event.edit("`Downloading file...`")

				downloaded_file_name = await bot.download_media(
					replymsg,
					pathjoin(TEMP_DL_DIR, "patients.txt"),
					progress_callback=progress
				)
				their_list = None
				with open(downloaded_file_name, "r", encoding="utf-8") as fd:
					their_list = fd.readlines()
				os.remove(downloaded_file_name)

				await event.edit("`Reading list...`")
				open(pathjoin("plus","patients.txt"), 'a').close()
				with open(pathjoin("plus","patients.txt"), "r", encoding="utf-8") as rf:
					ours=rf.read()
				await event.edit("`Merging...`")
				pats = 0;
				with open(pathjoin("plus","patients.txt"), "a", encoding="utf-8") as app:
					for pat in their_list:
						await event.respond(pat)
						if not pat in ours:
							app.write(pat)
							pats = pats + 1
				if pats != 0:
					await event.edit(f"The {pc.VIRUS} just infected {pats} more patients from {replymsg.sender.first_name}'s list!")
				else:
					await event.edit(f"Everyone who was infected by {replymsg.sender.first_name} were already in the list!")
			else:
				await event.edit("Reply to a message containing patients.txt!")
		else:
			await event.edit("I don't know whom to merge lists with!")

@ehandler.on(command="infstats", hasArgs=False, outgoing=True)
async def infected(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		rf=open(pathjoin("plus","patients.txt"), "r", encoding="utf-8")
		read=rf.read()
		rf.close()
		reply = f"List of people infected with the {pc.VIRUS}:\n{read}"
		await event.edit(reply[0:4090])

register_module_desc("Spread your own plague across Telegram!")
register_cmd_usage("infect", "(replying to someone)", "Infect someone.")
register_cmd_usage("infstats", "", "Stats on the people you infected.")
register_cmd_usage("infmerge", "(replying to a patients.txt file)", "Merge a patient list with yours.")
register_cmd_usage("infshare", "", "Share your patient list. Check out our list sharing group here: t.me/joinchat/V7NyfpJVUXSiMSeN")
register_module_info(
    name="Disease",
    authors="githubcatw, help from prototype74",
    version=VERSION
)