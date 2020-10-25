# chats (extension)
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage
from os.path import basename

@tgclient.on(NewMessage(outgoing=True, pattern="^\.inactive$"))
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

@tgclient.on(NewMessage(outgoing=True, pattern="^\.pinact ([\s\S]*)$"))
async def forceactive(act):
    if not act.text[0].isalpha() and act.text[0] in ("."):
        chat = None
        message = act.pattern_match.group(1)
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
            reply = "This group is pretty active"
        else:
            reply = reply.rstrip(", ")+" "
            reply = reply+message
        await act.respond(reply)
        await act.delete()

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Extra commands for the chat module."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
        ".inactive\
    \nUsage: Lists inactive people.\
    \n\n.pinact\
    \nUsage: Pings inactive people."})

MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Chat (extension)', version='1.0')})