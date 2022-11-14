import requests
from bs4 import BeautifulSoup

chat_link = 'https://t.me/jgirwaojoaeweowjbot'


import requests
from bs4 import BeautifulSoup


def get_chat_info(chat_link):
    try:
        url = chat_link
        r = requests.get(url=url).text
        soup = BeautifulSoup(r, 'lxml')
        image = soup.find("img", {"class": "tgme_page_photo_image"})['src']
        title = soup.find("span", {"dir": "auto"}).text
        raw_subscribers = soup.find("div", {"class": "tgme_page_extra"}).text
        subscribers = ''
        for i in raw_subscribers.split(' '):
            if 'sub' not in i:
                subscribers += i
        subscribers = int(subscribers)
    except:
        image = ''
        title = ''
        subscribers = 0
    return image, title, subscribers


def get_bot_info(chat_link):
    try:
        url = chat_link
        r = requests.get(url=url).text
        soup = BeautifulSoup(r, 'lxml')
        title = soup.find("span", {"dir": "auto"}).text
    except:
        title = ''
    return title


get_bot_info(chat_link)
