import wda,codecs,time
def test_preferences(client,username):
    #print("Status:", client.status())
    #print("Info:", client.info)
    #print("BatteryInfo", client.battery_info())
    #print("AppCurrent:", client.app_current())
    print("当前时间: %s" % time.ctime())
    print(username)

    if not client(className="XCUIElementTypeOther").accessible :
    	client.click(0.09, 0.893)
    client(label="ppx ic UserName Login Icon").click()
    client(className="XCUIElementTypeTextField").clear_text()
    client(className="XCUIElementTypeTextField").set_text(username)
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]/StaticText[1]').click()
    client(className="XCUIElementTypeSecureTextField").set_text("123456yyy")
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[2]').click()
    time.sleep(10)
    if client(label="daily reward close").exists :
        client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        time.sleep(3)
        client(label="daily reward close").click()
    client(label="我的").click()
    client(label="ppx ic hl me page setting icon").click()
    client.xpath('//ScrollView/Button[10]').click()
    client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    time.sleep(1)

myclient = wda.USBClient()
myclient.session().app_terminate("sg.bigo.pipixia")
myclient.session().app_activate("sg.bigo.pipixia")
time.sleep(10)
if myclient(label="daily reward close").exists :
    myclient.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
    myclient(label="daily reward close").click()
if myclient(label="我的").exists :
    myclient(label="我的").click()
    myclient(label="ppx ic hl me page setting icon").click()
    myclient.xpath('//ScrollView/Button[10]').click()
    myclient.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
while True :
    file = codecs.open("username.txt", 'r', "utf-8")
    for line in file:
        test_preferences(myclient,line)
    file.close()
    time.sleep(10)