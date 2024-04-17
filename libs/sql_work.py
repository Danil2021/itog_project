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
    cursor.execute(f'CREATE TABLE t{chatid} (text TEXT NOT NULL, shorted TEXT NOT NULL, voice TEXT, date TEXT NOT NULL, msg_id TEXT NOT NULL);')
    con.commit()

def add_new_value(chatid, text, shorted, voice, msg_id):
    con = sqlite3.connect(f'dbs/{chatid}.db')
    cursor = con.cursor()
    cursor.execute(f'INSERT INTO t{chatid} (text, shorted, voice, date, msg_id) VALUES (?,?,?,?,?)', (text, shorted, voice, datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), msg_id))
    con.commit()
    con.close()

def get_all_values(chatid):
    con = sqlite3.connect(f'dbs/{chatid}.db')
    cursor = con.cursor()
    values = cursor.execute(f'SELECT * FROM t{chatid};').fetchall()
    con.close()
    return values

def set_user_lang(chatid, lang):
    con = sqlite3.connect('dbs/root.db')
    cursor = con.cursor()
    cursor.execute(f'UPDATE root SET lang =? WHERE chatid =?;', (lang, chatid))
    con.commit()
    con.close()


