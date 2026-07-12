import random
import webbrowser as wb


class Url:
    def __init__(self, url):
        self.url = url
        self.token = random.random()

    def open(self):
        if self.url[0] == '/':
            self.url = 'https://www.luogu.com.cn'+self.url
        wb.open(self.url)
