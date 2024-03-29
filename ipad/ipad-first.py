import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
# 本机
# myclient = wda.USBClient("00008101-000958911A91001E",port=8100)
# 测试机器
# myclient = wda.USBClient("00008101-0006310A0C32001E", port=8100)
# ipad
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
    hello.initForIpad(myclient, "cm")

    file_cm = codecs.open("../data/first.txt", 'r', "utf-8")
    for line in file_cm:
        hello.process(myclient, line, "ipad", "username", "false", 2)
    file_cm.close()
    time.sleep(3)
