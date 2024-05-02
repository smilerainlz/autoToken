import os, wda, codecs, time, sys

sys.path.append("..//")
import hello

runCount = 0
uuid = "15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4"
key = "0015"
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
    # hello.process(myclient, "bmbm123", "phone", "username", "false", 0, "hello")
    hello.processNew(myclient, "bmbm123", "myPhone", "username", "false", 1, "hello")

    hello.initNoClose(myclient, "cm")
    hello.processNew(myclient, "bmbm123", "myPhone", "username", "false", 1, "cm")

    hello.initNoClose(myclient, "ppx")
    hello.processNew(myclient, "hello5555", "myPhone", "username", "false", 1, "ppx")
