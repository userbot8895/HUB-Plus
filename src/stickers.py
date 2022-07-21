# stickers
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot.sysutils.registration import register_cmd_usage, register_module_desc, register_module_info
from userbot.sysutils.event_handler import EventHandler
from os.path import basename

import io
import math
import random
import PIL
import urllib.request
from os import remove
import os

from PIL import Image
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from telethon.tl.types import DocumentAttributeSticker
from telethon.tl.types import InputStickerSetID
from userbot.sysutils.configuration import getConfig
LOGGING = getConfig("LOGGING")

ehandler = EventHandler()
VERSION = "2022.2.1" 

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "hehe me stel ur stikér\nhehe.",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pacc looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal Your Sticker is stealing this sticker... ",
]

@ehandler.on(command="kang", hasArgs=True, outgoing=True)
async def kang(args):
    if not args.text[0].isalpha() and args.text[0] in ("."):
        user = await args.client.get_me()
        if not user.username:
            user.username = user.first_name
        message = await args.get_reply_message()
        photo = None
        emojibypass = False
        is_anim = False
        emoji = None

        if message and message.media:
            if isinstance(message.media, MessageMediaPhoto):
                await args.edit(f"`{random.choice(KANGING_STR)}`")
                photo = io.BytesIO()
                photo = await args.client.download_media(message.photo, photo)
            elif "image" in message.media.document.mime_type.split('/'):
                await args.edit(f"`{random.choice(KANGING_STR)}`")
                photo = io.BytesIO()
                await args.client.download_file(message.media.document, photo)
                if (DocumentAttributeFilename(file_name='sticker.webp') in
                        message.media.document.attributes):
                    emoji = message.media.document.attributes[1].alt
                    emojibypass = True
            elif "tgsticker" in message.media.document.mime_type:
                await args.edit(f"`{random.choice(KANGING_STR)}`")
                await args.client.download_file(message.media.document,
                                        'AnimatedSticker.tgs')

                attributes = message.media.document.attributes
                for attribute in attributes:
                    if isinstance(attribute, DocumentAttributeSticker):
                        emoji = attribute.alt

                emojibypass = True
                is_anim = True
                photo = 1
            else:
                await args.edit("`Unsupported File!`")
                return
        else:
            await args.edit("`I can't kang that...`")
            return

        if photo:
            splat = args.text.split()
            if not emojibypass:
                emoji = "🤔"
            pack = 1
            if len(splat) == 3:
                pack = splat[2]  # User sent both
                emoji = splat[1]
            elif len(splat) == 2:
                if splat[1].isnumeric():
                    # User wants to push into different pack, but is okay with
                    # thonk as emote.
                    pack = int(splat[1])
                else:
                    # User sent just custom emote, wants to push to default
                    # pack
                    emoji = splat[1]

            isCustom = os.path.exists("pack")
            if isCustom:
                try:
                    pac = open("apack", "r").read() if is_anim else open("pack","r").read()
                    psp = pac.split("\n")
                    pack = 0
                    packname = psp[1]
                    packnick = psp[0]
                except FileNotFoundError:
                    packname = f"a{user.id}_by_{user.username}_{pack}"
                    packnick = f"@{user.username}'s kang pack Vol.{pack}"

            else:
                packname = f"a{user.id}_by_{user.username}_{pack}"
                packnick = f"@{user.username}'s kang pack Vol.{pack}"
            cmd = '/newpack'
            file = io.BytesIO()

            if not is_anim:
                image = await resize_photo(photo)
                file.name = "sticker.png"
                image.save(file, "PNG")
            else:
                if not isCustom:
                    packname += "_anim"
                    packnick += " (Animated)"
                cmd = '/newanimated'

            response = urllib.request.urlopen(
                urllib.request.Request(f'http://t.me/addstickers/{packname}'))
            htmlstr = response.read().decode("utf8").split('\n')

            if "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>." not in htmlstr:
                async with args.client.conversation('Stickers') as conv:
                    await conv.send_message('/addsticker')
                    await conv.get_response()
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.send_message(packname)
                    x = await conv.get_response()
                    while "120" in x.text:
                        pack += 1
                        packname = f"a{user.id}_by_{user.username}_{pack}"
                        packnick = f"@{user.username}'s kang pack Vol.{pack}"
                        cusMsg = "S"
                        if isCustom:
                            cusMsg = "Custom pack is full, s"
                        await args.edit(f"`{cusMsg}witching to pack {str(pack)} due to insufficient space`")
                        await conv.send_message(packname)
                        x = await conv.get_response()
                        if x.text == "Invalid pack selected.":
                            await conv.send_message(cmd)
                            await conv.get_response()
                            # Ensure user doesn't get spamming notifications
                            await args.client.send_read_acknowledge(conv.chat_id)
                            await conv.send_message(packnick)
                            await conv.get_response()
                            # Ensure user doesn't get spamming notifications
                            await args.client.send_read_acknowledge(conv.chat_id)
                            if is_anim:
                                await conv.send_file('AnimatedSticker.tgs')
                                remove('AnimatedSticker.tgs')
                            else:
                                file.seek(0)
                                await conv.send_file(file, force_document=True)
                            await conv.get_response()
                            await conv.send_message(emoji)
                            # Ensure user doesn't get spamming notifications
                            await args.client.send_read_acknowledge(conv.chat_id)
                            await conv.get_response()
                            await conv.send_message("/publish")
                            if is_anim:
                                await conv.get_response()
                                await conv.send_message(f"<{packnick}>")
                            # Ensure user doesn't get spamming notifications
                            await conv.get_response()
                            await args.client.send_read_acknowledge(conv.chat_id)
                            await conv.send_message("/skip")
                            # Ensure user doesn't get spamming notifications
                            await args.client.send_read_acknowledge(conv.chat_id)
                            await conv.get_response()
                            await conv.send_message(packname)
                            # Ensure user doesn't get spamming notifications
                            await args.client.send_read_acknowledge(conv.chat_id)
                            await conv.get_response()
                            # Ensure user doesn't get spamming notifications
                            await args.client.send_read_acknowledge(conv.chat_id)
                            await args.edit(
                                f"`Sticker added in a Different Pack !\
                                \nThis Pack is Newly created!\
                                \nYour pack can be found [here](t.me/addstickers/{packname})",
                                parse_mode='md')
                            return
                    if is_anim:
                        await conv.send_file('AnimatedSticker.tgs')
                        remove('AnimatedSticker.tgs')
                    else:
                        file.seek(0)
                        await conv.send_file(file, force_document=True)
                    rsp = await conv.get_response()
                    if "Sorry, the file type is invalid." in rsp.text:
                        await args.edit(
                            "`Failed to add sticker, use` @Stickers `bot to add the sticker manually.`"
                        )
                        return
                    await conv.send_message(emoji)
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await conv.send_message('/done')
                    await conv.get_response()
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
            else:
                await args.edit("`Brewing a new Pack...`")
                async with args.client.conversation('Stickers') as conv:
                    await conv.send_message(cmd)
                    await conv.get_response()
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.send_message(packnick)
                    await conv.get_response()
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    if is_anim:
                        await conv.send_file('AnimatedSticker.tgs')
                        remove('AnimatedSticker.tgs')
                    else:
                        file.seek(0)
                        await conv.send_file(file, force_document=True)
                    rsp = await conv.get_response()
                    if "Sorry, the file type is invalid." in rsp.text:
                        await args.edit(
                            "`Failed to add sticker, use` @Stickers `bot to add the sticker manually.`"
                        )
                        return
                    await conv.send_message(emoji)
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await conv.send_message("/publish")
                    if is_anim:
                        await conv.get_response()
                        await conv.send_message(f"<{packnick}>")
                    # Ensure user doesn't get spamming notifications
                    await conv.get_response()
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.send_message("/skip")
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    await conv.send_message(packname)
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)
                    await conv.get_response()
                    # Ensure user doesn't get spamming notifications
                    await args.client.send_read_acknowledge(conv.chat_id)

            cuMsg = "\n__Note: if kang failed you can try .resetkang to remove your custom kang pack settings (this doesn't remove the packs themselves).__"
            await args.edit(
                f"`Sticker kanged successfully!`\
                \nPack can be found [here](t.me/addstickers/{packname}){cuMsg if isCustom else ''}",
                parse_mode='md')


