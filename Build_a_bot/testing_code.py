# class My_car():
#     def __init__(self, wheels, kilometers, colour):
#         self.wheels = wheels
#         self.kilometers = kilometers
#         self.colour = colour
#     def __str__(self):
#         y = "The kilometers are" + str("{}").format(self.kilometers)
#         return y
#     # def __repr__(self):
#     #     x = self.colour + "this is the colour of the car!"
#     #     return x
#
# instancer = My_car(4, 1290, "black")
# # print(instancer)
# i = str(My_car)
# print(i)
#
#
# import datetime
#
# x = datetime.date.today()
# print(x)
# print(str(x))
# print(repr(x))
import json
import requests
import time


TOKEN = "673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg"
URL = "https://api.telegram.org/bot673246689:AAH3rY9DLgpnDc2V96MoG4jwFJZoPg2ecEg/"

# get_url = downloads the content from a URL and gives a string back
# .decode("utf8") = extra compatibility - necessary for some Python versions
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

#content = gives us the same result as above (get_url())
#json = we use it as a dictionary json.loads()
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

def get_chat_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

print (get_url(URL))
print (get_json_from_url(URL))
print (get_updates())
print (get_chat_id(get_updates()))
# print (get_last_chat_id_and_text(get_updates()))
text, id = get_chat_id(get_updates())
# send_message(text, id)

# def main():
#     last_textchat = (None, None)
#     while True:
#         text, chat = get_chat_id(get_updates())
#         if (text, chat) != last_textchat:
#             send_message(text, chat)
#             last_textchat = (text, chat)
#         time.sleep(0.5)
# main()