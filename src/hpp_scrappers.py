# scrapers (extension)
# HyperBot++
# Licensed under the DBBPL
# (C) 2020 githubcatw

from userbot import tgclient, MODULE_DESC, MODULE_DICT, LOGGING
from telethon.events import NewMessage
from os.path import basename

from requests import get
from re import findall
from google_play_scraper import app
from google_play_scraper import exceptions as gpse
import asyncurban
from html import unescape
from googleapiclient.discovery import build
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from search_engine_parser import GoogleSearch


@tgclient.on(NewMessage(outgoing=True, pattern="^\.ud (.*)"))
async def urban_dict(ud_e):
    """ For .ud command, fetch content from Urban Dictionary. """
    await ud_e.edit("`Processing...`")
    query = ud_e.pattern_match.group(1)
    urban_dict_helper = asyncurban.UrbanDictionary()
    try:
        urban_def = await urban_dict_helper.get_word(query)
    except asyncurban.WordNotFoundError:
        await ud_e.edit(f"Sorry, couldn't find any results for: {query}")
        return
    deflen = sum(len(i) for i in urban_def.definition)
    exalen = sum(len(i) for i in urban_def.example)
    meanlen = deflen + exalen
    if int(meanlen) >= 0:
        if int(meanlen) >= 4096:
            await ud_e.edit("`Output too large, sending as file.`")
            file = open("output.txt", "w+")
            file.write("Text: " + query + "\n\nMeaning: " +
                       urban_def.definition + "\n\n" + "Example: \n" +
                       urban_def.example)
            file.close()
            await ud_e.client.send_file(
                ud_e.chat_id,
                "output.txt",
                caption="`Output was too large, sent it as a file.`")
            if os.path.exists("output.txt"):
                os.remove("output.txt")
            await ud_e.delete()
            return
        await ud_e.edit("Text: **" + query + "**\n\nMeaning: **" +
                        urban_def.definition + "**\n\n" + "Example: \n__" +
                        urban_def.example + "__")
        if LOGGING:
            await event_log(event, "SCRAPERS (HYPERBOT++)", custom_text="UrbanDictionary query for `" + query +
                "` executed successfully.")
    else:
        await ud_e.edit("No result found for **" + query + "**")

@tgclient.on(NewMessage(outgoing=True, pattern="^\.play (.*)"))
async def playstore(ps_e):
    """ For .play command, fetch content from Play Store. """
    await ps_e.edit("`Finding...`")
    query = ps_e.pattern_match.group(1)
    try:
        res = app(query)
    except gpse.NotFoundError:
        await ps_e.edit("Invalid package ID")
        return
    if res.title is None:
        await ps_e.edit("Data error!")
        return
    await ps_e.edit("**"+res["title"]+"**\n\nBy "+res["developer"]+"\n\nSummary: "+res['summary']+"\n\n[link]("+res["url"]+")")
    
@tgclient.on(NewMessage(outgoing=True, pattern="^\.yt (.*)"))
async def yt_search(yts):
    """ For .yt command, do a YouTube search from Telegram. """
    query = yts.pattern_match.group(1)
    result = ''

    if not YOUTUBE_API_KEY:
        await yts.edit(
            "`Error: YouTube API key missing! Add it to environment vars or config.env.`"
        )
        return

    await yts.edit("`Processing...`")

    full_response = await youtube_search(query)
    videos_json = full_response[1]

    for video in videos_json:
        title = f"{unescape(video['snippet']['title'])}"
        link = f"https://youtu.be/{video['id']['videoId']}"
        videoID = f"{video['id']['videoId']}"
        result += f"{title}\n{link}\n`{videoID}`\n\n"

    reply_text = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n{result}"

    await yts.edit(reply_text)

async def youtube_search(query,
                         order="relevance",
                         token=None,
                         location=None,
                         location_radius=None):
    """ Do a YouTube search. """
    youtube = build('youtube',
                    'v3',
                    developerKey=YOUTUBE_API_KEY,
                    cache_discovery=False)
    search_response = youtube.search().list(
        q=query,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=10,
        location=location,
        locationRadius=location_radius).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return (nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return (nexttok, videos)
        
@tgclient.on(NewMessage(outgoing=True, pattern="^\.ytv (.*)"))
async def yt_video(ytv):
    """ For .play command, fetch content from Play Store. """
    await ytv.edit("`Finding...`")
    query = ytv.pattern_match.group(1)
    ydl = YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(
            'http://www.youtube.com/watch?v='+query,
            download=False # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    video_url = video['title']
    video_up = video['uploader']
    video_l = video['like_count']
    video_dl = video['dislike_count']
    video_v = video['view_count']
    video_desc = video['description']
    if video_l == None:
        video_l = "∞"
    if video_dl == None:
        video_dl = "∞"
    if video_v == None:
        video_v = "∞"
    if video_desc == None:
        video_desc = "none"
    ans_data = f"**{video_url}**\n\nBy {video_up}\n\n__{video_v} views, {video_l} likes and {video_dl} dislikes__\n\nDescription:\n{video_desc}"
    if len(ans_data) > 1024:
        ans_data = ans_data[0:1024] + "..."
    await ytv.edit(ans_data)
    
    
@tgclient.on(NewMessage(outgoing=True, pattern=r"^\.google (.*)"))
async def gsearch(q_event):
    await q_event.edit("`Processing...`")
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await q_event.edit("**Search Query:**\n`" + match + "`\n\n**Results:**\n" +
                       msg,
                       link_preview=False)

MODULE_DESC.update({
    basename(__file__)[:-3]:
    "Extra commands for the scrappers (sic) module."})

MODULE_DICT.update({
    basename(__file__)[:-3]:
        ".ud <text>\
    \nUsage: Does a search on Urban Dictionary.\
    \n\n.yt <text>\
    \nUsage: Does a search on YouTube.\
    \n\n.ytv <videoID>\
    \nUsage: Shows YouTube video informations.\
    \n\n.google <text>\
    \nUsage: Does a search on Google.\
    \n\n.play <packageID>\
    \nUsage: Does a search on Play Store."})