import os, wda, codecs, time


def addFirend(client, appName):
    client.click(0.63, 0.145)
    client.send_keys("83881191")
    client(label="search").click()
    time.sleep(1)
    client.click(0.26, 0.148)
    time.sleep(1)
    client.click(0.106, 0.307)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[3]/Button[1]/StaticText[1]').click()
    if appName == "cm":
        client(label="orangy ic profile back icon").click()
    if appName == "ppx":
        client(label="ppx ic profile back icon").click()
    time.sleep(1)
    client.click(0.893, 0.094)


def removeGZ(client):
    client(label="我的").click()
    client.xpath('//Table/Other[1]/Other[2]/Other[3]').click()
    while True:
        client.xpath('//Table/Button[2]/StaticText[1]').click()
        client.xpath('//NavigationBar/Button[2]/StaticText[1]').click()
        client.xpath('//Table/Cell[2]/Button[1]').click()
        client.xpath('//Table/Cell[3]/Button[1]').click()
        client.xpath('//Table/Cell[4]/Button[1]').click()
        client.xpath('//Table/Cell[5]/Button[1]').click()
        client.xpath('//Table/Cell[6]/Button[1]').click()
        client.xpath('//Table/Cell[7]/Button[1]').click()
        client.xpath('//Table/Cell[8]/Button[1]').click()
        client.xpath('//Table/Cell[9]/Button[1]').click()
        client.xpath('//Table/Cell[10]/Button[1]').click()
        client.xpath('//NavigationBar/Button[2]/StaticText[1]').click()
        client.xpath('//Window[1]/Other[2]/Other[2]/Button[3]/StaticText[1]').click()


def login(client, username, appName):
    print("当前时间: %s" % time.ctime())
    print(username)
    # 如果未勾选用户协议，勾选
    if not client(className="XCUIElementTypeOther").accessible:
        client.click(0.09, 0.893)
    # 选择用户名登录
    if appName == "cm":
        client(label="orangy ic UserName Login Icon").click()
    if appName == "ppx":
        client(label="ppx ic UserName Login Icon").click()
    # 清空用户名并输入用户名
    client(className="XCUIElementTypeTextField").clear_text()
    client(className="XCUIElementTypeTextField").set_text(username)
    # 点击密码输入框并输入密码
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]/StaticText[1]').click()
    client(className="XCUIElementTypeSecureTextField").set_text("qwe12345")
    # 点击登录
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[2]').click()


def close(client, appName):
    # 如果弹出签到提示，先签到，再关闭
    if client(label="daily reward close").exists:
        client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        time.sleep(1)
        client(label="daily reward close").click()
    # 如果提示年度活动，关掉
    if appName == "cm":
        if client(label="orangy ic main activity close").exists:
            client(label="orangy ic main activity close").click()
    if appName == "ppx":
        if client(label="ppx ic main activity close").exists:
            client(label="ppx ic main activity close").click()
    # 退出
    if client(label="我的").exists:
        client(label="我的").click()
        if appName == "cm":
            client(label="orangy ic hl me page setting i").click()
        if appName == "ppx":
            client(label="ppx ic hl me page setting icon").click()
        client.xpath('//ScrollView/Button[10]').click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()


def test_preferences(client, username, appName):
    # 登录
    login(client, username, appName)
    time.sleep(3)
    # 如果登录过期
    if client(label="确定").exists:
        client(label="确定").click()
        # 重新登录
        login(client, username, appName)
        time.sleep(3)
    close(client, appName)


runCount = 0
# 本机
# myclient = wda.USBClient("00008101-000958911A91001E",port=8100)
# 测试机器
myclient = wda.USBClient("00008101-0006310A0C32001E",port=8100)
while True:
    # 打开cm
    myclient.session().app_terminate("sg.bigo.orangy")
    myclient.session().app_activate("sg.bigo.orangy")
    if myclient(label="确定").exists:
        myclient(label="确定").click()
    # 初始化一次，如果未退出就退出
    close(myclient, "cm")
    runCount = runCount + 1
    # 循环超过10次重启charles
    if runCount % 10 == 0:
        os.system('sh ../charles-start.sh')
    file_cm = codecs.open("username_cm.txt", 'r', "utf-8")
    for line in file_cm:
        test_preferences(myclient, line, "cm")
    file_cm.close()
    time.sleep(3)
