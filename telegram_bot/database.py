import sqlite3 as sql
from sqlite3 import Error
from config import db


def create_connection():
    connection = None
    try:
        connection = sql.connect(db)
    except Error as e:
        print(e)
    return connection


DB_CONNECTION = None
CURSOR = None


def connect():
    global DB_CONNECTION, CURSOR
    DB_CONNECTION = create_connection()
    CURSOR = DB_CONNECTION.cursor()


connect()


GET_ALL_USERS = 'SELECT * FROM auth_user'
GET_ALL_POSTS = 'SELECT * FROM home_post'
GET_ALL_CHATS = 'SELECT * FROM home_chat'
GET_ALL_BOTS = 'SELECT * FROM home_bot'
GET_ALL_SCHEDULE = 'SELECT * FROM home_postschedule'
GET_ALL_TEMPLATES = 'SELECT * FROM home_template'

GET_SCH_BY_USER_ID_NOT_SENT = 'SELECT schedule, post_id, user_id, id FROM home_postschedule WHERE user_id=? and is_sent=?'
GET_CHAT_BY_USER_ID = 'SELECT ref FROM home_chat WHERE user_id=?'
GET_POST_BY_ID = 'SELECT text, photo_1, photo_2, photo_3 ,photo_4, photo_5, url, url_text, video, btn_name_1, btn_name_2, btn_name_3, btn_name_4, template_id FROM home_post WHERE id=?'
GET_BOT_BY_USER_ID = 'SELECT * FROM home_bot WHERE user_id=?'
GET_TEMPLATE_BY_ID = 'SELECT * FROM home_template WHERE id=?'

UPDATE_SCHED_SET_SENT = 'UPDATE home_postschedule SET is_sent=? WHERE id=?'


def get_all(connection, query, *args):
    with connection as con:
        cursor = con.cursor()
        data = cursor.execute(query).fetchall()
    # print(data)
    return data


def get_by_id(connection, query, value):
    with connection as con:
        cursor = con.cursor()
        data = cursor.execute(query, value).fetchall()
    # print(data)
    return data


def update(connection, query, value):
    with connection as con:
        cursor = con.cursor()
        cursor.execute(query, value)
        con.commit()
    return True


# get_all(DB_CONNECTION, GET_ALL_USERS)
# get_all(DB_CONNECTION, GET_ALL_POSTS)
# get_all(DB_CONNECTION, GET_ALL_CHATS)
# get_all(DB_CONNECTION, GET_ALL_BOTS)
# get_all(DB_CONNECTION, GET_ALL_SCHEDULE)
#
# get_by_id(DB_CONNECTION, GET_SCH_BY_USER_ID_NOT_SENT, (1, False))
# get_by_id(DB_CONNECTION, GET_CHAT_BY_USER_ID, (1,))
# get_by_id(DB_CONNECTION, GET_BOT_BY_USER_ID, (1,))
# get_by_id(DB_CONNECTION, GET_POST_BY_ID, (1,))
# get_by_id(DB_CONNECTION, GET_TEMPLATE_BY_ID, (1,))

# update(DB_CONNECTION, UPDATE_SCHED_SET_SENT, (9, 1))
# template = get_by_id(DB_CONNECTION, GET_TEMPLATE_BY_ID, (5,))[0][3]
# print(template)