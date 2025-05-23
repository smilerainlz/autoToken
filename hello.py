import time, wda, os, codecs


def addFirend(client):
    time.sleep(2)
    client.click(0.205, 0.149)
    client.send_keys("588815")
    if client(label="搜索").exists:
        client(label="搜索").click()
    elif client(label="search").exists:
        client(label="search").click()
    time.sleep(1)
    client.click(0.106, 0.307)
    client(label="加为好友").click()
    time.sleep(1)
    client.click(0.852, 0.328)
    client(label="profile back icon").click()
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


def modifyPwd(client, password):
    client(label="我的").click()
    time.sleep(1)
    client(label="安全中心").click()
    time.sleep(1)
    client.xpath('//Table/Cell[3]').click()
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/SecureTextField[1]').set_text(
        password)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/SecureTextField[1]').set_text(
        "qwer1234$$$")
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]/SecureTextField[1]').set_text(
        "qwer1234$$$")
    time.sleep(1)
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]').click()
    time.sleep(1)
    client.click(0.051, 0.065)
    time.sleep(1)


def openAJSMethod(client, appType):
    client.session().app_activate("com.aijiasuinc.AiJiaSuClient")
    time.sleep(3)
    if client(label="home btn connect nor").exists:
        client(label="home btn connect nor").click()
        time.sleep(3)
    if appType == "cm":
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        client.session().app_activate("com.yy.hello")
    time.sleep(1)


def closeAJSMethod(client, appType):
    client.session().app_activate("com.aijiasuinc.AiJiaSuClient")
    time.sleep(3)
    if client(label="home btn connect sus").exists:
        client(label="home btn connect sus").click()
        time.sleep(3)
    if appType == "cm":
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        client.session().app_activate("com.yy.hello")
    time.sleep(1)


# appName(cm or ppx)
# loginType(phone or username)
def login(client, username, password, loginType, appType, openAJS):
    if openAJS == "true":
        openAJSMethod(client, appType)
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
        client.click(0.872, 0.75)
    # 清空用户名并输入用户名
    client(className="XCUIElementTypeTextField").clear_text()
    client(className="XCUIElementTypeTextField").set_text(username)
    # 点击密码输入框并输入密码
    client.xpath(
        '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]/StaticText[1]').click_exists(
        timeout=3.0)
    client(className="XCUIElementTypeSecureTextField").set_text(password)
    # 点击登录
    client(label="登录").click_exists(
        timeout=3.0)
    client(label="登 录").click_exists(
        timeout=3.0)
    time.sleep(3)
    if openAJS == "true":
        closeAJSMethod(client, appType)


def close(client, isLogin):
    # time.sleep(3)
    if client(label="确定", timeout=1.0).exists:
        client(label="确定").click()
    if client(label="取消", timeout=1.0).exists:
        client(label="取消").click()
    if client(label="知道了", timeout=1.0).exists:
        client(label="知道了").click()
    if client(label="daily reward close", timeout=1.0).exists:
        client.click(0.6, 0.7)
        time.sleep(3)
        client(label="daily reward close").click()
    # 退出
    if isLogin == "true":
        client(label="我的").click()
        if client(label="选好了").exists:
            client(label="选好了").click()
        client.click(0.927, 0.088)
        client(label="退出当前帐号").click()
        if client(label="下次再说", timeout=1.0).exists:
            client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
            client(label="退出当前帐号").click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    if isLogin != "true":
        if client(label="我的").exists:
            client(label="我的").click()
            if client(label="选好了").exists:
                client(label="选好了").click()
            client.click(0.927, 0.088)
            client(label="退出当前帐号").click()
            if client(label="下次再说").exists:
                client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
                client(label="退出当前帐号").click()
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
        client(label="退出当前帐号").click()
        client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()
    if isLogin != "true":
        if client(label="我的").exists:
            client(label="我的").click()
            client.click(0.975, 0.043)
            client(label="退出当前帐号").click()
            client.xpath('//Window[1]/Other[2]/Other[1]/Other[1]/Button[1]/StaticText[1]').click()


