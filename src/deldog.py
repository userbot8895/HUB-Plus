# deldog
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

import asyncio
from datetime import datetime
import os
import requests

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage
from os.path import basename

def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))

@tgclient.on(NewMessage(outgoing=True, pattern="^\.dog([\s\S]*)"))
async def _(event):
    tmp_dir = "deldog_temp"
    if event.fwd_from:
        return
    if not os.path.isdir(tmp_dir):
        os.makedirs(tmp_dir)
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = "Syntax: `.dog <text>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            await event.edit("`Downloading file...`")
            downloaded_file_name = await bot.download_media(
                previous_message,
                tmp_dir,
                progress_callback=progress
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        await event.edit("Syntax: `.dog <text>`")
    if message == "Syntax: `.dog <text>`":
        await event.edit("Syntax: `.dog <text>`")
        return
    await event.edit("`Uploading...`")
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    end = datetime.now()
    ms = (end - start).seconds
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        await event.edit("Pasted to {} in {} seconds. [link]({}).".format(url, ms, nurl))
    else:
        await event.edit("Pasted to {} in {} seconds.".format(url, ms))
        
MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Upload text to del.dog."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
    ".dog <text>\
    \nUsage: Upload text to del.dog."})

MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='Del.dog', version='1.0')})