import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
# 本机
# myclient = wda.USBClient("00008101-000958911A91001E",port=8100)
# 测试机器
# myclient = wda.USBClient("00008101-0006310A0C32001E", port=8100)
# ipad-1
myclient = wda.USBClient("00008030-001E245A21C0202E", port=8100)
# 本机（新）
# myclient = wda.USBClient("00008110-001A21803482401E", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 5 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)

    # 打开cm
    hello.init(myclient)
    hello.process(myclient, "m13211870646", "ipad", "username", "false", 2)
    hello.process(myclient, "q3452725271", "ipad", "username", "false", 2)
    hello.process(myclient, "m18559530951", "ipad", "username", "false", 2)
    hello.process(myclient, "id82560797", "ipad", "username", "false", 2)
