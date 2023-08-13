import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("c933eea94b3ba611f48322b9d9ebc02e9c1efef1", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 50 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)
    # 打开cm
    hello.init(myclient,"cm")

    file_cm = codecs.open("../data/blindbox.txt", 'r', "utf-8")
    for line in file_cm:
        hello.process(myclient, line, "phone", "phone", "false", 0)
    file_cm.close()
    time.sleep(3)
