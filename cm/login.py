import os,wda,codecs,time

def addFirend(d):
    d.click(0.63, 0.145)
    d.send_keys("83881191")
    d(label="search").click()
    time.sleep(1)
    d.click(0.26, 0.148)
    time.sleep(1)
    d.click(0.106, 0.307)
    d.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[3]/Button[1]/StaticText[1]').click()
    d(label="orangy ic profile back icon").click()
    time.sleep(1)
    d.click(0.893, 0.094)

def removeGZ(d):
    d(label="我的").click()
    d.xpath('//Table/Other[1]/Other[2]/Other[3]').click()
    while True :
        d.xpath('//Table/Button[2]/StaticText[1]').click()
        d.xpath('//NavigationBar/Button[2]/StaticText[1]').click()
        d.xpath('//Table/Cell[2]/Button[1]').click()
        d.xpath('//Table/Cell[3]/Button[1]').click()
        d.xpath('//Table/Cell[4]/Button[1]').click()
        d.xpath('//Table/Cell[5]/Button[1]').click()
        d.xpath('//Table/Cell[6]/Button[1]').click()
        d.xpath('//Table/Cell[7]/Button[1]').click()
        d.xpath('//Table/Cell[8]/Button[1]').click()
        d.xpath('//Table/Cell[9]/Button[1]').click()
        d.xpath('//Table/Cell[10]/Button[1]').click()
        d.xpath('//NavigationBar/Button[2]/StaticText[1]').click()
        d.xpath('//Window[1]/Other[2]/Other[2]/Button[3]/StaticText[1]').click()

def test_preferences(client,username):
    #print("Status:", client.status())
    #print("Info:", client.info)
    #print("BatteryInfo", client.battery_info())
    #print("AppCurrent:", client.app_current())
    print("当前时间: %s" % time.ctime())
    print(username)
    if not client(className="XCUIElementTypeOther").accessible :
    	client.click(0.09, 0.893)
    client(label="orangy ic UserName Login Icon").click()
    client(className="XCUIElementTypeTextField").clear_text()
    client(className="XCUIElementTypeTextField").set_text(username)
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]/StaticText[1]').click()
    client(className="XCUIElementTypeSecureTextField").set_text("qwe12345")
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[2]').click()
    time.sleep(3)
    if client(label="确定").exists :
        client(label="确定").click()
        time.sleep(3)
    if client(label="daily reward close").exists :
        client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        time.sleep(3)
        client(label="daily reward close").click()
    #addFirend(client)
    if client(label="我的").exists :
        client(label="我的").click()
        client(label="orangy ic hl me page setting i").click()
        client.xpath('//ScrollView/Button[10]').click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    time.sleep(1)

runCount=0
myclient = wda.USBClient()
myclient.session().app_terminate("sg.bigo.orangy")
myclient.session().app_activate("sg.bigo.orangy")
time.sleep(5)
if myclient(label="daily reward close").exists :
    myclient.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
    time.sleep(3)
    myclient(label="daily reward close").click()
if myclient(label="我的").exists :
    myclient(label="我的").click()
    myclient(label="orangy ic hl me page setting i").click()
    myclient.xpath('//ScrollView/Button[10]').click()
    myclient.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
while True :
    runCount = runCount + 1
    if runCount%10==0:
        os.system('sh ../charles-start.sh')
    file = codecs.open("username.txt", 'r', "utf-8")
    for line in file:
        test_preferences(myclient,line)
    file.close()
    time.sleep(1)
