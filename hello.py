import time, wda, os, codecs


def addFirend(client):
    time.sleep(2)
    client.click(0.205, 0.149)
    client.send_keys("80716857")
    client(label="搜索").click()
    time.sleep(1)
    client.click(0.26, 0.148)
    time.sleep(1)
    client.click(0.106, 0.307)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[3]/Button[1]/StaticText[1]').click_exists(
        timeout=3.0)
    client(label="orangy ic profile back icon").click()
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
        "zzz12345")
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]').click_exists(
        timeout=3.0)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]').set_text(
        "qwe$1234")
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').click_exists(
        timeout=3.0)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').set_text(
        "qwe$1234")
    time.sleep(1)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]').click_exists(
        timeout=3.0)
    time.sleep(1)
    client(label="orangy ic common back black").click()
    time.sleep(1)


# appName(cm or ppx)
# loginType(phone or username)
def login(client, username, password, loginType):
    print("当前时间: %s" % time.ctime())
    print(username, end="")
    # 如果未勾选用户协议，勾选
    if not client(className="XCUIElementTypeOther").accessible:
        client.click(0.09, 0.893)
    # 选择用户名登录
    if loginType == "phone":
        client(label="手机登录/注册").click()
        time.sleep(5)
        if client(label="其他号码登录 >").exists:
            client(label="其他号码登录 >").click()
    if loginType == "username":
        client.click(0.821, 0.817)
    # 清空用户名并输入用户名
    client(className="XCUIElementTypeTextField").clear_text()
    client(className="XCUIElementTypeTextField").set_text(username)
    # 点击密码输入框并输入密码
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]/StaticText[1]').click_exists(
        timeout=3.0)
    client(className="XCUIElementTypeSecureTextField").set_text(password)
    # 点击登录
    client.xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[2]').click_exists(
        timeout=3.0)


