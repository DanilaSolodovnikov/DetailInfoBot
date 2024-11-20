import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('YOUR_TOKEN')
user_id = {}


procedures_info = {"1": {"description": 'Описание 1 процедуры',"photo_before": "before1.png", "photo_after": 'after1.png'},
                   "2": {"description": 'Описание 2 процедуры',"photo_before": "before2.png", "photo_after": 'after2.png'},
                   "3": {"description": 'Описание 3 процедуры',"photo_before": "before3.png", "photo_after": 'after3.png'},
                   "4": {"description": 'Описание 4 процедуры',"photo_before": "before4.png", "photo_after": 'after4.png'},
                   "5": {"description": 'Описание 5 процедуры',"photo_before": "before5.png", "photo_after": 'after5.png'},
                   "6": {"description": 'Описание 6 процедуры',"photo_before": "before6.png", "photo_after": 'after6.png'},
                   "7": {"description": 'Описание 7 процедуры',"photo_before": "before7.png", "photo_after": 'after7.png'},
                   "8": {"description": 'Описание 8 процедуры',"photo_before": "before8.png", "photo_after": 'after8.png'},
                   "9": {"description": 'Описание 9 процедуры',"photo_before": "before9.png", "photo_after": 'after9.png'}}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    button_procedures = InlineKeyboardButton('Услуги', callback_data='procedures')
    keyboard.add(button_procedures)
    bot.send_message(message.chat.id, 'Привет.\n В данном боте ты можешь узнать какие услуги мы предоставляем!\nНажми кнопку ниже!', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data=='procedures')
def procedures(call):
    keyboard = InlineKeyboardMarkup()
    list_procedure = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for procedure in list_procedure:
        keyboard.add(InlineKeyboardButton(procedure, callback_data=procedure))
    bot.send_message(call.message.chat.id, "Выберите процедуру о которой хотите узнать информацию:", reply_markup=keyboard)

@bot.callback_query_handler(lambda call: call.data in procedures_info.keys())
def procedure_info(call):
    procedure = call.data
    info = procedures_info[procedure]

    bot.send_message(call.message.chat.id, info["description"])

    with open(info["photo_before"], 'rb') as photo_before:
        bot.send_photo(call.message.chat.id, photo_before, caption="До")

    with open(info["photo_after"], 'rb') as photo_after:
        bot.send_photo(call.message.chat.id, photo_after, caption="После")


bot.polling(none_stop=True)
PIDARAS