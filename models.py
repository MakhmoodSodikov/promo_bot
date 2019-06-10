import sqlite3
import markups as mrk
import messages as msg
import telegram
from db_requests import *
import constants as const
import random


class Dialog:
    def __init__(self):
        self.Connection = sqlite3.connect("dialogs.db")
        self.Cursor = self.Connection.cursor()
        self.Cursor.execute(CREATE)
        self.Connection.commit()

    def start(self, bot, update):
        user_id = update.message.from_user.id
        first_name = update.message.from_user.first_name
        username = update.message.from_user.username
        print("ID : {} -- New start request from NAME : {} USER: {}".format(user_id, first_name, username))
        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if not len(curs.execute(FIND_USER.format(user_id)).fetchall()):
            curs.execute(INS.format(user_id, first_name, username, 0))
            conn.commit()
            print("ID : {} -- New INSERT into DB have done".format(user_id))

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(update.message.from_user.first_name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))
        else:
            bot.send_message(chat_id=user_id,
                             text=msg.start_text.format(update.message.from_user.first_name),
                             reply_markup=mrk.start_markup(),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Continue...'.format(user_id))

        print('ID : {} -- start function exited'.format(user_id))

    def ask_one(self, bot, update):
        user_id = update.callback_query.from_user.id
        name = update.callback_query.from_user.first_name

        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            print("Crit_sec")
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))

            return
        print("ID : {} -- 1 question reached".format(user_id))
        bot.send_message(chat_id=user_id,
                         text=msg.ask_one,
                         reply_markup=mrk.yes_no('ask_sec'),
                         parse_mode=telegram.ParseMode.MARKDOWN)
        print("ID : {} -- 1 question asked".format(user_id))

    def ask_sec(self, bot, update):
        user_id = update.callback_query.from_user.id

        name = update.callback_query.from_user.first_name

        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            print("Crit_sec")
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))

            return
        print("ID : {} -- 2 question reached".format(user_id))
        bot.send_message(chat_id=user_id,
                         text=msg.ask_sec,
                         reply_markup=mrk.yes_no('ask_third'),
                         parse_mode=telegram.ParseMode.MARKDOWN)
        print("ID : {} -- 2 question asked".format(user_id))

    def ask_third(self, bot, update):
        user_id = update.callback_query.from_user.id

        name = update.callback_query.from_user.first_name

        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            print("Crit_sec")
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))

            return
        print("ID : {} -- 3 question reached".format(user_id))
        bot.send_message(chat_id=user_id,
                         text=msg.ask_third,
                         reply_markup=mrk.yes_no('thx_for'),
                         parse_mode=telegram.ParseMode.MARKDOWN)
        print("ID : {} -- 3 question asked".format(user_id))

    def thx_for(self, bot, update):
        user_id = update.callback_query.from_user.id

        name = update.callback_query.from_user.first_name

        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            print("Crit_sec")
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))

            return

        print("ID : {} -- Thanks!".format(user_id))
        bot.send_message(chat_id=user_id,
                         text=msg.thx_for.format(name),
                         reply_markup=mrk.submit('submit'),
                         parse_mode=telegram.ParseMode.MARKDOWN)
        print("ID : {} -- Thanked".format(user_id))

    def submit(self, bot, update):
        user_id = update.callback_query.from_user.id

        name = update.callback_query.from_user.first_name

        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            print("Crit_sec")
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))

            return
        progress = curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0]
        print("ID : {} -- Selected progress : {}".format(user_id, progress))

        curs.execute(UPD_PROGRESS.format(progress + 1, user_id))
        conn.commit()
        print("ID : {} -- Incremented progress".format(user_id))

        if progress <= 2:
            bot.send_message(chat_id=user_id,
                             text=msg.sorry.format(3),
                             reply_markup=mrk.submit('submit'),
                             parse_mode=telegram.ParseMode.MARKDOWN)
        if 2 < progress <= 3:
            bot.send_message(chat_id=user_id,
                             text=msg.sorry.format(2),
                             reply_markup=mrk.submit('submit'),
                             parse_mode=telegram.ParseMode.MARKDOWN)
        if 4 < progress <= 5:
            bot.send_message(chat_id=user_id,
                             text=msg.sorry.format(1),
                             reply_markup=mrk.submit('submit'),
                             parse_mode=telegram.ParseMode.MARKDOWN)
        if progress > 5:
            bot.send_message(chat_id=user_id,
                             text=msg.success,
                             reply_markup=mrk.submit('success'),
                             parse_mode=telegram.ParseMode.MARKDOWN)

    def success(self, bot, update):
        user_id = update.callback_query.from_user.id
        name = update.callback_query.from_user.first_name

        conn = sqlite3.connect("dialogs.db")
        curs = conn.cursor()

        if curs.execute(GET_PROGRESS.format(user_id)).fetchall()[0][0] == -1:
            print("Crit_sec")
            bot.send_message(chat_id=user_id,
                             text=msg.already.format(name),
                             parse_mode=telegram.ParseMode.MARKDOWN)
            print('ID : {} -- Denied'.format(user_id))

            return
        print("ID : {} -- Succeed")
        bot.send_message(chat_id=user_id,
                         text=msg.burg_info.format(name, random.randint(10, 40000)),
                         parse_mode=telegram.ParseMode.MARKDOWN)

        bot.send_photo(chat_id=user_id, photo=const.URL_QR_CODE.format(name,
                                                                       random.randint(1000000, 100000000)))

        curs.execute(UPD_PROGRESS.format(-1, user_id))
        conn.commit()
