import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("00008101-0006310A0C32001E", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 50 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)
    # 打开cm
    hello.init(myclient)

    file_cm = codecs.open("../data/lottery.txt", 'r', "utf-8")
    for line in file_cm:
        hello.process(myclient, line, "testPhone", "username", "true", 0)
    file_cm.close()
    time.sleep(300)
