import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "08771801cd4ba47bd323204310a296c6e05e2b1a"
key = "0057"

client = wda.USBClient(uuid, port=8100)

if client(label="ID: 588815").exists:
    print("ddddd")
