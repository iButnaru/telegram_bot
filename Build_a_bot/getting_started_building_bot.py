import json
import requests
import time

TOKEN = "673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg"
URL = "https://api.telegram.org/bot673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg/"

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

def get_chat_id(updates):
    num_updates = len(updates["result"])
    last_upd = num_updates - 1
    text = updates["result"][last_upd]["message"]["text"]
    chat_id = updates["result"][last_upd]["message"]["chat"]["id"]
    return (text, chat_id )

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_last_update_id(updates):
    get_last = []
    for upd in updates["result"]:
        get_last.append(upd["update_id"])
    print(get_last)
    return max(get_last)

def echo_all_messages(updates):
    try:
        for updt in updates["result"]:
            text = updt["message"]["text"]
            chat_id = updt["message"]["chat"]["id"]
            send_message(text,chat_id)
    except Exception as e:
        print(e)



def main():
    last_text = (None, None)
    while True:
        text, chat_id = get_chat_id(get_updates())
        if (text, chat_id) != last_text:
            send_message(text, chat_id)
            last_text = (text, chat_id)

        time.sleep(0.5)


if __name__=="__main__":
    main()


print(echo_all_messages(get_updates()))
