import wda, codecs, time


def process(client, userId):
    userId = userId.strip().replace(' ', '').replace('\n', '')
    print(userId)
    time.sleep(2)
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
    if client.xpath("//*[@label=\"充值中心\"]/TextField").value == userId:
        client(label="完成").click()
        time.sleep(2)
        client.xpath('//*[@label="充值中心"]/Other[10]').click()
        myclient.swipe_up()
        if client.xpath("//Switch").value == "0":
            time.sleep(1)
            client.xpath("//Switch").click()
        client(label="微信支付").click()
        time.sleep(3)
        if client(label="打开").exists:
            client(label="打开").click()
        time.sleep(5)
        if client(label="购买Hello语音钻石到账号ID" + userId + "点  6点0 0元").exists:
            client(label="立即支付").click()
            if client(label="确认支付").exists:
                client(label="确认支付").click()
            client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]/StaticText[1]').click()
            client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[6]/StaticText[1]').click()
            client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[10]/StaticText[1]').click()
            client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]/StaticText[1]').click()
            client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]/StaticText[1]').click()
            client.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]/StaticText[1]').click()
            client(label="完成").click()
        else:
            print(userId + " : 充值id或金额错误，跳过！")
            client(label="取消").click()
            client(label="放弃").click()
    else:
        print(userId + " : 充值id错误，跳过！")


myclient = wda.USBClient("00008110-001A21803482401E", port=8100)
file = codecs.open("helloid.txt", 'r', "utf-8")
myclient.home()
myclient(label="Safari浏览器").click()
time.sleep(2)
for line in file:
    process(myclient, line)
file.close()
