import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "00008110-001A21803482401E"
key = "0052"

client = wda.USBClient(uuid, port=8100)

# 送礼物
client.xpath("//*[@label=\"搜大神、搜房间、搜玩友\"]").click()
client.send_keys("588815")
client.xpath("//*[@label=\"搜索\"]").click()
client.click(0.109, 0.291)
client.xpath(
    "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/Button[1]").click()
if client.xpath("//*[@label=\"ID: 588815\"]").exists:
    client.xpath("//*[@label=\"送礼物\"]").click()
    # 送普通礼物
    # client.xpath("//*[@label=\"星耀票\"]").click()
    # client.xpath("//*[@label=\"送礼\"]").click()
    # 送福袋
    client.swipe_up()
    client.xpath("//*[@label=\"特别\"]").click()
    client.xpath("//*[@label=\"初级水晶球\"]").click()
    client.xpath("//*[@label=\"送礼\"]").click()
    time.sleep(1)
    if client(label="取消").exists:
        client(label="取消").click()
client.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
client.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
client.xpath('//CollectionView/Cell[4]/Other[1]/Image[1]').click()
time.sleep(1)
client.click(0.901, 0.089)
