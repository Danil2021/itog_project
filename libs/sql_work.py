import sqlite3
import datetime

def check_user(chatid):
    con = sqlite3.connect('dbs/root.db')
    cursor = con.cursor()
    chatids = cursor.execute('SELECT chatid FROM root;')
    if chatid in [i[0] for i in chatids.fetchall()]:
        con.close()
        return True
    else:
        con.close()
        return False

def get_user_lang(chatid):
    con = sqlite3.connect('dbs/root.db')
    cursor = con.cursor()
    lang = cursor.execute(f'SELECT lang FROM root WHERE chatid = {chatid};').fetchone()[0]
    con.close()
    return lang

def create_new_user(chatid, lang):
    con = sqlite3.connect('dbs/root.db')
    cursor = con.cursor()
    cursor.execute('INSERT INTO root (chatid, lang) VALUES (?,?)', (chatid, lang))
    con.commit()
    con.close()

def create_new_user_table(chatid):
    open(f'dbs/{chatid}.db', 'w')
    con = sqlite3.connect(f'dbs/{chatid}.db')
    cursor = con.cursor()
    cursor.execute(f'CREATE TABLE t{chatid} (text TEXT NOT NULL, shorted TEXT NOT NULL, voice TEXT, date TEXT NOT NULL);')
    con.commit()

def add_new_value(chatid, text, shorted, voice):
    con = sqlite3.connect(f'dbs/{chatid}.db')
    cursor = con.cursor()
    cursor.execute(f'INSERT INTO t{chatid} (text, shorted, voice, date) VALUES (?,?,?,?)', (text, shorted, voice, datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")))
    con.commit()
    con.close()


