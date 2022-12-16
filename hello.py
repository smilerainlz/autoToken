import time


def addFirend(client, appName):
    client.click(0.63, 0.145)
    client.send_keys("83881191")
    client(label="search").click()
    time.sleep(1)
    client.click(0.26, 0.148)
    time.sleep(1)
    client.click(0.106, 0.307)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[3]/Button[1]/StaticText[1]').click_exists(
        timeout=3.0)
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
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/SecureTextField[1]').click_exists(
        timeout=3.0)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/SecureTextField[1]').set_text(
        "qwe12345")
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]').click_exists(
        timeout=3.0)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]').set_text(
        "qwe12345")
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').click_exists(
        timeout=3.0)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').set_text(
        "qwe12345")
    time.sleep(1)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]').click_exists(
        timeout=3.0)
    client(label="ppx ic common back black").click()
    client(label="ppx ic common back black").click()


# appName(cm or ppx)
# device(iphone or ipad)
# loginType(phone or username)
def login(client, username, device, loginType):
    print("当前时间: %s" % time.ctime())
    print(username, end="")
    # 如果未勾选用户协议，勾选
    if not client(className="XCUIElementTypeOther").accessible:
        if device == "myPhone" or device == "testPhone":
            client.click(0.09, 0.893)
        if device == "ipad":
            client.click(0.29, 0.959)
    # 选择用户名登录
    if loginType == "phone":
        client(label="手机登录/注册").click()
        if device == "myPhone":
            time.sleep(3)
            client(label="其他号码登录 >").click()
    if loginType == "username":
        client(label="orangy ic UserName Login Icon").click()
    # 清空用户名并输入用户名
    client(className="XCUIElementTypeTextField").clear_text()
    client(className="XCUIElementTypeTextField").set_text(username)
    # 点击密码输入框并输入密码
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]/StaticText[1]').click_exists(
        timeout=3.0)
    client(className="XCUIElementTypeSecureTextField").set_text("qwe12345")
    # 点击登录
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[2]').click_exists(
        timeout=3.0)


def close(client, isLogin):
    # 如果弹出签到提示，先签到，再关闭
    if client(label="daily reward close").exists:
        client.xpath(
            '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        client(label="daily reward close").click()
    # 如果提示年度活动，关掉
    if client(label="orangy ic main activity close").exists:
        client(label="orangy ic main activity close").click()
    # 退出
    if isLogin == "true":
        client(label="我的").click()
        client(label="orangy ic hl me page setting i").click()
        client.xpath('//ScrollView/Button[10]').click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    if isLogin != "true":
        if client(label="我的").exists:
            client(label="我的").click()
            client(label="orangy ic hl me page setting i").click()
            client.xpath('//ScrollView/Button[10]').click()
            client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()


def init(client):
    client.session().app_terminate("sg.bigo.orangy")
    client.session().app_activate("sg.bigo.orangy")
    if client(label="确定").exists:
        client(label="确定").click()
    close(client, "false")


def getDiamond(client, appName):
    client(label="我的").click()
    client.xpath('//Table/Cell[1]').click()
    time.sleep(3)
    print(client(className="XCUIElementTypeStaticText")[5].value)
    client(label="orangy ic common back black").click()


def getSecurityPacket(client, isGetSecurityPacket, device):
    client(label="发现").click()
    # if device == "ipad":
    #    client.swipe(0.5, 0.88, 0.5, 0.1)
    # if device != "ipad":
    #    client.swipe(0.5, 0.88, 0.5, 0.1)
    # time.sleep(1)
    client.swipe(0.5, 0.8, 0.5, 0.3)
    time.sleep(1)
    client.xpath('//Table/Cell[3]/Image[1]').click()
    time.sleep(2)
    if isGetSecurityPacket == 1:
        for i in range(7):
            client(label="orangy ic common back black").click()
            client.xpath('//Table/Cell[3]/Image[1]').click()
            time.sleep(120)
    client(label="orangy ic common back black").click()


# device(myPhone or testPhone or ipad)
# loginType(phone or username)
# isCheckDiamond是否查看钻石（true获取）
# isGetSecurityPacket是否获取securityPacket（1：1个号循环获取，2：多个号获取）
def process(client, username, device, loginType, isCheckDiamond, isGetSecurityPacket):
    try:
        # 登录
        login(client, username, device, loginType)
        # 如果登录过期
        if client(label="确定").exists:
            client(label="确定").click()
            # 重新登录
            login(client, username, device, loginType)
        if isCheckDiamond == "true":
            getDiamond(client)
        if isGetSecurityPacket >= 1:
            getSecurityPacket(client, isGetSecurityPacket, device)
        close(client, "true")
    except:
        print("捕获异常，重新调用登录")
        init(client)
        process(client, username, device, loginType, isCheckDiamond, isGetSecurityPacket)
