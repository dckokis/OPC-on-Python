import telebot
import config
import random

from telebot import types


def main():
    bot = telebot.TeleBot(config.TOKEN)

    @bot.message_handler(commands=['start'])
    def welcome(message):
        sti = open('static/welcome.webp', 'rb')

        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("😊 Как дела?")
        item2 = types.KeyboardButton("Хочешь узнать погоду?")

        markup.add(item1, item2)

        bot.send_message(message.chat.id,
                         "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы добавить смысла жизни создателю.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.chat.type == 'private':
            if message.text == 'Хочешь узнать погоду?':
                bot.send_message(message.chat.id, str(random.randint(0, 100)))
            elif message.text == '😊 Как дела?':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
                item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

                markup.add(item1, item2)

                bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
