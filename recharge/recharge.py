import os, wda, codecs, time, sys

def process(client,userId):
    print(userId)
    client.xpath('//*[@label=""]').click()
    client.xpath('//*[@label=""]').clear_text()
    client.send_keys(userId)
    client(label="完成").click()
    time.sleep(30)

# 本机
# myclient = wda.USBClient("00008101-000958911A91001E",port=8100)
# 测试机器
myclient = wda.USBClient("00008101-0006310A0C32001E", port=8100)
# ipad
# myclient = wda.USBClient("00008030-001E245A21C0202E", port=8100)
myclient.home()
myclient(label="Safari浏览器").click()
while True:
    file = codecs.open("first.txt", 'r', "utf-8")
    for line in file:
        process(myclient, line)
    file.close()
