# autoversion
# HUB++
# Licensed under the DBBPL
# (c) 2021 githubcatw

# =====================
LATEST_VER = "2021.7"
# =====================
VER_REGEX = '20\d+\.\d( for HUB [0-9]+\.x)?(?=\")'
SOURCE = "src/"
# =====================
import re
import os


for directory, subdirectories, files in os.walk(SOURCE):
  for file in files:
    ct = ""
    print(file)
    with open(SOURCE + file, "r", encoding="utf-8") as f:
      ct = f.read()
    ct = re.sub(VER_REGEX,LATEST_VER,ct)
    with open(SOURCE + file, "w", encoding="utf-8") as f:
      f.write(ct)