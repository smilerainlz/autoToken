import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0052"

myclient = wda.USBClient(uuid, port=8100)

# 开超级玩家
# myclient.xpath("//*[@label=\"星球\"]").click()
# myclient.xpath("//*[@label=\"超级玩家\"]").click()
# myclient.swipe_up()
# myclient.swipe(0.7, 0.758, 0.204, 0.768)
# myclient.xpath("//*[@label=\"¥3\"]").click()
# myclient.xpath("//*[@label=\"立即开通 体验7天\"]").click()
# myclient.xpath("//*[@label=\"订阅\"]").click()
# time.sleep(5)
# if myclient(label="购买").exists:
#     myclient.xpath("//*[@label=\"购买\"]").click()
#     myclient.xpath("//*[@label=\"好\"]").click()
#     time.sleep(5)
# else:
#     myclient.send_keys("860822!Zzpg")
#     myclient.xpath("//*[@label=\"登录\"]").click()
#     myclient.xpath("//*[@label=\"购买\"]").click()
#     myclient.xpath("//*[@label=\"好\"]").click()
# myclient.xpath(
#     "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/WebView[1]/WebView[1]/WebView[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]").click()

# 送礼物
# myclient.xpath("//*[@label=\"搜大神、搜房间、搜玩友\"]").click()
# myclient.send_keys("588815")
# myclient.xpath("//*[@label=\"搜索\"]").click()
# myclient.click(0.109, 0.291)
# myclient.xpath("//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/Button[1]").click()
# myclient.xpath("//*[@label=\"送礼物\"]").click()
# 送普通礼物
# myclient.xpath("//*[@label=\"星耀票\"]").click()
# myclient.xpath("//*[@label=\"送礼\"]").click()
# 送福袋
# myclient.swipe_up()
# myclient.xpath("//*[@label=\"特别\"]").click()
# myclient.xpath("//*[@label=\"初级水晶球\"]").click()
# myclient.xpath("//*[@label=\"送礼\"]").click()
# myclient.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
# myclient.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
# myclient.xpath('//CollectionView/Cell[4]/Other[1]/Image[1]').click()
# time.sleep(1)
# myclient.click(0.901, 0.089)

# 充值
myclient.click(0.343, 0.204)
myclient.send_keys("588815")
myclient.xpath("//*[@label=\"充值中心\"]/Other[9]").click()
myclient.swipe_up()
myclient.xpath("//Switch").click()
myclient.xpath("//*[@label=\"微信支付\"]").click()
time.sleep(3)
myclient.xpath("//ScrollView/Other[1]/WebView[1]/Other[1]/Other[2]/Other[2]/Button[2]/StaticText[1]").click()
time.sleep(3)
myclient.xpath("//*[@label=\"立即支付\"]").click()
myclient.click(0.631, 0.652)
myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]").click()
myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[6]").click()
myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[0]").click()
myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]").click()
myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]").click()
myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]").click()
