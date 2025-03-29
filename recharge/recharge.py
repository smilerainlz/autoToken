import wda, codecs, time


def process(client, userId):
    userId = userId.strip().replace(' ', '').replace('\n', '')
    print(userId)
    if client(label="取消").exists:
        client(label="取消").click()
        time.sleep(3)
        if client(label="取消").exists:
            client(label="取消").click()
    if client(label="确定").exists:
        client(label="确定").click()
    client.xpath('//*[@label=""]').click()
    client.xpath('//*[@label=""]').clear_text()
    client.send_keys(userId)
    time.sleep(1)
    if client.xpath("//*[@label=\"充值中心\"]/TextField").value == "588815":
        client(label="完成").click()
        time.sleep(2)
        client.xpath('//*[@label="充值中心"]/Other[9]').click()
        myclient.swipe_up()
        time.sleep(1)
        if client.xpath("//Switch").value == 0:
            myclient.xpath("//Switch").click()
        client(label="微信支付").click()
        time.sleep(3)
        if client(label="打开").exists:
            client(label="打开").click()
        print('购买Hello语音钻石到账号ID' + userId)
        client(label="立即支付").click()
        client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]/StaticText[1]').click()
        client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[6]/StaticText[1]').click()
        client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[10]/StaticText[1]').click()
        client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]/StaticText[1]').click()
        client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]/StaticText[1]').click()
        client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]/StaticText[1]').click()
        client(label="完成").click()

myclient = wda.USBClient("00008110-001A21803482401E", port=8100)
file = codecs.open("helloid.txt", 'r', "utf-8")
myclient.home()
myclient(label="Safari浏览器").click()
time.sleep(2)
for line in file:
    process(myclient, line)
file.close()
