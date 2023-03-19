import telebot
import random
import json
import math
import os
import re
import sys
import datetime
import threading
token = ''

bot = telebot.TeleBot(token)

number = 0

with open('TgBot/horoscope.json', 'r', encoding='utf-8') as horo:
   some_dict = json.load(horo)

@bot.message_handler(commands=['start'])
def welcome(message):
   markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

   item1 = telebot.types.KeyboardButton('Рандомное число')
   item2 = telebot.types.KeyboardButton('Кинуть кость')
   item3 = telebot.types.KeyboardButton('Как дела?')
   item4 = telebot.types.KeyboardButton('Напоминалка')
   item5 = telebot.types.KeyboardButton('Загадай число')
   item6 = telebot.types.KeyboardButton('Знак зодиака')
   item7 = telebot.types.KeyboardButton('Математические задачки')
   item8 = telebot.types.KeyboardButton('Вычислить стоимость продукта')

   markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

   bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
   if message.text.lower() == 'отлично':
       bot.send_message(message.chat.id, 'Я рад за тебя')
   elif message.text.lower() == 'плохо':
       bot.send_message(message.chat.id, 'Что случилось?')
   elif message.text.lower() == 'знак зодиака':
       markup = telebot.types.ReplyKeyboardMarkup(row_width = 4)
       item1 = telebot.types.KeyboardButton('Овен')
       item2 = telebot.types.KeyboardButton('Телец')
       item3 = telebot.types.KeyboardButton('Близнецы')
       item4 = telebot.types.KeyboardButton('Рак')
       item5 = telebot.types.KeyboardButton('Лев')
       item6 = telebot.types.KeyboardButton('Козерог')
       item7 = telebot.types.KeyboardButton('Весы')
       item8 = telebot.types.KeyboardButton('Скорпион')
       item9 = telebot.types.KeyboardButton('Водолей')
       item10 = telebot.types.KeyboardButton('Стрелец')
       item11 = telebot.types.KeyboardButton('Дева')
       item12 = telebot.types.KeyboardButton('Рыбы')
       item13 = telebot.types.KeyboardButton('Назад')
       markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
       bot.send_message(message.chat.id, 'Жмакни на кнопку', reply_markup=markup)
       bot.register_next_step_handler(message, horoscope)


   elif message.text.lower() == 'загадай число':
       global number
       number = random.randint(1, 10)
       bot.send_message(message.chat.id, 'Ок, загадал')
       bot.send_message(message.chat.id, 'Введи число, которое думаешь что я загадал!')
       bot.register_next_step_handler(message, think_of)


   elif message.text.lower() == 'как дела?':
       some_list = ['Good', 'Bad', 'Awful', 'Great', 'Awesome', 'Пока не родила']
       n = random.randint(0, len(some_list))
       bot.send_message(message.chat.id, some_list[n])
   elif message.text.lower() == 'рандомное число':
       bot.send_message(message.chat.id, str(random.randint(1, 100)))
   elif message.text.lower() == 'кинуть кость':
       bot.send_message(message.chat.id, str(random.randint(1, 7)))
   elif message.text.lower() == 'напоминалка':
       bot.send_message(message.chat.id, 'Введите название напоминания:')
       bot.register_next_step_handler(message, set_reminder_name)
   elif message.text.lower() == 'математические задачки':
       markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
       item1 = telebot.types.KeyboardButton('Вычеслить факториал')
       item2 = telebot.types.KeyboardButton('Вычеслить число Фиббоначчи')
       item3 = telebot.types.KeyboardButton('Назад')
       markup.add(item1, item2, item3)
       bot.send_message(message.chat.id, 'Жмакни на кнопку', reply_markup=markup)
       bot.register_next_step_handler(message, mathsolving)       
   elif message.text.lower() == 'вычислить стоимость продукта':
       bot.send_message(message.chat.id, 'Введите данные в формате: Цена, процент чаевых, процент налога: 12.00,20,8')
       bot.register_next_step_handler(message, solve_meal_input)
   else:
       bot.send_message(message.chat.id, 'Ориентируйтесь по предложенной клавиатуре и указаниям в чате')


@bot.message_handler(content_types=['text'])
def solve_meal_input(message):
    tmp = message.text.lower().split(',')
    if tmp[0].isnumeric() == True and tmp[1].isnumeric() == True and tmp[2].isnumeric() == True :
       
       meal_cost = float(tmp[0])
       tip_percent = int(tmp[1])
       tax_percent = int(tmp[2])

       tip = float((meal_cost/100)*tip_percent)
       tax = float((tax_percent/100)*meal_cost)
       total_cost = meal_cost+tip+tax

       bot.send_message(message.chat.id, round(total_cost))
       bot.send_message(message.chat.id, 'Операция вычисления стоимости покупки завершена')
    else:
        bot.send_message(message.chat.id, 'Введите только числа >= 0')
        bot.send_message(message.chat.id, 'Продолжите вводить здесь')
        bot.register_next_step_handler(message, solve_meal_input) 


@bot.message_handler(content_types=['text'])
def set_reminder_name(message):
   user_data = {}
   user_data[message.chat.id] = {'reminder_name': message.text}
   bot.send_message(message.chat.id, 'Введите дату и время, когда вы хотите получить напоминание в формате ГГГГ-ММ-ДД чч:мм:сс.')
   bot.register_next_step_handler(message, reminder_set, user_data)

