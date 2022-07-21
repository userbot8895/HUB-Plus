# chats (extension)
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from os.path import basename
from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
ehandler = EventHandler()
VERSION = "2022.2.1" 

@ehandler.on(command="inactive", hasArgs=False, outgoing=True)
async def inactive(act):
    if not act.text[0].isalpha() and act.text[0] in ("."):
        chat = None
        if not hasattr(act.message.to_id, "channel_id"):
            await act.edit("`Nope, it works with channels and groups only.`")
            return
        try:
            chat = await act.client.get_entity(act.chat_id)
        except Exception as e:
            print("Exception:", e)
            await act.edit("`Failed to get chat`")
            return
        chat_id = chat.id
        chat_name = chat.title
        reply = f"Inactive members in {chat_name}:"
        init_reply = reply
        async for user in act.client.iter_participants(chat_id):
            if str(user.status) == "UserStatusOffline()" or str(user.status) == "UserStatusLastMonth()":
                data = user.first_name
                if user.last_name is not None:
                    data = data + " " + user.last_name
                if user.username is not None:
                    data = "@" + user.username
                else:
                    data = f"[{data}](tg://user?id={user.id})"
                newrep = reply + f"\n- {data}"
                if not len(newrep) > 4093:
                    reply = newrep
                else:
                    reply = reply + "- ..."
        if reply is init_reply:
            reply = "This group is pretty active."
        await act.edit(reply)

@ehandler.on(command="pinact", hasArgs=True, outgoing=True)
async def forceactive(act):
    if not act.text[0].isalpha() and act.text[0] in ("."):
        chat = None
        if not hasattr(act.message.to_id, "channel_id"):
            await act.edit("`Nope, it works with channels and groups only.`")
            return
        try:
            chat = await act.client.get_entity(act.chat_id)
        except Exception as e:
            print("Exception:", e)
            await act.edit("`Failed to get chat`")
            return
        chat_id = chat.id
        chat_name = chat.title
        reply = ""
        init_reply = reply
        async for user in act.client.iter_participants(chat_id):
            if str(user.status) == "UserStatusOffline()" or str(user.status) == "UserStatusLastMonth()":
                data = user.first_name
                if user.last_name is not None:
                    data = data + " " + user.last_name
                if user.username is not None:
                    data = "@" + user.username
                else:
                    data = f"[{data}](tg://user?id={user.id})"
                newrep = reply + f"{data}, "
                if not len(newrep+message) > 4093:
                    reply = newrep
                else:
                    reply = reply
        if reply is init_reply:
            reply = "`This group is pretty active`"
        else:
            reply = reply.rstrip(", ")+" "
            reply = reply+message
        await act.respond(reply)
        await act.delete()

@ehandler.on(command="dinact", hasArgs=False, outgoing=True)
async def delinactive(act):
    if not act.text[0].isalpha() and act.text[0] in ("."):
        chat = None
        if not hasattr(act.message.to_id, "channel_id"):
            await act.edit("`Nope, it works with channels and groups only.`")
            return
        try:
            chat = await act.client.get_entity(act.chat_id)
        except Exception as e:
            print("Exception:", e)
            await act.edit("`Failed to get chat`")
            return
        chat_id = chat.id
        chat_name = chat.title
        dels = 0
        async for user in act.client.iter_participants(chat_id):
            if str(user.status) == "UserStatusOffline()" or str(user.status) == "UserStatusLastMonth()":
                dels = dels + 1
                await act.client(EditBannedRequest(chat, user, ChatBannedRights(
                    until_date=None,
                    view_messages=True
                )))
        if dels == 0:
            reply = "This group is pretty active."
        else:
            reply = f"Kicked {dels} user{'s' if dels > 1 else ''}."
        await act.edit(reply)

register_module_desc("Extra commands for the chat module.")
register_cmd_usage("inactive", "", "Lists inactive people.")
register_cmd_usage("pinact", "", "Pings inactive people.")
register_cmd_usage("dinact", "", "Kicks inactive people.")
register_module_info(
    name="Chat (extension)",
    authors="githubcatw, Haklerman, help from prototype74",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')