import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("08771801cd4ba47bd323204310a296c6e05e2b1a", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        print("重启charles")
        time.sleep(10)

    # 打开cm
    hello.initNoClose(myclient, "hello")
    # hello.process(myclient, "bao33225520", "phone", "username", "false", 0, "hello")
    hello.processNew(myclient, "hello334407", "myPhone", "username", "false", 1, "hello")
