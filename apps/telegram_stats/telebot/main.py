from telebot import TeleBot
from config import token, chat


bot = TeleBot(token)


print('bot.get_chat()', bot.get_chat(chat))

print('bot.get_chat_members_count()', bot.get_chat_members_count(chat))

print('bot.get_chat_administrators()', bot.get_chat_administrators(chat))

# print(bot.get_chat_menu_button(chat_id=chat))

print('', bot.get_updates())
