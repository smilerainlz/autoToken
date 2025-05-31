import sys

sys.path.append("..//")
import hello

uuid = "c933eea94b3ba611f48322b9d9ebc02e9c1efef1"
key = "0081"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
hello.doFromFile(uuid, key, "002", "hello", "false", 1, 0, "false","false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "001", "hello", "588815", "package", "星星票")