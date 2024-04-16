import telebot
from telebot import types
import requests
import os

token = '6772739524:AAHRgjEe6xfTsCOXg6gwknGe-iSn9p-1mwc'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button_ru = types.InlineKeyboardButton("🇷🇺", callback_data='lang_ru')
    button_en = types.InlineKeyboardButton("🇺🇸🇬🇧", callback_data='lang_en')
    markup.add(button_ru)
    markup.add(button_en)
    bot.send_message(message.chat.id,"🇺🇸Choose language🇬🇧/🇷🇺Выберете язык🇷🇺".format(message.from_user), reply_markup=markup)




@bot.callback_query_handler(func=lambda call: call.data == 'lang_ru')
def save_btn(call):
    print('ru')


@bot.callback_query_handler(func=lambda call: call.data == 'lang_en')
def save_btn(call):
    print('en')



#@bot.message_handler(content_types=['voice'])
#def get_audio_messages(message):
#    file_info = bot.get_file(message.voice.file_id)
#    path = file_info.file_path
#    fname = os.path.basename(path).lstrip('file_')
#    print(fname)
#    doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
#    with open('voices/' + fname, 'wb') as f:
#        f.write(doc.content)
#    last_audio = str(last_voice(os.listdir('voices')))
#    print(os.listdir('voices'))
#    #print(last_audio)
#    convert(last_audio)
#    text = stt_work(last_audio)
#    print(text)
#    bot.send_message(message.chat.id, text)


bot.infinity_polling()