def init(client, appType, openAJS):
    if appType == "cm":
        client.session().app_terminate("sg.bigo.orangy")
        if openAJS == "true":
            openAJSMethod(client, appType)
        else:
            client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        client.session().app_terminate("sg.bigo.pipixia")
        if openAJS == "true":
            openAJSMethod(client, appType)
        else:
            client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        client.session().app_terminate("com.yy.hello")
        if openAJS == "true":
            openAJSMethod(client, appType)
        else:
            client.session().app_activate("com.yy.hello")
    close(client, "false")


def initForIpad(client, appType):
    if appType == "cm":
        # client.session().app_terminate("sg.bigo.orangy")
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        # client.session().app_terminate("sg.bigo.pipixia")
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        # client.session().app_terminate("com.yy.hello")
        client.session().app_activate("com.yy.hello")
    if client(label="确定").exists:
        client(label="确定").click()
    closeForIpad(client, "false")


def initNoClose(client, appType):
    if appType == "cm":
        # client.session().app_terminate("sg.bigo.orangy")
        client.session().app_activate("sg.bigo.orangy")
    if appType == "ppx":
        # client.session().app_terminate("sg.bigo.pipixia")
        client.session().app_activate("sg.bigo.pipixia")
    if appType == "hello":
        # client.session().app_terminate("com.yy.hello")
        client.session().app_activate("com.yy.hello")


def getDiamond(client):
    client(label="我的").click()
    client(label="我的钱包").click()
    time.sleep(3)
    print("     " + client(className="XCUIElementTypeStaticText")[5].value)
    client.click(0.06, 0.06)


def intoRoom(client):
    client(label="首页").click()
    client(label="心动女声").click()
    client(label="封坑踢保").click()
    client(label="声音恋人").click()
    time.sleep(1)
    client.xpath(
        "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/ScrollView[1]/Other[1]/Other[1]/CollectionView[1]/Cell[2]/Other[1]/Image[1]").click()
    # client.click(0.756, 0.677)
    time.sleep(5)
    client.click(0.93, 0.062)
    client.click(0.843, 0.097)


def openSuperPlayer(client):
    client.xpath("//*[@label=\"星球\"]").click()
    client.xpath("//*[@label=\"超级玩家\"]").click()
    client.click(0.566, 0.896)
    client.swipe_up()
    client.swipe(0.7, 0.758, 0.204, 0.768)
    client.xpath("//*[@label=\"¥3\"]").click()
    time.sleep(1)
    if client.xpath("//*[@label=\"立即开通 体验7天\"]").exists:
        client.xpath("//*[@label=\"立即开通 体验7天\"]").click()
        client.xpath("//*[@label=\"订阅\"]").click()
        time.sleep(5)
        if client(label="购买").exists:
            client.xpath("//*[@label=\"购买\"]").click()
            client.xpath("//*[@label=\"好\"]").click()
            time.sleep(5)
        else:
            client.send_keys("860822!Zzpg")
            client.xpath("//*[@label=\"登录\"]").click()
            client.xpath("//*[@label=\"购买\"]").click()
            client.xpath("//*[@label=\"好\"]").click()
    client.xpath(
        "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/WebView[1]/WebView[1]/WebView[1]/Other[1]/Other[1]/Other[1]/Other[1]/Button[1]").click()


def sendGift(client, username, sendUserId, sendType, sendName):
    client.xpath(
        "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[4]").click()
    client.send_keys(sendUserId)
    if client.xpath("//*[@label=\"搜索\"]").exists:
        client.xpath("//*[@label=\"搜索\"]").click()
    if client.xpath("//*[@label=\"search\"]").exists:
        client.xpath("//*[@label=\"search\"]").click()
    time.sleep(1)
    sendPackageMethed(client, username, sendUserId, sendType)
    time.sleep(1)
    client.click(0.901, 0.089)


