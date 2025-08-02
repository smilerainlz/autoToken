import sys

sys.path.append("..//")
import hello

uuid = "010c2c6dd46d94ab3f129697112f74b3a2367f75"
key = "1021"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
hello.doFromFile(uuid, key, "003", "hello", "false", 0, 0, "false","false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "003", "hello", "49502575", "package", "初级水晶球")
