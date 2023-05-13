import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("c933eea94b3ba611f48322b9d9ebc02e9c1efef1", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)

    # 打开cm
    myclient.session().app_terminate("sg.bigo.orangy")
    myclient.session().app_activate("sg.bigo.orangy")
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "cm")
