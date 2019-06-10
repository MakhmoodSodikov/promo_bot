from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import constants as const
import models

if __name__ == '__main__':
    updater = Updater(token=const.TOKEN_TELEGRAM_BOT)
    dispatcher = updater.dispatcher
    dialogs = models.Dialog()

    # ------------------------------------------------------
    dispatcher.add_handler(CommandHandler('start',
                                          callback=lambda bot, update: dialogs.start(bot, update)))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ask_one',
                                                callback=lambda bot, update: dialogs.ask_one(bot, update)))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ask_sec',
                                                callback=lambda bot, update: dialogs.ask_sec(bot, update)))
    dispatcher.add_handler(CallbackQueryHandler(pattern='ask_third',
                                                callback=lambda bot, update: dialogs.ask_third(bot, update)))
    dispatcher.add_handler(CallbackQueryHandler(pattern='thx_for',
                                                callback=lambda bot, update: dialogs.thx_for(bot, update)))
    dispatcher.add_handler(CallbackQueryHandler(pattern='submit',
                                                callback=lambda bot, update: dialogs.submit(bot, update)))
    dispatcher.add_handler(CallbackQueryHandler(pattern='success',
                                                callback=lambda bot, update: dialogs.success(bot, update)))

    # ------------------------------------------------------
    updater.start_polling(clean=True)
    updater.idle()
