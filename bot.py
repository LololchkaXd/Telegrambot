import telebot
import wakeonlan
import os
import sys
from subprocess import Popen
from telebot import types
import random

from telebot import types
bot = telebot.TeleBot('1604438883:AAH2VWSNPNuE041Lz_lDiTIGYE8A5W-8xe0')


@bot.message_handler(commands=['help', 'wake'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я codex_bot!')


@bot.message_handler(commands=['setatus', 'item2'])
def run_block(run):
    p = Popen('/home/nazar/wlan/autologinbot/test.py')
    #msg = bot.send_message(run.chat.id, '')
    
            

@bot.message_handler(commands=['run', 'item1'])
def read_blocked(wake):
    b = Popen('/home/nazar/wlan/autologinbot/wake-on-lan.py')
    bot.send_message(wake.chat.id, 'Сервер запущен',reply_markup=markup)


@bot.message_handler(commands=['start'])
def welcome(message):
   
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Запустити сервер")

 
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def server(message):
    if message.chat.type == 'private':
        if message.text == 'Запустити сервер':
            p = Popen('/home/nazar/wlan/autologinbot/wake-on-lan.py')
            bot.send_message(message.chat.id,"Сервер Запущено.3хв Очікування.")
    

  

if __name__ == "__main__":
    bot.polling()

