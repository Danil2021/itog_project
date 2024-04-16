import telebot
from telebot import types
from libs import sql_work
from libs.translate import translate
import requests
from libs import stt
import os
from libs import ai_work
import datetime

token = '6772739524:AAHRgjEe6xfTsCOXg6gwknGe-iSn9p-1mwc'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    if sql_work.check_user(str(message.chat.id)):
        lang = sql_work.get_user_lang(message.chat.id)
        if lang == 'ru':
            bot.send_message(message.chat.id, translate('greet', lang=lang))
            bot.send_message(message.chat.id, translate("short_guide", lang=lang), reply_markup=main_keyboard(lang))
        elif lang == 'en':
            bot.send_message(message.chat.id, translate('greet', lang=lang))
            bot.send_message(message.chat.id, translate("short_guide", lang=lang), reply_markup=main_keyboard(lang))
    else:
        markup = types.InlineKeyboardMarkup()
        button_ru = types.InlineKeyboardButton(translate('flag', 'ru'), callback_data='lang_ru')
        button_en = types.InlineKeyboardButton(translate('flag', 'en'), callback_data='lang_en')
        markup.add(button_ru)
        markup.add(button_en)
        bot.send_message(message.chat.id,
                         f"{translate('set_lang', 'ru')}/{translate('set_lang', 'en')}".format(message.from_user),
                         reply_markup=markup)




@bot.callback_query_handler(func=lambda call: call.data == 'lang_ru')
def save_btn(call):
    sql_work.create_new_user(str(call.message.chat.id), 'ru')
    sql_work.create_new_user_table(str(call.message.chat.id))
    bot.send_message(call.message.chat.id, translate("greet_new", 'ru'))
    bot.send_message(call.message.chat.id, translate("short_guide", 'ru'))


@bot.callback_query_handler(func=lambda call: call.data == 'lang_en')
def save_btn(call):
    sql_work.create_new_user(str(call.message.chat.id), 'en')
    sql_work.create_new_user_table(str(call.message.chat.id))
    bot.send_message(call.message.chat.id, translate('greet_new', 'en'))
    bot.send_message(call.message.chat.id, translate("short_guide", 'en'))


def main_keyboard(lang):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    get_zap = types.KeyboardButton(text=translate('zapisi', lang=lang))
    settings = types.KeyboardButton(text=translate('settings', lang=lang))
    keyboard.add(get_zap, settings)
    return keyboard



@bot.message_handler(content_types=['voice'])
def get_audio_messages(message):
    lang = sql_work.get_user_lang(message.chat.id)
    file_info = bot.get_file(message.voice.file_id)
    path = file_info.file_path
    fname = os.path.basename(path).lstrip('file_')
    doc = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
    with open('tmp/' + fname, 'wb') as f:
        f.write(doc.content)
    text = stt.stt_work(fname[:-4])
    #short_text = ai_work.shorted_text(text)
    short_text = "Its not working yet"
    voice = f'voices/{message.chat.id}/{fname[:-4]}.wav'
    sql_work.add_new_value(chatid=str(message.chat.id), text=text, shorted=short_text, voice=voice)
    bot.send_message(message.chat.id,
                     f'{translate("success1", lang)}`{datetime.datetime.now().strftime("%d\.%m\.%Y %H:%M:%S")}` {translate("success2", lang)}\n```{datetime.datetime.now().strftime("%d.%m.%Y")}\n{text}```\n{translate('short', lang)}:\n`{short_text}`', parse_mode='MarkdownV2', reply_to_message_id=message.message_id)




bot.infinity_polling()