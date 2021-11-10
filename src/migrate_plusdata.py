# data folder migrater
# HyperBot++
# Licensed under the DBBPL
# (C) 2021 githubcatw

from userbot import getConfig
from os import remove
from os.path import isdir
from os.path import join as pathjoin
from os.path import exists as isfile
from userbot.sysutils.sys_funcs import isWindows
import shutil

userData = getConfig("USERDATA")
tempDl = getConfig("TEMP_DL_DIR")

if isWindows():
    USER_MODULES_DIR = ".\\userbot\\modules_user\\"
else:
    USER_MODULES_DIR = "./userbot/modules_user/"

def migrate():
  if not userData:
    print("migrate: Please add a USERDATA variable to your config and reboot HyperUBot.")
    print()
    print("Press any key to continue booting HyperUBot.")
    input()
    return
  if not isfile(pathjoin(".","userbot","config.py")):
    print("migrate: Please create a config.py and reboot HyperUBot.")
    print()
    print("Press any key to continue booting HyperUBot.")
    input()
    return

  plus_userdata = pathjoin(userData,"plus")
  plus_userbot = pathjoin(".","userbot","plus")
  plus_dot = pathjoin(".","plus")

  plus_deldog = pathjoin(".","deldog_temp")
  plus_notes = pathjoin(".","notes")
  plus_bullied = pathjoin(".","bullied_users.txt")
  plus_patients = pathjoin(".","patients.txt")

  if not isdir(plus_userdata):
    print('migrate: creating "plus" folder in user data')
    os.makedirs(plus_userdata)

  if isdir(plus_userbot):
    print("migrate: moving from /userbot/plus")
    shutil.move(plus_userbot, userData)

  if isdir(plus_dot):
    print("migrate: moving from /plus")
    shutil.move(plus_dot, userData)

  if isdir(plus_deldog):
    print("migrate: moving /deldog_temp to temp DL dir")
    shutil.move(plus_deldog, tempDl)

  if isdir(plus_notes):
    print("migrate: moving /notes to plus")
    shutil.move(plus_notes, plus_userdata)

  if isfile(plus_bullied):
    print("migrate: moving bullied_users.txt to plus")
    shutil.move(plus_bullied, plus_userdata)

  if isfile(plus_patients):
    print("migrate: moving patients.txt to plus")
    shutil.move(plus_patients, plus_userdata)

  print("migrate: finished migration")

print("migrate_plusdata: HUB++ data folder migrater")
print("(c) 2021 githubcatw, Haklerman")
print("Licensed under the DBBPL")
migrate()
print("Removing module...")
remove(__file__)
