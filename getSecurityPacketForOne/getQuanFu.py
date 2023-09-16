import wda, time, sys, redis

myclient = wda.USBClient("15b6ddd0b40473b4c753ad9ff7dddad149cf6eb4", port=8100)
r = redis.Redis(host='garyhelo.redis.rds.aliyuncs.com', port=6379, db=0, password='Lz860822')
print("当前时间: %s" % time.ctime())
while True:
    if myclient.xpath(
            '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/StaticText[1]').exists:
        r.set("myFlagCount", "-1")
        print("当前时间: %s" % time.ctime())
        # if "万众瞩目，火速围观" in myclient.xpath(
        #         '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/StaticText[1]').value:
        #     print("当前时间: %s" % time.ctime() + "：抽奖")
        # else:
        #     time.sleep(10)
        #     r.set("myFlagCount", "10")
        #     print("当前时间: %s" % time.ctime() + "：福袋")
        # print(myclient.xpath(
        #    '//Window/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/Other[1]/StaticText[1]').value)
        time.sleep(30)
        r.set("myFlagCount", "10")
    time.sleep(1)
