import wda, codecs, time


def process(client, userId):
    if client(label="搜大神、搜房间、搜玩友").exists:
        client(label="搜大神、搜房间、搜玩友").click()
    client.send_keys(userId)
    time.sleep(2)
    client.click(0.67, 0.309)
    time.sleep(3)
    if client.xpath("//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[7]/Other[1]/Other[1]/Image[1]").exists:
        print("---------------- " + userId)
    else:
        print(userId)
    client(label="profile back icon").click()
    client.click(0.908, 0.093)


myclient = wda.USBClient("00008110-001A21803482401E", port=8100)
file = codecs.open("helloid.txt", 'r', "utf-8")
for line in file:
    process(myclient, line)
file.close()
