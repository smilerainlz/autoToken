import sys, wda
import time

sys.path.append("..//")
import hello

uuid = "08771801cd4ba47bd323204310a296c6e05e2b1a"
key = "0061"

client = wda.USBClient(uuid, port=8100)

client(label="消息").click()
if client(label="风").exists:
    client(label="风").click()
    client(label="马上前往").click()
    if client.xpath("//*[@label=\"网页对话框\"]/Other[9]/StaticText[1]").exists:
        client.xpath("//*[@label=\"网页对话框\"]/Other[9]/StaticText[1]").click()
        client(label="马上开通").click()
        client(label="订阅").click()
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
    time.sleep(1)
    client.click(0.06, 0.069)