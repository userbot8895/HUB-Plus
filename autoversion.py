# autoversion
# HUB++
# Licensed under the DBBPL
# (c) 2021 githubcatw

# =====================
LATEST_STABLE = "2022.2.1"
LATEST_BETA = "2022.1.b2"
# =====================
VER_REGEX = '20\d+\.\d+(\.b?a?\d+)?( for HUB [0-9]+\.x)?( beta [0-9]+)?(?=\")'
SOURCE = "src/"
LATEST_VER = ""
# =====================
import re
import os

while True:
   bos = input(f"[B]eta ({LATEST_BETA}) or [S]table ({LATEST_STABLE})? (Default: stable) ").lower()

   if bos == "b":
      LATEST_VER = LATEST_BETA
      break
   elif bos == "s" or bos =="":
      LATEST_VER = LATEST_STABLE
      break
   else:
      print("Unknown option")

for directory, subdirectories, files in os.walk(SOURCE):
  for file in files:
    ct = ""
    print(file)
    with open(SOURCE + file, "r", encoding="utf-8") as f:
      ct = f.read()
    ct = re.sub(VER_REGEX,LATEST_VER,ct)
    with open(SOURCE + file, "w", encoding="utf-8") as f:
      f.write(ct)
