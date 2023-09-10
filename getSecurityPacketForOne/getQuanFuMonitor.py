import wda, time, sys, redis

sys.path.append("..//")

runCount = 0
myclient = wda.USBClient("010c2c6dd46d94ab3f129697112f74b3a2367f75", port=8100)
r = redis.Redis(host='garyhelo.redis.rds.aliyuncs.com', port=6379, db=0, password='Lz860822')
testa = "恭喜 电 获得 永夜的黎明 ，万众瞩目，火速围观！"
while True:
    myclient.click(0.5, 0.5)
    time.sleep(100)
