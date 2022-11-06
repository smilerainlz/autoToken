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

def modifyPwd(client):
    client(label="我的").click()
    time.sleep(1)
    client.xpath('//Table/Cell[7]').click()
    time.sleep(1)
    client.xpath('//Table/Cell[3]').click()
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/SecureTextField[1]').click()
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/SecureTextField[1]').set_text("123321zz1029")
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]').click()
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]').set_text("qwe12345")
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').click()
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').set_text("qwe12345")
    time.sleep(1)
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]').click()
    time.sleep(1)
    client(label="ppx ic common back black").click()
    client(label="ppx ic common back black").click()

def login(client, username, appName):
    print("当前时间: %s" % time.ctime())
    print(username)
    # 如果未勾选用户协议，勾选
    if not client(className="XCUIElementTypeOther").accessible:
        client.click(0.09, 0.893)
    # 选择用户名登录
    client(label="手机登录/注册").click()
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
myclient = wda.USBClient()
while True:
    # 打开ppx
    myclient.session().app_terminate("sg.bigo.pipixia")
    myclient.session().app_activate("sg.bigo.pipixia")
    if myclient(label="确定").exists:
        myclient(label="确定").click()
    # 初始化一次，如果未退出就退出
    close(myclient, "ppx")

    file_ppx = codecs.open("username_ppx.txt", 'r', "utf-8")
    for line in file_ppx:
        test_preferences(myclient, line, "ppx")
    file_ppx.close()
    time.sleep(3)