def sendMethed(client, username, sendUserId, sendType, sendName):
    client.click(0.114, 0.31)
    time.sleep(1)
    client.click(0.501, 0.158)
    if client.xpath("//*[@label=\"ID: " + sendUserId + "\"]").exists:
        client.xpath("//*[@label=\"送礼物\"]").click()
        # 送普通礼物
        if sendType == "diamond":
            client.xpath("//*[@label=\"经典\"]").click()
        # 送福袋
        elif sendType == "package":
            client.xpath("//*[@label=\"包裹\"]").click()
            client.swipe_up()
            # client.swipe_up()
        else:
            client.xpath("//*[@label=\"特别\"]").click()
        if client.xpath("//*[@label=\"" + sendName + "\"]").exists:
            client.xpath("//*[@label=\"" + sendName + "\"]").click()
            client.xpath("//*[@label=\"送礼\"]").click()
        else:
            client.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
            print(username + " : 礼物不存在 ：" + sendName)
        time.sleep(1)
        if client(label="取消").exists:
            client(label="取消").click()
            print(username + " : 没钻了，请充值")
            client.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
    else:
        print(username + " : 送礼物失败")
    client.xpath("//*[@label=\"new chatroom navi bar more\"]").click()
    client.xpath('//CollectionView/Cell[4]/Other[1]/Image[1]').click()


