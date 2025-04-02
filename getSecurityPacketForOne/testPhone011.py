import sys

sys.path.append("..//")
import hello

uuid = "04f53f637d3dd14f7266fcb483256bc81080e235"
key = "0057"

# 登陆好的
# hello.doAll(uuid, key)

# 通过文件一个个登陆uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime
# hello.doFromFile(uuid, key, "011", "hello", "false", 1, 0, "false")

# 送礼物uuid, key, fileName, appType, sendUserId, sendType, sendName
hello.doFromFileSendGift(uuid, key, "011", "hello", "49502575", "package", "初级水晶球")