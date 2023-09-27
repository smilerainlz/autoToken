import os

import wda, time, sys, redis

try:
    myclient = wda.USBClient("15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4", port=8100)
except:
    os.system(
        "/Users/jfx/Library/Python/3.9/bin/tidevice -u 15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4 kill com.facebook.WebDriverAgentLib.lizhengtest021.xctrunner")
    os.system(
        "/Users/jfx/Library/Python/3.9/bin/tidevice -u 15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4 launch com.facebook.WebDriverAgentLib.lizhengtest021.xctrunner")
    time.sleep(3)
    myclient = wda.USBClient("15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4", port=8100)
    myclient.session().app_activate("com.yy.hello")
r = redis.Redis(host='garyhelo.redis.rds.aliyuncs.com', port=6379, db=0, password='Lz860822')
print("当前时间: %s" % time.ctime())
count = 0
while True:
    count = count + 1
    if count % 500 == 0:
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u 15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4 kill com.facebook.WebDriverAgentLib.lizhengtest021.xctrunner")
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u 15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4 launch com.facebook.WebDriverAgentLib.lizhengtest021.xctrunner")
        time.sleep(3)
        myclient.session().app_activate("com.yy.hello")
        print("当前时间: %s" % time.ctime() + " : 重启")
    if myclient.xpath(
            '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/StaticText[1]').wait(
        timeout=10):
        result = myclient.xpath(
            '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/StaticText[1]').value
        if "九尾离火" in result:
            r.set("myFlagCount", "-1")
        print("当前时间: %s" % time.ctime())
        print(result)
        time.sleep(3)
