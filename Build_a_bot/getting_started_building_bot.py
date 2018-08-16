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

def get_updates():
    url = URL + "getUpdates"
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

#sendMessage?text={}&chat_id={}"
#
# print(get_url(URL))
# print(get_json_from_url(URL))
# print(get_updates())
# print(get_chat_id(get_updates()))
# text, chat_id = get_chat_id(get_updates())
# send_message(text, chat_id)

def main():
    last_text = (None, None)
    while True:

        text, chat_id = get_chat_id(get_updates())
        if (text, chat_id) != last_text:
            send_message(text, chat_id)
            last_text = (text, chat_id)

if __name__=="__main__":
    main()

