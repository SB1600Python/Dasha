import random
import telebot


token = '6060836398:AAF2QTJ0HYWkwQMTy_MlqCkBK2YVdwQhBTU'
bot = telebot.TeleBot(token)
num = random.randint(1, 100)

@bot.message_handler(commands=['start'])
def start(message):
    global num
    num = random.randint(1, 100)
    bot.send_message(message.from_user.id, text='Вгадай число від 16 100')

@bot.message_handler(content_types=['text'])
def check_num(message):
    res = int(message.text)
    if res > num:
        text = 'Ваше число більше'
    elif res < num:
        text = 'Ваше число менше'
    elif res == num:
        text = 'Ви вийграли'
    bot.send_message(message.from_user.id, text=text)

bot.polling(none_stop=True, interval=0)