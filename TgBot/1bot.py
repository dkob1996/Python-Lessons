import telebot
import random
import json
token = ''

bot = telebot.TeleBot(token)

number = 0


with open('TgBot/horoscope.json', 'r', encoding='utf-8') as horo:
   some_dict = json.load(horo)
   print(some_dict)


@bot.message_handler(commands=['start'])
def welcome(message):
   markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)


   item1 = telebot.types.KeyboardButton('Рандомное число')
   item2 = telebot.types.KeyboardButton('Кинуть кость')
   item3 = telebot.types.KeyboardButton('Как дела?')
   item4 = telebot.types.KeyboardButton('Напоминалка')
   item5 = telebot.types.KeyboardButton('Загадай число')
   item6 = telebot.types.KeyboardButton('Знак зодиака')
   item7 = telebot.types.KeyboardButton('Покажи id стикера')


   markup.add(item1, item2, item3, item4, item5, item6, item7)


   bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)




@bot.message_handler(content_types=['text'])
def answer(message):
   if message.text.lower() == 'отлично':
       bot.send_message(message.chat.id, 'Я рад за тебя')
   elif message.text.lower() == 'плохо':
       bot.send_message(message.chat.id, 'Что случилось?')
   elif message.text.lower() == 'знак зодиака':
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
       markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
       bot.send_message(message.chat.id, 'Жмакни на кнопку', reply_markup=markup)
       bot.register_next_step_handler(message, horoscope)


   elif message.text.lower() == 'загадай число':
       global number
       number = random.randint(1, 10)
       bot.send_message(message.chat.id, 'Ок, загадал')
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
       bot.send_message(message.chat.id, 'Введите время для будильника')
       bot.register_next_step_handler(message, alarm)
   else:
       bot.send_message(message.chat.id, 'Я пока не умею отвечать на данное сообщение!')


def alarm(message):
   bot.send_message(message.chat.id, 'Включил напоминалку')
#     global time
#     time = message
#     global chat_id
#     chat_id = message.chat.id
#
# bot.send_message(chat_id)
@bot.message_handler(content_types=['text'])
def think_of(message):
   # print(number)
   # number = 5  # random.randint(0, 100)
   if message.text.lower() != f'{number}':
       bot.send_message(message.chat.id, 'nope')
       bot.register_next_step_handler(message, think_of)
   else:
       bot.send_message(message.chat.id, 'yep!')


@bot.message_handler(content_types=['text'])
def horoscope(message):
   markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
   item13 = telebot.types.KeyboardButton('ХвАтить!')
   markup.add(item13)
   if message.text != 'ХвАтить!':
       bot.send_message(message.chat.id, some_dict[message.text], reply_markup=markup)
       bot.register_next_step_handler(message, horoscope)






bot.polling(none_stop=True)
