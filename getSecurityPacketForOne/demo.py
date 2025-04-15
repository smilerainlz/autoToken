import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0061"

client = wda.USBClient(uuid, port=8100)

client.session().app_activate("com.aijiasuinc.AiJiaSuClient")