async def resize_photo(photo):
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image
    
    
@ehandler.on(command="getsticker", hasArgs=False, outgoing=True)
async def get_sticker(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
    	if not event.reply_to_msg_id:
    		await event.edit("`Reply to a sticker first.`")
    		return
    	reply = await event.get_reply_message()
    	rsticker = reply.sticker
    	if not rsticker:
    		await event.edit("`This isn't a sticker, smh.`")
    		return
    	if rsticker.mime_type == "application/x-tgsticker":
    		await event.edit("`No point in uploading animated stickers.`")
    		return
    	else:
    		sticker_bytes = io.BytesIO()
    		await reply.download_media(sticker_bytes)
    		sticker = io.BytesIO()
    		try:
    			pilimg = PIL.Image.open(sticker_bytes)
    		except OSError as e:
    			await event.edit(f"`OSError: {e}`")
    			return
    		pilimg.save(sticker, format="PNG")
    		pilimg.close()
    		sticker.name = "sticker.png"
    		sticker.seek(0)
    		if event:
    			await reply.respond(file=sticker, force_document=True)
    		else:
    			await reply.reply(file=sticker)
    		sticker_bytes.close()
    		sticker.close()
    	await event.delete()
    
@ehandler.on(command="stkrinfo", hasArgs=False, outgoing=True)
async def get_pack_info(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if not event.is_reply:
            await event.edit("`I can't fetch info from nothing, can I ?!`")
            return

        rep_msg = await event.get_reply_message()
        if not rep_msg.document:
            await event.edit("`Reply to a sticker to get the pack details`")
            return

        try:
            stickerset_attr = rep_msg.document.attributes[1]
            await event.edit(
                "`Fetching details of the sticker pack, please wait..`")
        except BaseException:
            await event.edit("`This is not a sticker. Reply to a sticker.`")
            return

        if not isinstance(stickerset_attr, DocumentAttributeSticker):
            await event.edit("`This is not a sticker. Reply to a sticker.`")
            return

        get_stickerset = await event.client(
            GetStickerSetRequest(
                InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash)))
        pack_emojis = []
        for document_sticker in get_stickerset.packs:
            if document_sticker.emoticon not in pack_emojis:
                pack_emojis.append(document_sticker.emoticon)

        OUTPUT = f"**Sticker Title:** `{get_stickerset.set.title}\n`" \
                 f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n" \
                 f"**Official:** `{get_stickerset.set.official}`\n" \
                 f"**Archived:** `{get_stickerset.set.archived}`\n" \
                 f"**Stickers In Pack:** `{len(get_stickerset.packs)}`\n" \
                 f"**Emojis In Pack:**\n{' '.join(pack_emojis)}"

        await event.edit(OUTPUT)

@ehandler.on(command="setkang", hasArgs=False, outgoing=True)
async def get_pack_info(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        if not event.is_reply:
            await event.edit("`I can't kang to nothing, can I ?!`")
            return

        rep_msg = await event.get_reply_message()
        if not rep_msg.document:
            await event.edit("`Reply to a sticker to set a custom pack.`")
            return

        try:
            stickerset_attr = rep_msg.document.attributes[1]
            await event.edit(
                "`Setting custom pack, please wait...`")
        except BaseException:
            await event.edit("`This is not a sticker. Reply to a sticker.`")
            return

        if not isinstance(stickerset_attr, DocumentAttributeSticker):
            await event.edit("`This is not a sticker. Reply to a sticker.`")
            return
        
        get_stickerset = await event.client(
            GetStickerSetRequest(
                InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash)))

        if get_stickerset.set.archived:
            await event.edit("`This pack is archived!`")
            return

        if len(get_stickerset.packs) == 120:
            await event.edit("`This pack is full!`")
            return

        # don't let people attempt to kang to others' packs
        async with event.client.conversation('Stickers') as conv:
            await conv.send_message('/addsticker')
            await conv.get_response()
            # Ensure user doesn't get spamming notifications
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message(get_stickerset.set.short_name)
            x = await conv.get_response()
            # Ensure user doesn't get spamming notifications
            await event.client.send_read_acknowledge(conv.chat_id)
            await conv.send_message("/cancel")
            # Ensure user doesn't get spamming notifications
            await event.client.send_read_acknowledge(conv.chat_id)
            if "Invalid" in x.text:
                await event.edit("`Cannot kang to others' packs!`")
                return

        if (rep_msg.sticker.mime_type == "application/x-tgsticker"):
            open("apack", "w", encoding="utf8").write(f"{get_stickerset.set.title}\n{get_stickerset.set.short_name}")
        else:
            open("pack", "w", encoding="utf8").write(f"{get_stickerset.set.title}\n{get_stickerset.set.short_name}")

        ur = f"[{get_stickerset.set.title}](t.me/addstickers/{get_stickerset.set.short_name})"
        await event.edit(f"Successfully changed kang pack to {ur}. New kanged stickers will be added there.")

@ehandler.on(command="resetkang", hasArgs=False, outgoing=True)
async def get_pack_info(event):
    if not event.text[0].isalpha() and event.text[0] in ("."):
        await event.edit("Deleting custom pack settings...")

        txt = " The saved kang packs were:"
        if(os.path.isfile("apack")):
            pf = open("apack", "r", encoding="utf8")
            ps = pf.read().split("\n")
            pf.close()
            if len(ps) == 2:
                print(f"Contents of apack: [{ps[0]}](t.me/addstickers/{ps[1]})")
                txt += f"\n[{ps[0]}](t.me/addstickers/{ps[1]})"
            print("Deleting apack...")
            os.remove("apack")

        if(os.path.isfile("pack")):
            pf = open("pack", "r", encoding="utf8")
            ps = pf.read().split("\n")
            pf.close()
            if len(ps) == 2:
                print(f"Contents of pack: [{ps[0]}](t.me/addstickers/{ps[1]})")
                txt += f"\n[{ps[0]}](t.me/addstickers/{ps[1]})"
            print("Deleting pack...")
            os.remove("pack")

        await event.edit(f"Deleted custom kang pack settings.{txt if len(txt) > 27 else ''}")

register_module_desc("Make a sticker pack.")
register_cmd_usage("kang", "(emojis) (number)", "Reply .kang to a sticker or an image to kang it to your userbot pack.\nIf emojis isn't specified uses 🤔 as emoji. (number) sets the number of the pack, but overrides .setkang.")
register_cmd_usage("stkrinfo", "", "Gets info about the replied sticker's pack.")
register_cmd_usage("setkang", "", "Reply to a sticker to set its pack as the kang pack.")
register_cmd_usage("resetkang", "", "Deletes custom kang pack settings. __Note: this doesn't delete the actual packs__")
register_module_info(
    name="Stickers",
    authors="githubcatw, Haklerman, nunopenim, help from prototype74",
    version=VERSION
)
_f_='welcsent'
from os.path import isfile as _i_
if not _i_(_f_):
 print(f"HUB++ version {VERSION} was installed successfully.\n\nCheck .listcmds or .help to see what things your userbot can now do. Or, check `.pkg list` to see what modules are also available.\nTo stay up to date with HUB++ news subscribe to our channel (https://t.me/pawneeupdates).\nIf you want to report issues with or suggest new features for HUB++ file an issue on GitHub or write in our group (https://t.me/userbot8895).\n\nHave fun!")
 with open(_f_,'w')as _w_:_w_.write('')
