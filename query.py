import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
bot_db = os.environ['BOT_DB']


def connect_to_db():
    conn = sqlite3.connect(bot_db)
    cursor = conn.cursor()
    return conn, cursor

def insert_user(user_id,user_name):
    conn, cursor = connect_to_db()
    cursor.execute('INSERT OR IGNORE INTO users (user_id, user_name) VALUES (?, ?)', (user_id, user_name))


    conn.commit()
    conn.close()