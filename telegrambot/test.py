import telebot
import time

bot = telebot.TeleBot('1270117170:AAHQISiBZbvc_Or72SVkBX38X4gdjkd-ypY')


@bot.message_handler(content_types=['text'])
def send_text(message):
    while True:
        bot.send_message(message.chat.id, 'tetetet')
        time.sleep(5)


if __name__ == '__main__':
    bot.polling(none_stop=True)
