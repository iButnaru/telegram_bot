import json
import requests
import time
from Bot_SQLite_Database import DBStore

db = DBStore()

TOKEN = "673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_the_url(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")
    return content


def get_data_from_url(url):
    data = get_the_url(url)
    json_data = json.loads(data)
    return json_data


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    json_updates = get_data_from_url(url)
    return json_updates


def get_updated_id(updates):
    updated_id = []
    for update in updates["result"]:
        updated_id.append(update["update_id"])
    return max(updated_id)


def get_updated_chat_id_and_text(updates):
    number_upd = len(updates["result"])
    last_update = number_upd - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_the_url(url)


# def echo_all_messages(updates):
#     for update in updates["result"]:
#         try:
#             text = update["message"]["text"]
#             chat = update["message"]["chat"]["id"]
#             send_message(text, chat)
#         except Exception as e:
#             print(e)

def control_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            items = db.get_item()
            if text in items:
                db.delete_items(text)
                items = db.get_item()
            else:
                db.add_items(text)
                items = db.get_item()
            message = "\n".join(items)
            send_message(message, chat)
        except KeyError:
            print("errrorrr")


def main():
    db.create_table()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_updated_id(updates) + 1
        control_updates(updates)
    time.sleep(0.5)


if __name__ == "__main__":
    main()



