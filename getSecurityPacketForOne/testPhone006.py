import sys

sys.path.append("..//")
import hello

uuid = "15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4"
key = "0069"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
hello.doFromFile(uuid, key, "006", "hello", "false", 1, 1200, "false", "false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "005", "hello", "49502575", "package", "初级水晶球")