def close(client, isLogin):
    time.sleep(3)
    # 如果弹出签到提示，先签到，再关闭
    if client(label="daily reward close").exists:
        client.xpath(
            '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        time.sleep(3)
        client(label="daily reward close").click()
    # 退出
    if isLogin == "true":
        client(label="我的").click()
        client.click(0.927, 0.088)
        client.xpath('//ScrollView/Button[10]').click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    if isLogin != "true":
        if client(label="我的").exists:
            client(label="我的").click()
            client.click(0.927, 0.088)
            client.xpath('//ScrollView/Button[10]').click()
            client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()


def closeForIpad(client, isLogin):
    time.sleep(3)
    # 如果弹出签到提示，先签到，再关闭
    if client(label="daily reward close").exists:
        client.xpath(
            '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        time.sleep(3)
        client(label="daily reward close").click()
    # 退出
    if isLogin == "true":
        client(label="我的").click()
        client.click(0.975, 0.043)
        client.xpath('//ScrollView/Button[10]').click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    if isLogin != "true":
        if client(label="我的").exists:
            client(label="我的").click()
            client.click(0.975, 0.043)
            client.xpath('//ScrollView/Button[10]').click()
            client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()


def init(client, appType):
    if appType == "cm":
        client.session().app_terminate("sg.bigo.orangy")
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        client.session().app_terminate("sg.bigo.pipixia")
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        client.session().app_terminate("com.yy.hello")
        client.session().app_activate("com.yy.hello")
    if client(label="确定").exists:
        client(label="确定").click()
    close(client, "false")


def initForIpad(client, appType):
    if appType == "cm":
        client.session().app_terminate("sg.bigo.orangy")
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        client.session().app_terminate("sg.bigo.pipixia")
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        client.session().app_terminate("com.yy.hello")
        client.session().app_activate("com.yy.hello")
    if client(label="确定").exists:
        client(label="确定").click()
    closeForIpad(client, "false")


def initNoClose(client, appType):
    if appType == "cm":
        client.session().app_terminate("sg.bigo.orangy")
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        client.session().app_terminate("sg.bigo.pipixia")
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        client.session().app_terminate("com.yy.hello")
        client.session().app_activate("com.yy.hello")


def getDiamond(client):
    client(label="我的").click()
    client.xpath('//Table/Cell[1]').click()
    time.sleep(3)
    print(client(className="XCUIElementTypeStaticText")[5].value)
    client(label="orangy ic common back black").click()


def getSecurityPacket(client, isGetSecurityPacket, appType):
    if appType == "cm":
        client(label="广场").click()
        time.sleep(3)
        client(label="发现").click()
    if appType == "ppx":
        client(label="广场").click()
        time.sleep(3)
        client(label="发现").click()
    if appType == "hello":
        client(label="星球").click()
    time.sleep(5)
    client(label="超级玩家").click()
    time.sleep(20)
    # client.click(0.566, 0.896)
    time.sleep(1)
    client.swipe(0.5, 0.8, 0.5, 0.5)
    time.sleep(2)
    client.click(0.566, 0.896)
    time.sleep(1)
    if isGetSecurityPacket == 1:
        # for i in range(5):
        client.click(0.566, 0.896)
        # time.sleep(60)
    time.sleep(1)
    client.click(0.066, 0.077)
    # client.xpath(
    #    '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/WebView[1]/WebView[1]/WebView[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]').click()
    # client(label="orangy ic common back black").click()


# loginType(phone or username)
# isCheckDiamond是否查看钻石（true获取）
# isGetSecurityPacket是否获取securityPacket（1：1个号循环获取，2：多个号获取）
def process(client, username, password, loginType, isCheckDiamond, isGetSecurityPacket, appType):
    # 登录
    login(client, username, password, loginType)
    if client(label="daily reward close").exists:
        client.xpath(
            '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]').click()
        time.sleep(3)
        client(label="daily reward close").click()
    if client(label="icon close interest label").exists:
        client(label="icon close interest label").click()
    # 如果登录过期
    if client(label="确定").exists:
        client(label="确定").click()
        # 重新登录
        login(client, username, loginType)
    if isCheckDiamond == "true":
        getDiamond(client)
    if isGetSecurityPacket >= 1:
        getSecurityPacket(client, isGetSecurityPacket, appType)
    close(client, "true")


def processNew(client, isGetSecurityPacket, appType):
    time.sleep(5)
    if client(label="daily reward close").exists:
        client.xpath("//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]").click()
        client(label="daily reward close").click()
    if isGetSecurityPacket >= 1:
        try:
            getSecurityPacket(client, isGetSecurityPacket, appType)
        except:
            print(appType + " : 号被顶了")
    time.sleep(10)


def doAll(uuid, key):
    runCount = 0
    try:
        myclient = wda.USBClient(uuid, port=8100)
    except:
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " kill com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " launch com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        myclient = wda.USBClient(uuid, port=8100)
    while True:
        runCount = runCount + 1
        # 循环超过5次重启charles
        if runCount % 200 == 0:
            os.system('sh ../charles-start.sh')
            print("重启charles")
            time.sleep(10)

        # 打开cm
        initNoClose(myclient, "hello")
        # process(myclient, "bmbm123", "username", "false", 0, "hello")
        processNew(myclient, 1, "hello")

        initNoClose(myclient, "cm")
        processNew(myclient, 1, "cm")

        initNoClose(myclient, "ppx")
        processNew(myclient, 1, "ppx")


def doFromFile(uuid, key, fileName):
    runCount = 0
    try:
        myclient = wda.USBClient(uuid, port=8100)
    except:
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " kill com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " launch com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        myclient = wda.USBClient(uuid, port=8100)
    init(myclient, "hello")
    while True:
        runCount = runCount + 1
        # 循环超过5次重启charles
        if runCount % 200 == 0:
            os.system('sh ../charles-start.sh')
            print("重启charles")
            time.sleep(10)

        # 打开cm
        while True:
            file_cm = codecs.open("../data/" + fileName + ".txt", 'r', "utf-8")
            for line in file_cm:
                try:
                    process(myclient, line.split("----")[0], line.split("----")[1], "username", "false", 1, "hello")
                except:
                    init(myclient, "hello")
                    process(myclient, line.split("----")[0], line.split("----")[1], "username", "false", 1, "hello")