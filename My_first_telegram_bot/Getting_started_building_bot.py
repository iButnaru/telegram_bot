import json
import requests


TOKEN = "673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg"
URL = "https://api.telegram.org/bot673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg/"


def get_the_url(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")
    return content


def get_data_from_url(url):
    data = get_the_url(url)
    json_data = json.loads(data)
    return json_data


def get_updates():
    url = URL + "getUpdates"
    json_updates = get_data_from_url(url)
    return json_updates


def get_updated_chat_id_and_text(updates):
    number_upd = len(updates["result"])
    last_update = number_upd - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_the_url(url)


get_the_url(URL)
get_data_from_url(URL)
print(get_updates())
print(get_updated_chat_id_and_text(get_updates()))
text, chat_id = get_updated_chat_id_and_text(get_updates())
send_message(text, chat_id)