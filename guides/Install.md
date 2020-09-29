# How to install HyperBot++
## Upgrading from HyperBot
### Pre-requisites
Add `nunopenim/modules-universe` and `githubcatw/HyperBot_Plus` as community repos in your config.

> The first repo is used to install the requisite installer, and the second is the main repo.

Your community repo list should look like this:

`COMMUNITY_REPOS = ["nunopenim/module-universe", "githubcatw/HyperBot_Plus"]`
### Installing the pre-requisites
In Telegram, run `.pkg install req_installer`.

After the installation is done, run `.req cowpy asyncurban google-play-scraper youtube-dl google-api-python-client pyfiglet beautifulsoup4==4.9.1` to install the pre-requisites for HyperBot++.

### Adding extra config fields
Open `config.py` in a text editor, and add this after the end:
```
class PlusConfig(object):
    # Your best friends, required for some modules
    HOMIES = []
    # The name of your virus, required for disease
    VIRUS = "televirus"
```

### Installing HyperBot++
Thanks to HyperUBot featuring a package manager, you can now install only the modules you need.

Choose the modules you need from the table below:

|**Original modules**||
|-----|-----|
|`flasher`|Flash ZIP files.|
|`profile`|Various commands to edit profile.|
|`disease`|Spread your own virus across Telegram.|
|`notes`|Save various data and retrieve it later.|
|`locks`|Block members from posting certain types of messages.|
|`deldog`|del.dog client.|
|`scramble`|Scramble a message.|

For the extra commands, read [this](https://github.com/githubcatw/HyperBot_Plus/blob/master/guides/Installing_Old_Extra_Commands.md) guide.

In this guide, we will pick `notes` and `flasher`.

In Telegram, run `.pkg install <the packages you picked, separated with spaces>`. In our case, the command is `.pkg install notes flasher`.
