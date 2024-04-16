import json
ru = json.loads(''.join([i.rstrip('\n') for i in open('utils/ru.json', 'r', encoding='utf-8').readlines()]))
en = json.loads(''.join([i.rstrip('\n') for i in open('utils/en.json', 'r', encoding='utf-8').readlines()]))


def translate(text, lang):
    if lang == 'ru':
        return ru[text]
    elif lang == 'en':
        return en[text]
    else:
        return False
