# qrcode
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT, MODULE_INFO
from userbot.include.aux_funcs import module_info
from telethon.events import NewMessage
from os.path import basename

import asyncio
import os

import qrcode
from bs4 import BeautifulSoup
from userbot.sysutils.configuration import getConfig
LOGGING = getConfig("LOGGING")

@tgclient.on(NewMessage(pattern=r"^\.decode$", outgoing=True))
async def parseqr(qr_e):  # decods qr or barcode
    if not qr_e.text[0].isalpha() and qr_e.text[0] in ("."):
        downloaded_file_name = await qr_e.client.download_media(
            await qr_e.get_reply_message())
        # parse the Official ZXing webpage to decode the QRCode
        command_to_exec = ["curl", "-X", "POST", "-F", "f=@" + downloaded_file_name + "", "https://zxing.org/w/decode"]
        process = await asyncio.create_subprocess_exec(*command_to_exec, stdout=asyncio.subprocess.PIPE,
                                                       stderr=asyncio.subprocess.PIPE, )  # who knew syscalls in python, huh?
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()
        os.remove(downloaded_file_name)
        if not t_response:
            logger.info(e_response)
            logger.info(t_response)
            await qr_e.edit("Failed to decode.")
            return
        soup = BeautifulSoup(t_response, "html.parser")
        qr_contents = soup.find_all("pre")[0].text
        await qr_e.edit("Decoded message: " + qr_contents)


@tgclient.on(NewMessage(pattern=r"\.makeqr(?: |$)([\s\S]*)", outgoing=True))
async def make_qr(makeqr):  # makes qr
    if not makeqr.text[0].isalpha() and makeqr.text[0] in ("."):
        if makeqr.fwd_from:
            return
        input_str = makeqr.pattern_match.group(1)
        message = "SYNTAX: `.makeqr <long text to include>`"
        reply_msg_id = None
        if input_str:
            message = input_str
        elif makeqr.reply_to_msg_id:
            previous_message = await makeqr.get_reply_message()
            reply_msg_id = previous_message.id
            if previous_message.media:
                downloaded_file_name = await makeqr.client.download_media(previous_message)
                m_list = None
                with open(downloaded_file_name, "rb") as file:
                    m_list = file.readlines()
                message = ""
                for media in m_list:
                    message += media.decode("UTF-8") + "\r\n"
                os.remove(downloaded_file_name)
            else:
                message = previous_message.message
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(message)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("img_file.webp", "PNG")
        await makeqr.client.send_file(makeqr.chat_id, "img_file.webp", reply_to=reply_msg_id)
        os.remove("img_file.webp")
        await makeqr.delete()


MODULE_DESC.update({
    basename(__file__)[:-3]:
    "you have a brain, right?"})

MODULE_DICT.update({
    basename(__file__)[:-3]:
        "`.decode <reply to barcode/qrcode>`\
    \nUsage: Get the content from the replied QR Code/Bar Code.\
    \n\n`.makeqr <content>`\
    \nUsage: Make a QR Code from the given content."})

MODULE_INFO.update({basename(__file__)[:-3]: module_info(name='QR code', version='1.0')})