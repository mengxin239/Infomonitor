from pyrogram import Client, filters
import string
import requests
import logging

logging.basicConfig(level=logging.INFO)

token="5164532764:AAGtpKzNTPkct6vC2E7sgzOb8ojFtO8FuWE"
chat_id=-1001674853973
keyword="Telegram,入侵,网络,病毒,漏洞,TG,异常,VPS,服务器"
lastword = []


app = Client("MonitorBot")

@app.on_message(filters.text & filters.channel)
def findword(client, message):
    global lastword
    word=[]
    haveword = False
    for i in range(0,len(keyword.split(','))):
        text=message.text
        logging.info(f"关注的频道{message.sender_chat.title}更新，正在查找有无关键词")
        if text.find(keyword.split(',')[i]) != -1:
            if haveword == False:
                haveword = True
            word.append(keyword.split(',')[i])
            nowword=keyword.split(',')[i]
            logging.info(f"包括 {nowword}",)
        else:
            nowword=keyword.split(',')[i]
            logging.info(f"不包括 {nowword}",)
    lastword.sort()
    word.sort()
    if haveword == True and lastword != word:
        send(f"来自 *{message.sender_chat.title}* \r\n" + message.text + "\r\n本消息由Bot自动发送")
    lastword=[]
    for i in range(0,len(word)):
        lastword.append(word[i])
    print(word)
    print(lastword)


def send(message):
    url=r"https://api.telegram.org/bot"+token+"/sendMessage"
    data={}
    data["text"]=message
    data["chat_id"]=chat_id
    logging.debug(f"请求参数:{data}")
    response=requests.post(url=url,data=data)
    logging.debug(f"返回数据:{response.text}")
    logging.info("转发到Channel成功")

app.run()