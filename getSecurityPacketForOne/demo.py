import sys,wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0052"


# 送礼物
myclient = wda.USBClient(uuid, port=8100)
myclient.xpath("//*[@label=\"搜大神、搜房间、搜玩友\"]").click()
myclient.send_keys("588815")
myclient.xpath("//*[@label=\"搜索\"]").click()
myclient.click(0.109, 0.291)
myclient.xpath("//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/Button[1]").click()
myclient.xpath("//*[@label=\"送礼物\"]").click()
#送普通礼物
#myclient.xpath("//*[@label=\"星耀票\"]").click()
#myclient.xpath("//*[@label=\"送礼\"]").click()
#送福袋
myclient.swipe_up()
myclient.xpath("//*[@label=\"特别\"]").click()
myclient.xpath("//*[@label=\"初级水晶球\"]").click()
myclient.xpath("//*[@label=\"送礼\"]").click()
myclient.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
myclient.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
myclient.xpath('//CollectionView/Cell[4]/Other[1]/Image[1]').click()
time.sleep(1)
myclient.click(0.901, 0.089)

# 充值
# myclient.click(0.343, 0.204)
# myclient.send_keys("588815")
# myclient.xpath("//*[@label=\"充值中心\"]/Other[9]").click()
# myclient.swipe_up()
# myclient.xpath("//Switch").click()
# myclient.xpath("//*[@label=\"微信支付\"]").click()
# time.sleep(3)
# myclient.xpath("//ScrollView/Other[1]/WebView[1]/Other[1]/Other[2]/Other[2]/Button[2]/StaticText[1]").click()
# time.sleep(3)
# myclient.xpath("//*[@label=\"立即支付\"]").click()
# myclient.click(0.631, 0.652)
# myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]").click()
# myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[6]").click()
# myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[0]").click()
# myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]").click()
# myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]").click()
# myclient.xpath("//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]").click()