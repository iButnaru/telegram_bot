import requests
import json
import time


TOKEN = "673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg"
URL = "https://api.telegram.org/bot673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg/"

def get_url(url):
    req = requests.get(url)
    content = req.content.decode("utf8")
    return content


def get_json(url):
    url = json.loads(get_url(url))
    return url


def get_updates():
    gt = URL + "getUpdates"
    upd = get_json(gt)
    return upd

def get_chat_id(updates):
    num_updates = len(updates["result"])
    last_upd = num_updates - 1
    id = updates["result"][last_upd]["message"]["chat"]["id"]
    text = updates["result"][last_upd]["message"]["text"]
    return ("Id: " + str(id), "Text: " + str(text) )


print(get_url(URL))
print(get_json(URL))
print(get_updates())
print(get_chat_id(get_updates()))



