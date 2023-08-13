import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("00008030-001E245A21C0202E", port=8100)
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
        hello.process(myclient, line, "ipad", "phone", "true", 0)
    file_cm.close()
    time.sleep(3)
