import sys

sys.path.append("..//")
import hello

uuid = "15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4"
key = "1002"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
# hello.doFromFile(uuid, key, "006", "hello", "false", 1, 1500, "false", "true")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
hello.doFromFileSendGift(uuid, key, "006", "hello", "588815", "package", "初级水晶球")