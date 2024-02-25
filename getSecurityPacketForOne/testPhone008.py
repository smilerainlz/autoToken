import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("dfb8efa033b55e38bcda1c0b6ac9627451c7de42", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        print("重启charles")
        time.sleep(10)

    # 打开cm
    hello.initNoClose(myclient, "hello")
    hello.process(myclient, "zm091019", "phone", "username", "false", 0, "hello")
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "hello")
