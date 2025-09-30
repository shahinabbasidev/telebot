from telebot import TeleBot,types
from dotenv import load_dotenv
import os
import query

admins = ["474476386"]
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = str(message.from_user.id)
    user_name = message.from_user.username

    query.insert_user(user_id, user_name)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('سرویس ها','نوبت دهی')
    if user_id in admins:
        markup.row('اضافه کردن سرویس')

    bot.send_message(message.chat.id,"  لطفا یکی از گزینه ها رو انتخواب کنید به بات خوش آمدید.\n", reply_markup=markup)








bot.infinity_polling()