import json
import requests
import time


TOKEN = "673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg"
URL = "https://api.telegram.org/bot673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg/"

#get_url = downloads the content from a URL and gives a string back
#.decode("utf8") = extra compatibility - necessary for some Python versions
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

#content = gives us the same result as above (get_url())
#json = we use it in order to use it as a dictionary json.loads()
#loads = short for Load String
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

#calls an API command and retrives a list of "updates"
def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    print("Numarul 1: " + str(num_updates))
    print("Numarul 2: " + str(last_update))
    print(text)
    print(chat_id)
    return (text, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

# print (get_url(URL))
# print (get_json_from_url(URL))
# print (get_updates())
# print (get_last_chat_id_and_text(get_updates()))
print (get_last_chat_id_and_text(get_updates()))




