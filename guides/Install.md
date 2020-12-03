# How to install HyperBot++
You need to already have [HyperUBot](https://www.github.com/nunopenim/HyperUBot) installed.
### Pre-requisites
Add `"userbot8895/HyperBot_Plus"` as a community repo in your config.

Your community repo list should look like this:

`COMMUNITY_REPOS = ["userbot8895/HyperBot_Plus"]`

Or, in case you have more repos,

`COMMUNITY_REPOS = ["some_other_repo","userbot8895/HyperBot_Plus"]`

### Installing the pre-requisites
In Telegram, run `.pkg install req_installer`.

After the installation is done, run `.req cowpy asyncurban google-play-scraper youtube-dl google-api-python-client pyfiglet beautifulsoup4==4.9.1 pillow qrcode` to install the pre-requisites for HyperBot++.

Then, to make sure the bot can install the extra modules, do `.pkg update`. Then, run `.pkg list` and make sure `hyperbot++` shows up there.

### Adding extra config fields
Open the userbot's `config.py` (`config.env` is not supported) in a text editor, and add this after the end:
```python
class PlusConfig(object):
    # Your best friends. Required for some modules.
    HOMIES = []
    # The name of your virus. Required for disease.
    VIRUS = "televirus"
    # YouTube API key, get it from slickremix.com/get-api-key-for-youtube/. Required for scrapers.
    YOUTUBE_API_KEY = None
```
Fill in the relevant fields.

> Example config:
```python
class PlusConfig(object):
    # Your best friends. Required for some modules.
    HOMIES = [1337, 90210]
    # The name of your virus. Required for disease.
    VIRUS = "COVID-2020"
    # YouTube API key, get it from slickremix.com/get-api-key-for-youtube/. Required for scrapers.
    YOUTUBE_API_KEY = "SomeAPIkey"
```

### Installing HyperBot++
Thanks to HyperUBot featuring a package manager, you can now install only the modules you need.

Choose the modules you need from the table below:

|**Original modules**||
|-----|-----|
|`flasher`|Flash a ZIP file.|
|`profile`|Edit your name, bio and profile picture.|
|`disease`|Spread your own plague across Telegram!|
|`notes`|Save text and quickly send it later.|
|`locks`|Prevent people from posting certain types of media in this chat.|
|`deldog`|Create a del.dog from text.|
|`scramble`|Scramble text.|
|-----|-----|
|**Ported modules**||
|-----|-----|
|`qrcode`|Create and read QR codes.|
|`stickers`|Make your own sticker pack.|
|Extra commands|Read [this](https://github.com/githubcatw/HyperBot_Plus/blob/master/guides/Installing_Old_Extra_Commands.md) guide|

In Telegram, run `.pkg install <the packages you picked, separated with spaces>`.

> For example, if you pick `notes` and `flasher` the command is `.pkg install notes flasher`.

Then, run `.modules`. You should see the modules you picked.

### Enjoy!
