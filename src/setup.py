# setup
# HyperBot++
# Licensed under the DBBPL
# Uses code from HyperUBot and modules-universe, licensed under the PEL (Penim Enterprises License)
# (C) 2021 nunopenim
# (C) 2021 prototype74
# (C) 2021 githubcatw

from platform import system
from subprocess import check_call
from sys import executable, version_info
import os
import pyAesCrypt
from userbot import getConfig

IS_WINDOWS = (True if system().lower() == "windows" or
              os.name == "nt" or platform.startswith("win") else False)
SECURE_CONFIG = os.path.join(getConfig("USERDATA"), "secure_plus_config")
PY_EXEC = executable if not " " in executable else '"' + executable + '"'
WIN_COLOR_ENABLED = False
PIP_UTIL = False

try:
    if IS_WINDOWS:
        import colorama
        colorama.init()
        WIN_COLOR_ENABLED = True
except:
    pass

try:
	from userbot.include import pip_utils as pu
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
except:
	from userbot import VERSION as UB_VERSION

LOGO = """
 _   _ _   _ ____
| | | | | | | __ )   _     _
| |_| | | | |  _ \\ _| |_ _| |_
|  _  | |_| | |_) |_   _|_   _|
|_| |_|\\___/|____/  |_|   |_|

           Setup
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
pyAesCrypt
"""

VERSION = "2021.7"
MIN_UB_VERSION = "4.0.0"
LTS_UB_VERSION = "4.0.0"
OLD_UB_VERSION = "3.0.0"

#temp solution
def isSupportedVersion(version: str) -> bool:
    try:
        bot_ver = tuple(map(int, hubot_version.split(".")))
        req_ver = tuple(map(int, version.split(".")))
        if bot_ver >= req_ver:
            return True
    except:
        pass
    return False

def init():
	print(LOGO)
	print(f"\nVersion {VERSION}\n========================")
	checkVersion()
	checkConfig()
	print(setColorText("As HUB++ Setup is in beta it's advised to back up your userbot using the recovery.", Colors.RED))
	print(setColorText("Data might be lost, and we won't be responsible. Please report any bugs to the @userbot8895 Telegram group.", Colors.RED))
	print("Press Enter to continue.")
	input()
	print("========================")
	print("Installing dependencies...")
	if int(UB_VERSION[0:1]) > 4:
		installReqs()
	elif int(UB_VERSION[0:1]) == 4:
		if PIP_UTIL:
			installReqs()
		else:
			installReqsHUB4()
	else:
		installReqsHUB4()
	print("========================")
	setupPlusConfig()
	print("========================")
	print(f"Setup complete. {setColorText('Enjoy HUB++!', Colors.YELLOW)}\n")
	os.remove(__file__)

def installReqsHUB4():
    print("Using pip commands.")
    f = open("reqs.txt", "w")
    f.write(REQUIREMENTS)
    try:
        check_call(
            [PY_EXEC, "-m", "pip", "install", "-r", "reqs.txt"])
    except Exception as e:
        print(setColorText(
            f"Failed to install pip requirements: {e}", Colors.RED))
        return
    f.close()
    os.remove("reqs.txt")

def installReqs():
   print("Using pip_utils.")
   for dep in REQUIREMENTS.split():
      pu.installPkg(dep)

def setupPlusConfig():
	print(f"Some modules require {setColorText('a PlusConfig', Colors.YELLOW)}, which we can set up here.")
	config = "class PlusConfig(object):"
	while True:
		print(f"\nA YouTube API key is required for {setColorText('scrapers', Colors.YELLOW)}. If you don't know where to get one go to slickremix.com/get-api-key-for-youtube.")
		inp = input("Enter your YouTube API key, or if you didn't select scrapers press Enter to skip: ")
		if inp.lower() == "":
			break
		else:
			while True:
				print(f"\nOptionally you can secure the API key by storing it in {setColorText('a secure PlusConfig', Colors.YELLOW)}.")
				print(f"This secure PlusConfig is unrelated to the userbot's secure config and stored separately.")
				sinp = input("Do you want a secure PlusConfig? (y/n): ")
				if sinp.lower() in ("y", "yes"):
					encryptPlusConfig(inp)
					break
				elif sinp.lower() in ("n", "no"):
					config = f'{config}{"":4}YOUTUBE_API_KEY = "{inp}"\n'
					break
			break

	while True:
		print(f"\nIf you have selected {setColorText('disease', Colors.YELLOW)}, you can spread a virus across Telegram. But who wants to be infected with an unnamed virus?")
		inp = input("Enter the name of your virus here, or if you didn't select it press Enter to skip: ")
		if inp.lower() == "":
			break
		else:
			config = f'{config}{"":4}VIRUS = "{inp}"\n'
			break

	homies = []
	print("\nAlso, you might want to give your best friends immunity. Enter their IDs (check @userinfobot) here one by one and press 'S' at the end.")
	while True:
		inp = input("ID (press Enter to finish): ")
		if inp.lower() == "":
			break
		else:
			homies.append(inp)
			print(f"Selected {len(homies)} people")

	if len(homies) > 0:
		config = f'{config}{"":4}HOMIES = [{",".join(homies)}]"\n'

	print("\nSetup will now update your config.py to include the PlusConfig.")
	try:
		dl_path = os.path.join(".", "downloads")  # default path
		config_file = os.path.join(".", "userbot", "config.py")
		with open(config_file, "a") as cfg_file:
			print(f"Writing configuration file in {config_file}")
			cfg_file.write(config)
			cfg_file.close()
			print("Config file updated. Due to how HyperUBot works you need to reboot the userbot before your new config is loaded.")
	except Exception as e:
		print(setColorText(f"Failed to write configuration file: {e}", Colors.RED))
		raise Exception(setColorText(f"Failed to write configuration file: {e}", Colors.RED))

