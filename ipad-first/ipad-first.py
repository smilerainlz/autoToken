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
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 5 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)
    # 打开cm
    hello.init(myclient, "cm")

    file_cm = codecs.open("../data/base_cm.txt", 'r', "utf-8")
    for line in file_cm:
        hello.process(myclient, line, "cm", "ipad", "username")
    file_cm.close()
    time.sleep(3)

    # 打开ppx
    hello.init(myclient, "ppx")

    file_ppx = codecs.open("../data/base_ppx.txt", 'r', "utf-8")
    for line in file_ppx:
        hello.process(myclient, line, "ppx", "ipad", "username")
    file_ppx.close()
    time.sleep(3)