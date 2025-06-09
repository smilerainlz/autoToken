import sys

sys.path.append("..//")
import hello

uuid = "08771801cd4ba47bd323204310a296c6e05e2b1a"
key = "0083"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime, isInToRoom
hello.doFromFile(uuid, key, "001", "hello", "false", 1, 0, "false","false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
# hello.doFromFileSendGift(uuid, key, "001", "hello", "49502575", "package", "初级水晶球")