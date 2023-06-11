import random
import telebot
from telebot import types

user_turn = 0
bot_turn = 0
sweets = 55
max_sweet = 28
bot = telebot.TeleBot("6008483140:AAFuonJrP99jG570ro4H4WtkazxmIUH79rs")
flag = None

@bot.message_handler(commands=['start'])# вызов функции по команде в списке
def start(message):
    global sweets,flag
    bot.send_message(message.chat.id,f"Приветствую вас в игре!")
    flag = random.choice(["user","bot"])
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет")
    if flag == "user":
        bot.send_message(message.chat.id,f"Первым ходите вы")# отправка сообщения (кому отправляем, что отправляем(str))
        controller(message)
    else:
        bot.send_message(message.chat.id,f"Первым ходит бот")# отправка сообщения (кому отправляем, что отправляем(str))
        controller(message)

def controller(message):
    global flag,sweets
    if sweets>0:
        if flag == "user":
            bot.send_message(message.chat.id,f"Ваш ход введите кол-во конфет от 0 до {max_sweet}")
            bot.register_next_step_handler(message,user_input)
            print(1)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id,f"Победил {flag}!")


def bot_input(message):
    global sweets,flag,bot_turn
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global user_sweets,sweets,flag
    user_sweets = int(message.text)
    sweets = sweets - user_sweets
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()

# #скачиваем библиотеку pip install pytelegrambotapi
# import telebot
# from telebot import types
# user_sweets = 0
# #bot = telebot.TeleBot("5782756209:AAG-Rzx3ieL-JGwzHm5kGucQGT3TZ6nBhUw")
# @bot.message_handler(commands = ['start'])#вызов функции по команде в списке
# def start(message):
#     bot.send_message(message.chat.id,f"/button")#отправка сообщения (кому отправляем, что отправляем(str))
#     print(user_sweets)
# def summa(message):
#     summ = sum(list(map(int,message.text.split())))
#     bot.send_message(message.chat.id, str(summ))
#     button(message)
# @bot.message_handler(commands=["button"])
# def button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)#создание клавиатуры
#     but1 = types.KeyboardButton("сумма")#создание кнопок
#     but2 = types.KeyboardButton("разность")
#     markup.add(but1)#добавление кнопок
#     markup.add(but2)#добавление кнопок
#     bot.send_message(message.chat.id,"Выбери ниже", reply_markup=markup)
# @bot.message_handler(content_types=["text"])#вызов функции если тип сообщения - текст
# def controller(message):
#     if message.text == "сумма":
#         bot.send_message(message.chat.id,"введи два числа для суммы")
#         bot.register_next_step_handler(message, summa)  # вызов функции на ответ пользователя
#     elif message.text == "разность":
#         pass
# bot.infinity_polling()