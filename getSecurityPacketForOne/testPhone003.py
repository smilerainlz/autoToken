import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("010c2c6dd46d94ab3f129697112f74b3a2367f75", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)

    # 打开cm
    myclient.session().app_terminate("sg.bigo.orangy")
    myclient.session().app_activate("sg.bigo.orangy")
    hello.process(myclient, "m13211870646", "myPhone", "username", "false", 0)
    hello.processNew(myclient, "hello334407", "myPhone", "username", "false", 1, "hello")
