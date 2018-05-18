import telepot
import requests
from telepot.loop import MessageLoop
from time import sleep
from xml.dom import minidom



token = ""
appID = ""
chatID =

plus = "%2B"
divide = "%2F"


bot = telepot.Bot(token)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if(chat_id == chatID):
        text = msg['text']

        text = str(text).replace("+", plus)
        text = str(text).replace("/", divide)

        response = requests.get("http://api.wolframalpha.com/v2/query?appid=" + str(appID) + "&input=" + text)
        response = minidom.parseString(response.text)
        result = response.getElementsByTagName("plaintext")
        result = (result[1].firstChild.nodeValue)
        print(str(chat_id) + ";" + str(result))
        bot.sendMessage(chat_id, str(result))
    else:
        bot.sendMessage(chat_id,"Create your own WolframAlpha bot : https://github.com/LorenzoScebba/wolframalpha-telegram-bot")

MessageLoop(bot,handle).run_as_thread()

while 1:
    sleep(5)