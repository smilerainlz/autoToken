import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
uuid = "77df71489bd1227029fad1ce678d80490f52196e"
key = "0011"
try:
    myclient = wda.USBClient(uuid, port=8100)
except:
    os.system(
        "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " kill com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
    os.system(
        "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " launch com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
    myclient = wda.USBClient(uuid, port=8100)
while True:
    runCount = runCount + 1
    # 循环超过5次重启charles
    if runCount % 200 == 0:
        os.system('sh ../charles-start.sh')
        print("重启charles")
        time.sleep(10)

    # 打开cm
    hello.initNoClose(myclient, "hello")
    # hello.process(myclient, "id82560797", "phone", "username", "false", 0, "hello")
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "hello")

    hello.initNoClose(myclient, "cm")
    # hello.process(myclient, "m13175225697", "phone", "username", "false", 0, "cm")
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "cm")

    hello.initNoClose(myclient, "ppx")
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "ppx")
