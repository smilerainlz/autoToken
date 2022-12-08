import wda, codecs, time

def process(d, userId):
    userId = userId.strip().replace(' ', '').replace('\n', '')
    print(userId)
    d.home()
    d(label="Safari浏览器").click()
    time.sleep(2)
    if d(label="取消").exists:
        d(label="取消").click()
    if d(label="确定").exists:
        d(label="确定").click()
    d.xpath('//*[@label=""]').click()
    d.xpath('//*[@label=""]').clear_text()
    d.send_keys(userId)
    d(label="完成").click()
    time.sleep(2)
    d.xpath('//*[@label="充值中心"]/Other[12]').click()
    if d(className="XCUIElementTypeSwitch").value == "0":
        d.xpath('//Switch').click()
    d.swipe(0.5, 0.5, 0.5, 0.01)
    d(label="微信支付").click()
    time.sleep(2)
    if d(label="打开").exists:
        d(label="打开").click()
    print('购买Hello语音钻石到账号ID' + userId)
    if d(className="XCUIElementTypeStaticText")[2].value != (
            '购买Hello语音钻石到账号ID' + userId):
        print("充值账号错误，无限睡眠：" + d(className="XCUIElementTypeStaticText")[2].value)
        time.sleep(5000000)
    d(label="立即支付").click()
    if d(label="确认支付").exists:
        d(label="确认支付").click()
    d.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]/StaticText[1]').click()
    d.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[6]/StaticText[1]').click()
    d.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[10]/StaticText[1]').click()
    d.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[8]/StaticText[1]').click()
    d.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]/StaticText[1]').click()
    d.xpath('//Window[3]/Other[1]/Other[1]/Other[2]/Key[2]/StaticText[1]').click()
    d(label="完成").click()


# 本机
myclient = wda.USBClient("00008101-000958911A91001E", port=8100)
# 测试机器
# myclient = wda.USBClient("00008101-0006310A0C32001E", port=8100)
# ipad
# myclient = wda.USBClient("00008030-001E245A21C0202E", port=8100)
file = codecs.open("first.txt", 'r', "utf-8")
for line in file:
    process(myclient, line)
file.close()
