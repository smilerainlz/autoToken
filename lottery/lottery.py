import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("010c2c6dd46d94ab3f129697112f74b3a2367f75", port=8100)
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
        hello.process(myclient, line, "phone", "phone", "false", 0)
    file_cm.close()
    time.sleep(500)
