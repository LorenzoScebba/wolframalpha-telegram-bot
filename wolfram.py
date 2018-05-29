import telepot
from telepot.loop import MessageLoop
from time import sleep
import wolframalpha

token = "000000000:XXXXXXXXXXXXXXXXXXXXXXXX-XXXXXXXXXX"
appID = "XXXXXX-XXXXXXXXXX"
chatID = 000000000

bot = telepot.Bot(token)
client = wolframalpha.Client(appID)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if not str(msg['text']).startswith("/"):
        if chat_id == chatID:
            text = msg['text']
            res = client.query(text)
            print(res)
            try:
                bot.sendMessage(chat_id, next(res.results).text)
            except AttributeError:
                bot.sendMessage(chat_id, "Not a valid query")
            except StopIteration:
                bot.sendMessage(chat_id, "Possible format error")
            except Exception:
                bot.sendMessage(chat_id, "An exception occurred :(")
    else:
        bot.sendMessage("Send me a query to start!")


MessageLoop(bot, handle).run_as_thread()
print("Running")

while 1:
    sleep(5)
