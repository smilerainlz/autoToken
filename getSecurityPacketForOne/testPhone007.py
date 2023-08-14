import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
myclient = wda.USBClient("984e38e08278e882dda3017fc916d873d457b13d", port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        time.sleep(10)

    # 打开cm
    hello.initNoClose(myclient, "cm")
    # hello.process(myclient, "lg0811200", "myPhone", "username", "false", 0)
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "ppx")
