import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
# 本机
myclient = wda.USBClient("00008101-000958911A91001E",port=8100)
# 测试机器
# myclient = wda.USBClient("00008101-0006310A0C32001E", port=8100)
# ipad
# myclient = wda.USBClient("00008030-001E245A21C0202E", port=8100)
# 本机（新）
# myclient = wda.USBClient("00008110-001A21803482401E", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 50 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)

    # 打开cm
    myclient.session().app_terminate("sg.bigo.orangy")
    myclient.session().app_activate("sg.bigo.orangy")
    hello.processNew(myclient, "Linjingjing", "myPhone", "username", "false", 1)
    time.sleep(30)
