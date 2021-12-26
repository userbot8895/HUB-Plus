# report
# HUB++
# Licensed under the DBBPL
# Originally from github.com/Javes786/javes-2.0/blob/main/userbot/modules/call_admin.py, ported to HyperUBot by githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from telethon.tl.types import ChannelParticipantsAdmins

ehandler = EventHandler()
VERSION = "2022.1"

@ehandler.on(command="report", hasArgs=False, outgoing=True)
async def flash(event):
	if event.fwd_from:
		return
	mentions = "Reported to admins."
	chat = await event.get_input_chat()
	async for x in tgclient.iter_participants(chat, filter=ChannelParticipantsAdmins):
		mentions += f"[\u2063](tg://user?id={x.id})"
	reply_message = None
	if event.reply_to_msg_id:
		reply_message = await event.get_reply_message()
		await reply_message.reply(mentions)
	else:
		await event.reply(mentions)
	await event.delete()
 
register_module_desc("Report things to admins.")
register_cmd_usage("report", "", "Report a message")
register_module_info(
    name="Report",
    authors="githubcatw and the Javes 2 team",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')