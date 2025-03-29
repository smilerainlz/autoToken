import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "c933eea94b3ba611f48322b9d9ebc02e9c1efef1"
key = "0052"

client = wda.USBClient(uuid, port=8100)