
import json
import requests


class Telegrambot():
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_url(self.url):
        req = requests.get(self.url)
        content = req.content.decode("utf8")
        return print(content)

    def get_json(self.url):
        contentt = get_url(url)
        url = json.loads(contentt)
        return url

    def get_updates():
        gt = self.url + "getUpdates"
        upd = get_json(gt)
        return upd