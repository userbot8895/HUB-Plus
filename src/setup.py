# setup
# HyperBot++
# Licensed under the DBBPL
# Uses code from the HyperUBot Setup Assistant, licensed under the PEL (Penim Enterprises License)
# (C) 2021 nunopenim
# (C) 2021 prototype74
# (C) 2021 githubcatw

from platform import system
from subprocess import check_call
from sys import executable
import os

IS_WINDOWS = True if system().lower().startswith("win") else False
PY_EXEC = executable if not " " in executable else '"' + executable + '"'
WIN_COLOR_ENABLED = False

try:
    if IS_WINDOWS:
        import colorama
        colorama.init()
        WIN_COLOR_ENABLED = True
except:
    pass

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED_BG = "\033[101m"
    END = "\033[0m"

def setColorText(text: str, color: Colors) -> str:
    if IS_WINDOWS and not WIN_COLOR_ENABLED:
        return text  # don't use ANSI codes
    return color + text + Colors.END

try:
	from userbot.version import VERSION as UB_VERSION
except ImportError:
	raise ImportError(setColorText("Your version of HyperUBot is too old for HyperBot++.", Colors.RED))

LOGO = """
 _   _                       ____        _
| | | |_   _ _ __   ___ _ __| __ )  ___ | |_  _     _
| |_| | | | | '_ \\ / _ \\ '__|  _ \\ / _ \\| __|| |_ _| |_
|  _  | |_| | |_) |  __/ |  | |_) | (_) | ||_   _|_   _|
|_| |_|\\__, | .__/ \\___|_|  |____/ \\___/ \\__||_|   |_|
       |___/|_|         setup
"""

REQUIREMENTS = """
cowpy
asyncurban
google-play-scraper
youtube-dl
google-api-python-client
pyfiglet
beautifulsoup4==4.9.1
pillow
qrcode
"""

VERSION = "2021.4 for HUB 4.x"
MIN_UB_VERSION = "4"
LTS_UB_VERSION = "3"

def init():
	print(LOGO)
	print(f"\nVersion {VERSION}\n========================")
	checkVersion()
	checkConfig()
	print("========================")
	print("Installing dependencies")
	f = open("reqs.txt", "w")
	f.write(REQUIREMENTS)
	_install_requirements()
	f.close()
	os.remove("reqs.txt")
	print("========================")
	setupPlusConfig()

def _install_requirements():
    try:
        check_call(
            [PY_EXEC, "-m", "pip", "install", "-r", "reqs.txt"])
    except Exception as e:
        print(setColorText(
            f"Failed to install pip requirements: {e}", Colors.RED))
    return

def setupPlusConfig():
	print("Your module selection requires a PlusConfig, which we can set up here.")
	config = "class PlusConfig(object):"
	while True:
		print(f"A YouTube API key is required for {setColorText("scrapers", Colors.YELLOW)}. If you don't know where to get one go to slickremix.com/get-api-key-for-youtube.")
		inp = input("Enter your YouTube API key, or if you didn't select scrapers press 'S' to skip: ")
		if inp.lower() == "s":
			break
		else:
			config = f'{config}{"":4}YOUTUBE_API_KEY = "{inp}"\n'
			break

	while True:
		print(f"If you have selected {setColorText("disease", Colors.YELLOW)}, you can spread a virus across Telegram. But who wants to be infected with an unnamed virus?")
		inp = input("Enter the name of your virus here, or if you didn't select it press 'S' to skip: ")
		if inp.lower() == "s":
			break
		else:
			config = f'{config}{"":4}VIRUS = "{inp}"\n'
			break

	homies = []
	print("Also, you might want to give your best friends immunity.")
	while True:
		inp = input("Enter their IDs here one by one and press 'S' at the end: ")
		if inp.lower() == "s":
			break
		else:
			homies.append(inp)
			print(f"Selected {len(homies)} people")

	if len(homies) > 0:
		config = f'{config}{"":4}HOMIES = [{",".join(homies)}]"\n'

	print("Setup will now update your config.py to include the PlusConfig.")
	try:
		dl_path = os.path.join(".", "downloads")  # default path
		config_file = os.path.join(".", "userbot", "config.py")
		with open(config_file, "w+") as cfg_file:
			print(f"Writing configuration file in {config_file}")
			cfg_file.write(config)
			cfg_file.close()
			print("Config file updated. Due to how HyperUBot works you need to reboot the userbot before your new config is loaded.")
	except Exception as e:
		print(setColorText(f"Failed to write configuration file: {e}", Colors.RED))
		raise Exception(setColorText(f"Failed to write configuration file: {e}", Colors.RED))

def checkVersion():
	signVersion = UB_VERSION[0:len(MIN_UB_VERSION)]
	signLtsVersion = UB_VERSION[0:len(LTS_UB_VERSION)]
	if signVersion == MIN_UB_VERSION:
		print("You have a supported version of HyperUBot.")
		return True
	elif signLtsVersion == LTS_UB_VERSION:
		print("Your version of HyperUBot is unsupported by HyperBot++, but is supported by HyperBot++ LTS.")
		return False
	else:
		print("\033[1;31;40mYour version of HyperUBot is unsupported by HyperBot++.\033[1;37;40m")
		return False

def checkConfig():
	if os.path.exists(os.path.join("..", "config.env")):
		print("\033[1;31;40mOnly config.py is supported. Please re-run HyperUBot setup.\033[1;37;40m")
		return False
	return True

init()