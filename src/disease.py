# disease
# HUB++
# Licensed under the DBBPL
# (C) 2021 githubcatw

import time
import random

from os.path import basename
from os.path import join as pathjoin
import os
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from userbot.sysutils.configuration import getConfig
from userbot import getConfig
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from datetime import datetime, timedelta
from telethon.errors import UserAdminInvalidError
from userbot.sysutils.configuration import getConfig

ehandler = EventHandler()
VERSION = "2022.2.1"
TEMP_DL_DIR = getConfig("TEMP_DL_DIR")
VIRUS = None
HOMIES = None

if getConfig("USERDATA") == None:
    raise Exception("disease requires a user data folder. Please set USERDATA in your config.")

FILES = pathjoin(getConfig("USERDATA"),"plus")

if not os.path.isdir(FILES):
    os.makedirs(FILES)

def loadData():
	global VIRUS, HOMIES
	# attempt to load PlusConfig
	try:
		from userbot.config import PlusConfig as pc
		VIRUS = pc.VIRUS
		HOMIES = pc.HOMIES
	# if it doesn't exist, load using getConfig
	except ImportError:
		VIRUS = getConfig("VIRUS")
		HOMIES = getConfig("HOMIES")

def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

@ehandler.on(command="infect", hasArgs=True, outgoing=True)
async def infect(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		replymsg = await event.get_reply_message()
		if replymsg:
			open(pathjoin(FILES,"patients.txt"), 'a').close()
			if not hasattr(replymsg.sender, 'first_name'):
				await event.edit("You can only infect people.")
				return
			if replymsg.sender.id == event.sender.id:
				await event.edit("Decided to end your life? I won't let you.")
				return
			rf=open(pathjoin(FILES,"patients.txt"), "r", encoding="utf-8")
			read=rf.read()
			rf.close()
			if f"[{replymsg.sender.first_name}](tg://user?id={replymsg.sender.id})" in read:
				await event.edit(f"{replymsg.sender.first_name} was already infected by you or someone you merged patients with!")
				return
			if replymsg.sender.id in HOMIES:
				await event.edit(f"Your homies have natural immunity against the {VIRUS}.")
				return
			f=open(pathjoin(FILES,"patients.txt"),"a+", encoding="utf-8")
			f.write(f"[{replymsg.sender.first_name}](tg://user?id={replymsg.sender.id})\n")
			f.close()
			try:
				await doInfect(event, replymsg)
				await replymsg.reply(f"{replymsg.sender.first_name}, you are now infected with the {VIRUS}! Now you can't send stickers, GIFs, use inline bots or embed links.")
				await event.delete()
			except UserAdminInvalidError:
				await replymsg.reply(f"{replymsg.sender.first_name}, you are now infected with the {VIRUS}!")
				await event.delete()
		else:
			await event.edit("I don't know whom to infect!")

async def isInfected(name, id):
	open(pathjoin(FILES,"patients.txt"), 'a').close()
	rf=open(pathjoin(FILES,"patients.txt"), "r", encoding="utf-8")
	read=rf.read()
	rf.close()
	return f"[{name}](tg://user?id={id})" in read

async def doInfect(event, mess):
	peer_id = event.chat_id
	rights = ChatBannedRights(
		until_date=datetime.now() + timedelta(minutes=20),
		send_stickers=True,
		send_gifs=True,
		send_games=True,
		send_inline=True,
		embed_links=True
	)
	await event.client(EditBannedRequest(peer_id, mess.sender, rights))

@ehandler.on(command="infshare", hasArgs=False, outgoing=True)
async def share(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		await event.client.send_file(
			event.chat_id,
			pathjoin(FILES,"patients.txt"),
			caption=f"This is a list of patients infected with the {VIRUS}.\
			\nReply with .infmerge to add the {VIRUS}'s patients to your own virus' patient list."
        )
		await event.delete()


@ehandler.on(command="infmerge", hasArgs=True, outgoing=True)
async def infmerge(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		replymsg = await event.get_reply_message()
		if replymsg:
			if replymsg.media:
				await event.edit("`Downloading file...`")

				downloaded_file_name = await event.client.download_media(
					replymsg,
					pathjoin(TEMP_DL_DIR, "patients.txt"),
					progress_callback=progress
				)
				their_list = None
				with open(downloaded_file_name, "r", encoding="utf-8") as fd:
					their_list = fd.readlines()
				os.remove(downloaded_file_name)

				await event.edit("`Reading list...`")
				open(pathjoin(FILES,"patients.txt"), 'a').close()
				with open(pathjoin(FILES,"patients.txt"), "r", encoding="utf-8") as rf:
					ours=rf.read()
				await event.edit("`Merging...`")
				pats = 0;
				with open(pathjoin(FILES,"patients.txt"), "a", encoding="utf-8") as app:
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

@ehandler.on(command="infstats", hasArgs=False, outgoing=True)
async def infected(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		rf=open(pathjoin(FILES,"patients.txt"), "r", encoding="utf-8")
		read=rf.read()
		rf.close()
		reply = f"List of people infected with the {VIRUS}:\n{read}"
		await event.edit(reply[0:4090])

@ehandler.on(command="patients", hasArgs=False, outgoing=True)
async def infected(event):
	if not event.text[0].isalpha() and event.text[0] in ("."):
		rf=open(pathjoin(FILES,"patients.txt"), "r", encoding="utf-8")
		read=rf.read()
		rf.close()
		reply = f"List of people infected with the {VIRUS}:\n{read}"
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

loadData()

_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')