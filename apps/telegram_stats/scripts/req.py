import requests
from bs4 import BeautifulSoup

chat_link = 'https://t.me/rian_ru'


def get_chat_info(chat_link):
    url = chat_link
    r = requests.get(url=url).text
    soup = BeautifulSoup(r, 'lxml')
    image = soup.find("img", {"class": "tgme_page_photo_image"})['src']
    title = soup.find("span", {"dir": "auto"}).text
    subscribers = soup.find("div", {"class": "tgme_page_extra"}).text
    subscribers = int(subscribers.split(' ')[0] + subscribers.split(' ')[1] + subscribers.split(' ')[2])

    print('Ссылка на изображение', image)
    print('Название чата:', title)
    print('Количество подписчиков:', subscribers)

    return image, title

    #   todo handle with bot or group photo


get_chat_info(chat_link)