# 聚宝盆、草莓冰棒、白桃啵啵、彩虹星、星月烙印、轻羽礼帽、金月星芒、吉吉松鼠、律动音符、兔兔雪糕
def sendPackageMethed(client, username, sendUserId, sendType):
    client.click(0.558, 0.345)
    time.sleep(2)
    if client(label="ID: " + sendUserId).exists:
        client(label="profile menu icon").click()
        client.xpath("//*[@label=\"送礼物\"]").click()
        # 送普通礼物
        if sendType == "diamond":
            client.xpath("//*[@label=\"经典\"]").click()
        # 送福袋
        elif sendType == "package":
            client.xpath("//*[@label=\"包裹\"]").click()
            client.swipe_up()
            # client.swipe_up()
        else:
            client.xpath("//*[@label=\"特别\"]").click()
        while True:
            if client.xpath("//*[@label=\"聚宝盆\"]").exists:
                client.xpath("//*[@label=\"聚宝盆\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            if client.xpath("//*[@label=\"礼花\"]").exists:
                client.xpath("//*[@label=\"礼花\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"草莓冰棒\"]").exists:
                client.xpath("//*[@label=\"草莓冰棒\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            if client.xpath("//*[@label=\"律动音符\"]").exists:
                client.xpath("//*[@label=\"律动音符\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"许愿瓶\"]").exists:
                client.xpath("//*[@label=\"许愿瓶\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"多色笔\"]").exists:
                client.xpath("//*[@label=\"多色笔\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"西瓜冰棒\"]").exists:
                client.xpath("//*[@label=\"西瓜冰棒\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"白桃啵啵\"]").exists:
                client.xpath("//*[@label=\"白桃啵啵\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"彩虹星\"]").exists:
                client.xpath("//*[@label=\"彩虹星\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"星月烙印\"]").exists:
                client.xpath("//*[@label=\"星月烙印\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"轻羽礼帽\"]").exists:
                client.xpath("//*[@label=\"轻羽礼帽\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"金月星芒\"]").exists:
                client.xpath("//*[@label=\"金月星芒\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"吉吉松鼠\"]").exists:
                client.xpath("//*[@label=\"吉吉松鼠\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"律动音符\"]").exists:
                client.xpath("//*[@label=\"律动音符\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            elif client.xpath("//*[@label=\"兔兔雪糕\"]").exists:
                client.xpath("//*[@label=\"兔兔雪糕\"]").click()
                client.xpath("//*[@label=\"送礼\"]").click()
            else:
                print("所有礼物不存在")
                break
        client.xpath("//*[@label=\"profile back icon\"]").click()
        client.xpath("//*[@label=\"profile back icon\"]").click()
    else:
        client.xpath("//*[@label=\"profile back icon\"]").click()
        print(username + " : 礼物ID不符合")


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
    time.sleep(3)
    client(label="超级玩家").click()
    time.sleep(5)
    client.click(0.566, 0.896)
    time.sleep(1)
    client.swipe(0.5, 0.8, 0.5, 0.5)
    time.sleep(3)
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
def process(client, username, password, loginType, isCheckDiamond, isGetSecurityPacket, appType, isInToRoom, openAJS):
    # 登录
    login(client, username, password, loginType, appType, openAJS)
    # 等待签到弹窗
    # if client(label="daily reward close", timeout=1.0).exists:
    #     client.click(0.6, 0.7)
    #     time.sleep(3)
    #     client(label="daily reward close").click()
    # 如果登录过期
    if client(label="确定", timeout=1.0).exists:
        client(label="确定").click()
        # 重新登录
        login(client, username, loginType, appType, openAJS)
    if isCheckDiamond == "true":
        getDiamond(client)
    if isGetSecurityPacket >= 1:
        # getSecurityPacket(client, isGetSecurityPacket, appType)
        openSuperPlayer(client)
    if isInToRoom == "true":
        intoRoom(client)
    # addFirend(client)
    # time.sleep(10)
    close(client, "true")


def processSendGift(client, username, password, loginType, sendUserId, sendType, sendName):
    # 登录
    login(client, username, password, loginType, "hello", "false")
    if client(label="daily reward close", timeout=1.0).exists:
        client.xpath(
            "//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[1]/Image[1]/Image[1]").click()
        time.sleep(3)
        client(label="daily reward close").click()
    # 如果登录过期
    if client(label="确定", timeout=1.0).exists:
        client(label="确定").click()
        # 重新登录
        login(client, username, loginType, "hello", "false")
    sendGift(client, username, sendUserId, sendType, sendName)
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


def doFromFile(uuid, key, fileName, appType, isCheckDiamond, isGetSecurityPacket, sleepTime, isInToRoom, openAJS):
    runCount = 0
    try:
        myclient = wda.USBClient(uuid, port=8100)
    except:
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " kill com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " launch com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        myclient = wda.USBClient(uuid, port=8100)
    init(myclient, appType, openAJS)
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
                print(line.split("----")[2])
                if "###" in line:
                    continue
                try:
                    process(myclient, line.split("----")[0], line.split("----")[1], line.split("----")[2],
                            isCheckDiamond, isGetSecurityPacket,
                            appType, isInToRoom, openAJS)
                except:
                    init(myclient, appType, openAJS)
                    try:
                        process(myclient, line.split("----")[0], line.split("----")[1], line.split("----")[2],
                                isCheckDiamond,
                                isGetSecurityPacket, appType, isInToRoom, openAJS)
                    except:
                        init(myclient, appType, openAJS)
                        process(myclient, line.split("----")[0], line.split("----")[1], line.split("----")[2],
                                isCheckDiamond,
                                isGetSecurityPacket,
                                appType, isInToRoom, openAJS)
            if sleepTime != 0:
                time.sleep(sleepTime)


def doFromFileSendGift(uuid, key, fileName, appType, sendUserId, sendType, sendName):
    runCount = 0
    try:
        myclient = wda.USBClient(uuid, port=8100)
    except:
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " kill com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        os.system(
            "/Users/jfx/Library/Python/3.9/bin/tidevice -u " + uuid + " launch com.facebook.WebDriverAgentLib.lizhengtest" + key + ".xctrunner")
        myclient = wda.USBClient(uuid, port=8100)
    init(myclient, appType)
    file_cm = codecs.open("../data/" + fileName + ".txt", 'r', "utf-8")
    for line in file_cm:
        print(line.split("----")[2])
        try:
            processSendGift(myclient, line.split("----")[0], line.split("----")[1], line.split("----")[2],
                            sendUserId, sendType, sendName)
        except:
            init(myclient, appType)
            try:
                processSendGift(myclient, line.split("----")[0], line.split("----")[1], line.split("----")[2],
                                sendUserId, sendType, sendName)
            except:
                init(myclient, appType)
                processSendGift(myclient, line.split("----")[0], line.split("----")[1], line.split("----")[2],
                                sendUserId, sendType, sendName)
