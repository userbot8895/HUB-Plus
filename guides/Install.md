# How to install HUB++
You need to already have [HyperUBot](https://www.github.com/prototype74/HyperUBot) installed.

## Installation using HUB++ Setup (beta)
HUB++ 2021.4 introduces HUB++ Setup (beta), which is an installer for HUB++. If you have found this guide from HUB++ LTS's old branch (which has version 2021.3) go to Manual installation.

**HUB++ Setup is considered beta software. A backup of the userbot from the HyperUBot Recovery is advised.**

**HUB++ Setup requires input, so if you're running the userbot as a service (e.g. systemd) proceed to manual installation.**

### Install using -repo (HyperUBot 6.0 or later)

In Telegram, run `.pkg update userbot8895/HUB-Plus`, then `.pkg install setup`. The userbot will reboot as usual, and you'll be greeted by HUB++ Setup in the terminal.

### Install through config

Add `"userbot8895/HUB-Plus"` as a community repo in your config.

Your community repo list should look like this:

`COMMUNITY_REPOS = ["userbot8895/HUB-Plus"]`

Or, in case you have more repos,

`COMMUNITY_REPOS = ["some_other_repo","userbot8895/HUB-Plus"]`

Start the userbot. In Telegram, run `.pkg install setup`. The userbot will reboot as usual, and you'll be greeted by HUB++ Setup in the terminal.

After you're done installing, go to "Installing HUB++ modules".

## Manual installation
### Installing the pre-requisites
In Telegram, run `.pkg install req_installer`.

After the installation is done, run `.req cowpy asyncurban google-play-scraper youtube-dl google-api-python-client pyfiglet beautifulsoup4==4.9.1 pillow qrcode search_engine_parser` to install the pre-requisites for HUB++.

Then, to make sure the bot can install the extra modules, do `.pkg update`. Then, run `.pkg list` and make sure a line starting with `Files in hb++_` shows up there.

### Adding extra config fields
Open the userbot's `config.py` (`config.env` and `config.ini` are not supported) in a text editor, and add this after the end:
```python
class PlusConfig(object):
    # IDs of your best friends. Required for some modules.
    HOMIES = []
    # The name of your virus. Required for disease.
    VIRUS = "televirus"
    # YouTube API key, get it from slickremix.com/get-api-key-for-youtube/. Required for scrapers.
    YOUTUBE_API_KEY = None
```
Fill in or change the relevant fields.

> Example config:
```python
class PlusConfig(object):
    # IDs of your best friends. Required for some modules.
    HOMIES = [1337, 90210]
    # The name of your virus. Required for disease.
    VIRUS = "COVID-21"
    # YouTube API key, get it from slickremix.com/get-api-key-for-youtube/. Required for scrapers.
    YOUTUBE_API_KEY = "SomeAPIkey"
```

## Installing HUB++ modules
Thanks to HyperUBot featuring a package manager, you can now install only the modules you need.

Choose the modules you want from the table below:

|Module|Description|
|------|-----------|
|`flasher`|"Flash" a ZIP file.|
|`profile`|Edit your name, bio and profile picture.|
|`disease`|Spread your own plague across Telegram!|
|`notes`|Save text and quickly send it later.|
|`locks`|Prevent people from posting certain types of media in a chat.|
|`deldog`|Upload text to del.dog.|
|`scramble`|Scramble text.|
|`report`|Report people.|
|`qrcode`|Create and read QR codes.|
|`stickers`|Make your own sticker pack.|
|`correction`|Correct people.|
|Extensions|See [here](https://github.com/userbot8895/HUB-Plus/blob/master/guides/Installing_Old_Extra_Commands.md#extensions).|
|`locks`|Lock certain types of messages.|
|Memes|See [here](https://github.com/userbot8895/HUB-Plus/blob/master/guides/Installing_Old_Extra_Commands.md#memes).|
|`migrate_plusdata`|Copies over data folders from older versions of HUB++. Remove after installation.|

In Telegram, run `.pkg install <the packages you picked, separated with spaces>`.

> For example, if you pick `notes` and `flasher` the command is `.pkg install notes flasher`.

Then, run `.modules`. You should see the modules you picked.

### Enjoy!
