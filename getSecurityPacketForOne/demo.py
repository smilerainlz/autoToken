import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0060"

client = wda.USBClient(uuid, port=8100)

client(label="消息").click()
if client(label="可遇hl").exists:
    client(label="可遇hl").click()
    client(label="马上前往").click()