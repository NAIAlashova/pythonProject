import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import info

token = ""
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands='start')
def start(messege):
    bot.send_message(messege.chat.id, 'Привет. Это бот-квест. Ты будешь проходить локации и в зависимости от твоего выбора будет определяться победа')
    bot.send_message(messege.chat.id, 'Нужна будет помощь, напиши /help')
    bot.send_message(messege.chat.id, 'А сейчас поехали /kvest')

s = 0
markup0 = ReplyKeyboardMarkup(resize_keyboard=True)
markup0.add(KeyboardButton(info[s]['Кнопки'][0]))
markup0.add(KeyboardButton(info[s]['Кнопки'][1]))
@bot.message_handler(commands='kvest')
def kvest(messege):
    bot.send_message(messege.chat.id,info[s]['Описание'], markup=markup0)
    bot.send_photo('lok 1.png')
    bot.register_next_step_handler(v1)

markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
markup1.add(KeyboardButton(info[s]['Ответы']['Кнопки'][0]))
markup1.add(KeyboardButton(info[s]['Ответы']['Кнопки'][1]))
markup1.add(KeyboardButton(info[s]['Ответы']['Кнопки'][2]))
def v1(messege):
    if messege == info[s]['Кнопки'][0]:
        bot.register_next_step_handler(text=info[s]['Ответы'][1]['Описание'], v2, markup=markup1)
    else:
        bot.send_message(info[s]['Ответы'][2])

markup2 = ReplyKeyboardMarkup(resize_keyboard=True)
markup2.add(KeyboardButton(info[s]['Кнопки'][0]))
markup2.add(KeyboardButton(info[s]['Кнопки'][1]))
markup3 = ReplyKeyboardMarkup(resize_keyboard=True)
markup3.add(KeyboardButton(info[s]['Кнопки'][0]))
markup3.add(KeyboardButton(info[s]['Кнопки'][1]))
def v2(messege):
    global s
    if messege == info[s]['Ответы']['Кнопки'][0]:
        s = 1
        bot.send_photo('lok 2.1.png')
        bot.send_messege(text=info[s])
    elif messege == info[s]['Ответы']['Кнопки'][1]:
        s = 2
        bot.send_photo('lok 2.3.png')
        bot.register_next_step_handler(text=info[s]['Описание'], markup=markup2)
    else:
        s = 3
        bot.send_photo('lok 2.2.png')
        bot.register_next_step_handler(text=info[s]['Описание'], markup=markup3)

def right2():
    global s
    a = False
    if s == 2 :
        a = True
    return a
@bot.message_handler(['text'], func=right2())
def lok2(message):
    if message == info[s]['Кнопки'][0]:
        bot.send_message(message.chat.id, info[s]['Ответы'][0])
    else:
        bot.send_message(message.chat.id, info[s]['Ответы'][1])
def right3():
    global s
    a = False
    if s == 3:
        a = True
    return a
@bot.message_handler(['text'], func=right3())
def lok3(message):
    if message == info[s]['Кнопки'][0]:
        bot.send_photo('lok 3.1.png')
        bot.send_message(message.chat.id, info['3.1']['Ответы'][0])
    else:
        bot.send_photo('lok 3.2.png')
        bot.send_message(message.chat.id, info['3.2']['Ответы'][1])

bot.polling()
