
import telebot
token = ''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass

@bot.message_handler(content_types=['text'])
def new_message(message):
    if message:
        print('Новое сообщение')
        print()




if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)