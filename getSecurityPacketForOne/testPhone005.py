import sys

sys.path.append("..//")
import hello

uuid = "77df71489bd1227029fad1ce678d80490f52196e"
key = "0063"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
hello.doFromFile(uuid, key, "005", "hello", "false", 1, 1000, "false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "005", "hello", "49502575", "package", "初级水晶球")