def reminder_set(message, user_data):
   try:
      reminder_time = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')
      now = datetime.datetime.now()
      delta = reminder_time - now
      if delta.total_seconds() <= 0:
         bot.send_message(message.chat.id, 'Вы ввели прошедшую дату, попробуйте еще раз.')
      else:
         reminder_name = user_data[message.chat.id]['reminder_name']
         bot.send_message(message.chat.id, 'Напоминание "{}" установлено на {}.'.format(reminder_name, reminder_time))
         reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [message.chat.id, reminder_name])
         reminder_timer.start()
   except ValueError:
      bot.send_message(message.chat.id, 'Вы ввели неверный формат даты и времени, попробуйте еще раз.')

def send_reminder(chat_id, reminder_name):
   bot.send_message(chat_id, 'Время получить ваше напоминание "{}"!'.format(reminder_name))

@bot.message_handler(content_types=['text'])
def think_of(message):
   if message.text.lower() != f'{number}':
       bot.send_message(message.chat.id, 'nope')
       bot.register_next_step_handler(message, think_of)
   else:
       bot.send_message(message.chat.id, 'yep!')

@bot.message_handler(content_types=['text'])
def horoscope(message):
   markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
   item1 = telebot.types.KeyboardButton('Овен')
   item2 = telebot.types.KeyboardButton('Телец')
   item3 = telebot.types.KeyboardButton('Близнецы')
   item4 = telebot.types.KeyboardButton('Рак')
   item5 = telebot.types.KeyboardButton('Лев')
   item6 = telebot.types.KeyboardButton('Козерог')
   item7 = telebot.types.KeyboardButton('Весы')
   item8 = telebot.types.KeyboardButton('Скорпион')
   item9 = telebot.types.KeyboardButton('Водолей')
   item10 = telebot.types.KeyboardButton('Стрелец')
   item11 = telebot.types.KeyboardButton('Дева')
   item12 = telebot.types.KeyboardButton('Рыбы')
   item13 = telebot.types.KeyboardButton('Назад')
   markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13)
   if message.text != 'Назад':
       bot.send_message(message.chat.id, some_dict[message.text], reply_markup=markup)
       bot.register_next_step_handler(message, horoscope)
   elif message.text == 'Назад':
       markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
       item1 = telebot.types.KeyboardButton('Рандомное число')
       item2 = telebot.types.KeyboardButton('Кинуть кость')
       item3 = telebot.types.KeyboardButton('Как дела?')
       item4 = telebot.types.KeyboardButton('Напоминалка')
       item5 = telebot.types.KeyboardButton('Загадай число')
       item6 = telebot.types.KeyboardButton('Знак зодиака')
       item7 = telebot.types.KeyboardButton('Математические задачки')
       item8 = telebot.types.KeyboardButton('Вычислить стоимость продукта')
       markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
       bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mathsolving(message):
   markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
   item1 = telebot.types.KeyboardButton('Вычеслить факториал')
   item2 = telebot.types.KeyboardButton('Вычеслить число Фиббоначчи')
   item3 = telebot.types.KeyboardButton('Назад')
   markup.add(item1, item2, item3)
   if message.text == 'Вычеслить факториал':
      bot.send_message(message.chat.id, 'Введите число N, факториал которого хотите узнать')
      bot.send_message(message.chat.id, 'Число должно быть >0')
      bot.register_next_step_handler(message, factoral)
   elif message.text == 'Вычеслить число Фиббоначчи':
      bot.send_message(message.chat.id, 'Введите номер числа Фибоначчи, значение которого хотите узнать')
      bot.send_message(message.chat.id, 'Число должно быть >0')
      bot.register_next_step_handler(message, fibb)
   elif message.text == 'Назад':
       markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
       item1 = telebot.types.KeyboardButton('Рандомное число')
       item2 = telebot.types.KeyboardButton('Кинуть кость')
       item3 = telebot.types.KeyboardButton('Как дела?')
       item4 = telebot.types.KeyboardButton('Напоминалка')
       item5 = telebot.types.KeyboardButton('Загадай число')
       item6 = telebot.types.KeyboardButton('Знак зодиака')
       item7 = telebot.types.KeyboardButton('Математические задачки')
       item8 = telebot.types.KeyboardButton('Вычислить стоимость продукта')
       markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
       bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)
   elif message.text != 'Вычеслить факториал' or 'Вычеслить число Фиббоначчи' or 'Назад':
      bot.send_message(message.chat.id, 'Сначала выберете на клавиатуре то, что хотите')
      bot.register_next_step_handler(message, mathsolving)
@bot.message_handler(content_types=['text'])
def factoral(message):
   a = message.text.lower()
   if a.isnumeric() == True:
      n = int(a)
      fact = 1
      while n > 0:
         fact *=  n
         n -= 1
      bot.send_message(message.chat.id, fact)
      bot.register_next_step_handler(message, mathsolving)
      bot.send_message(message.chat.id, 'Операция вычисления Факториала завершена')
   else:
      bot.send_message(message.chat.id, 'Введите только числа >= 0')
      bot.send_message(message.chat.id, 'Продолжите вводить здесь')
      bot.register_next_step_handler(message, factoral)      

@bot.message_handler(content_types=['text'])
def fibb(message):
   fib1 = 1
   fib2 = 1
   a = message.text.lower()

   if a.isnumeric() == True:
      n = int(a)
      i = 0
      while i < n - 2:
         fib_sum = fib1 + fib2
         fib1 = fib2
         fib2 = fib_sum
         i = i + 1
      bot.send_message(message.chat.id, fib2)
      bot.register_next_step_handler(message, mathsolving)
      bot.send_message(message.chat.id, 'Операция вычисления числа Фибоначчи завершена')
   else:
      bot.send_message(message.chat.id, 'Введите только числа >= 0')
      bot.send_message(message.chat.id, 'Продолжите вводить здесь')
      bot.register_next_step_handler(message, fibb)

bot.polling(none_stop=True)
