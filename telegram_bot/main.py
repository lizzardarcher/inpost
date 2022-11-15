from telebot.async_telebot import AsyncTeleBot
from telebot import TeleBot
from database import (get_all,
                      get_by_id,
                      DB_CONNECTION,
                      GET_ALL_USERS,
                      GET_SCH_BY_USER_ID_NOT_SENT,
                      GET_CHAT_BY_USER_ID,
                      GET_BOT_BY_USER_ID,
                      GET_POST_BY_ID,
                      GET_TEMPLATE_BY_ID,
                      UPDATE_SCHED_SET_SENT,
                      update)
from config import token
from datetime import datetime
from time import sleep


def auto_post():

    # получить всех юзеров
    users = get_all(DB_CONNECTION, GET_ALL_USERS)
    for user in users:
        user_id = user[0]
        # print(user)

        # цикл - получить расписание неотправленных постов с каждым юзером
        schedule = get_by_id(DB_CONNECTION, GET_SCH_BY_USER_ID_NOT_SENT, (user_id, False))
        for sched in schedule:
            sched_datetime = datetime.strptime(sched[0], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M')
            post_id = sched[1]
            sched_id = sched[3]
            datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M')
            # print(sched)

            # Проверка по дате-времени, если совпадает, то continue
            if datetime_now == sched_datetime:
                print('OK!')

                # цикл - по чатам с user_id
                chats = get_by_id(DB_CONNECTION, GET_CHAT_BY_USER_ID, (user_id,))
                for chat in chats:
                    chat_username = chat[0].split('/')[-1]
                    print(chat_username)

                    # Цикл по ботам с user_id
                    bots = get_by_id(DB_CONNECTION, GET_BOT_BY_USER_ID, (user_id,))
                    for bot in bots:
                        bot_token = bot[0]

                        # цикл по постам c user_id
                        post = get_by_id(DB_CONNECTION, GET_POST_BY_ID, (post_id,))[0]
                        print(post)
                        text = post[0]
                        template_id = post[13]
                        template = get_by_id(DB_CONNECTION, GET_TEMPLATE_BY_ID, (template_id,))
                        photo_1 = post[1]
                        photo_2 = post[2]
                        photo_3 = post[3]
                        photo_4 = post[4]
                        photo_5 = post[5]
                        url_btn = (post[6], post[7])
                        video = post[8]
                        btn_1 = post[9]
                        btn_2 = post[10]
                        btn_3 = post[11]
                        btn_4 = post[12]

                        # Отправить сообщение
                        bot = TeleBot(bot_token)
                        bot.send_message(chat_id='@'+chat_username, text=text)
                        print('Message sent')
                        update(DB_CONNECTION, UPDATE_SCHED_SET_SENT, (True, sched_id))


while True:
    auto_post()
    sleep(1)