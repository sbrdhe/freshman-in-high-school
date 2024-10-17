import json
import requests
import time
import urllib

from random import *

TOKEN = "6696796795:AAF4LdOL8X_q29G0cO9EKNDXB0utDX_maIY"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

words = ["apple","banana","car"]
gamelist ={}

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def process_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            # print(gamelist) #for debuging
            if(text == "/hangman"):
                send_message("행맨 게임을 시작합니다. ", chat)
                word = choice(words)
                print("game started with", chat, "/ Q:", word)
                gamelist[chat] = [word, False]  # Q, A, Success?
            elif(text == "/stop"):
                send_message("게임을 중단합니다. ", chat)
                gamelist[chat] = []
            elif(text == "/start"):
                print("new user:", chat)
                send_message(
                    "반갑습니다. 행맨 봇입니다. 게임을 시작하기 원하시면 /hangman 명령을 입력하세요. 게임을 멈추고 싶을 때는 언제든 /stop 명령을 입력하면 됩니다. ", chat)
            elif(len(gamelist[chat]) > 1 and not gamelist[chat][1]):
                print(chat, "entered", text)
                succeed = True
                feedback = ""
                for w in gamelist[chat][0]:
                    if w in text:
                        feedback += w + " "
                    else:
                        feedback += "_ "
                        succeed = False
                gamelist[chat][1] = succeed
                send_message(feedback, chat)

                if succeed:
                    send_message("맞췄습니다!!!", chat)
                    print(chat, "finished a game")
                    gamelist[chat] = []
        except Exception as e:
            print(e)




def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            process_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()