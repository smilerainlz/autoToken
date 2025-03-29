import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0056"

client = wda.USBClient(uuid, port=8100)

if client(label="购买Hello语音钻石到账号ID92274246点  6点0 0元", timeout=10).exists:
    print("ddddd")
