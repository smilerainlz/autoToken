import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("77df71489bd1227029fad1ce678d80490f52196e", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)

    # 打开cm
    hello.initNoClose(myclient, "hello")
    # hello.process(myclient, "lg0811200", "myPhone", "username", "false", 0)
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "hello")