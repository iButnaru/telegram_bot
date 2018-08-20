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
    return json
