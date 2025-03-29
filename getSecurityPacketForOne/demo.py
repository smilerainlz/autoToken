import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0052"

myclient = wda.USBClient(uuid, port=8100)

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