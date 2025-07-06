import sys

sys.path.append("..//")
import hello

uuid = "984e38e08278e882dda3017fc916d873d457b13d"
key = "0100"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime, isInToRoom
# hello.doFromFile(uuid, key, "007", "hello", "false", 1, 1200, "false","true")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
hello.doFromFileSendGift(uuid, key, "007", "hello", "588815", "package", "初级水晶球")