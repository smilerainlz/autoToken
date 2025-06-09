import sys

sys.path.append("..//")
import hello

uuid = "dfb8efa033b55e38bcda1c0b6ac9627451c7de42"
key = "0085"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime, isInToRoom
hello.doFromFile(uuid, key, "008", "hello", "false", 1, 1500, "false","false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "001", "hello", "49502575", "package", "初级水晶球")