# based on https://github.com/nunopenim/HyperUBot/blob/master/update_secure_cfg.py#L94

def encryptPlusConfig(key):
    print("You can use a password for your secure config to increase the security of your sensitive data. This is optional, but extra protection doesn't hurt.")
    print(setColorText("If you forgot your password, you have to re-run Setup and create a new secure config!", Colors.RED))
    print()

    set_pwd = False

    while True:
        inp = input("Set password? (y/n): ")
        if inp.lower() in ("y", "yes"):
            set_pwd = True
            break
        elif inp.lower() in ("n", "no"):
            break
        else:
            print(setColorText("Invalid input. Try again...", Colors.YELLOW))

    password = ""
    if set_pwd:
        print()
        from getpass import getpass
        print("Your password must have at least a length of 4 characters. Maximum length is 1024 characters")
        while True:
            password = getpass("Your password: ")
            if len(password) >= 4 and len(password) <= 1024:
                break
            elif len(password) < 4:
                print(setColorText("Password too short.", Colors.YELLOW))
            elif len(password) > 1024:
                print(setColorText("Password too long.", Colors.YELLOW))
            else:
                print(setColorText("Invalid input. Try again.", Colors.YELLOW))
        while True:
            retype_pwd = getpass("Retype your password: ")
            if password == retype_pwd:
                break
            else:
                print(setColorText("Invalid input. Try again.", Colors.YELLOW))

    print()
    try:
        print("Securing config...")
        if os.path.exists(SECURE_CONFIG):
            os.remove(SECURE_CONFIG)
        if os.path.exists("_temp.py"):
            os.remove("_temp.py")
        secure_configs = (f'YT_API_KEY = "{key}"')
        with open("_temp.py", "w") as cfg_file:
            cfg_file.write(secure_configs)
        cfg_file.close()
        pyAesCrypt.encryptFile(infile="_temp.py",
                               outfile=SECURE_CONFIG,
                               passw=password,
                               bufferSize=(64 * 1024))
        os.remove("_temp.py")
        if os.path.exists(SECURE_CONFIG):
            print(setColorText("Config secured! Continue setting up.", Colors.GREEN))
        else:
            print(setColorText("Failed to secure configs", Colors.RED))
    except Exception as e:
        print(setColorText(f"Failed to secure configs: {e}", Colors.RED))
    return

def checkVersion():
	if isSupportedVersion(MIN_UB_VERSION):
		print("You have a supported version of HyperUBot.")
		return True
	elif isSupportedVersion(LTS_UB_VERSION):
		print("Your version of HyperUBot is unsupported by HUB++, but is supported by HUB++ LTS.")
		print(f"Check it out here: {setColorText('github.com/userbot8895/HBPlus-LTS', Colors.YELLOW)}")
		return False
	elif isSupportedVersion(OLD_UB_VERSION):
		print(f"Your version of HyperUBot is unsupported by HUB++, but is supported by {setColorText('the previous version', Colors.YELLOW)} of HUB++ LTS.")
		print(f"Check it out here: {setColorText('github.com/userbot8895/HBPlus-LTS/tree/old', Colors.YELLOW)}")
		return False
	else:
		print(setColorText('Your version of HyperUBot is unsupported by HUB++.', Colors.RED))
		return False

def checkConfig():
	if os.path.exists(os.path.join("..", "config.env")):
		print(setColorText('Only config.py is supported. Please re-run HyperUBot setup.', Colors.RED))
		return False
	elif not os.path.exists(os.path.join("..", "config.py")):
		open(os.path.join("..", "config.py"),"w+")
		print(f"Looks like you don't have a config.py. Setup {setColorText('created one', Colors.YELLOW)} for you.")
	return True

init()