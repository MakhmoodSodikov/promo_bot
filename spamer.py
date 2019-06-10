import sqlite3
from constants import *
import telegram
import time
from db_requests import *
from messages import we_miss_you

conn = sqlite3.connect("dialogs.db")
curs = conn.cursor()
ls = curs.execute(GET_USERS_PROGMIN).fetchall()
print('Progressed users list: ', ls)
bot = telegram.Bot(TOKEN_TELEGRAM_BOT)

msg = we_miss_you

for user_id in ls:
    try:
        print(user_id)
        bot.send_message(chat_id=user_id,
                         text=msg,
                         parse_mode=telegram.ParseMode.MARKDOWN)
        print('Send to {}'.format(user_id))
        # time.sleep(2) # if your connection is low, try this to avoid TimedOutError
        print("Next")
    except telegram.error.Unauthorized:
        print('Blocked by ', user_id)
    except telegram.error.TimedOut:
        print('Timed out on ID ', user_id)
    except telegram.error.RetryAfter:
        time.sleep(10)
