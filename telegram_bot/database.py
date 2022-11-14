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


GET_ALL_POSTS = 'SELECT * FROM home_post'
GET_ALL_CHATS = 'SELECT * FROM home_chat'
GET_ALL_BOTS = 'SELECT * FROM home_bot'
GET_ALL_SCHEDULE = 'SELECT * FROM home_postschedule'


def get_all(connection, query):
    with connection as con:
        cursor = con.cursor()
        data = cursor.execute(query).fetchall()
    print(data)
    return data


get_all(DB_CONNECTION, GET_ALL_POSTS)
get_all(DB_CONNECTION, GET_ALL_CHATS)
get_all(DB_CONNECTION, GET_ALL_BOTS)
get_all(DB_CONNECTION, GET_ALL_SCHEDULE)
