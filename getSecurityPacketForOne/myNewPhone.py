import sys

sys.path.append("..//")
import hello

# my
uuid = "00008110-001A21803482401E"
key = "1006"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
hello.doFromFile(uuid, key, "my", "hello", "false", 0, 0, "false", "false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "my", "hello", "588815", "package", "星星票")
