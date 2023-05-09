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
        time.sleep(10)

    # 打开cm
    myclient.session().app_terminate("sg.bigo.pipixia")
    myclient.session().app_activate("sg.bigo.pipixia")
    hello.processNew(myclient, "hello334407", "myPhone", "username", "false", 1)
    time.sleep(30)