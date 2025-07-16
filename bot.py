import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')
updater = Updater(token=token)

def kino(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("titanik", callback_data="menu_kinolar")],
        [InlineKeyboardButton("alita", callback_data="menu_kinolarsd")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("qaysi kinoni tanlaysiz", reply_markup=reply_markup)
    print('salom - kino funksiyasi ishladi')

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data
    print("Bosilgan tugma callback_data:", data)

    if data == "menu_kinolar":
        keyboard = [
            [InlineKeyboardButton("Titanic", callback_data="titanik")],
            [InlineKeyboardButton("Avatar", callback_data="titanik")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text("Kinolar ro'yxati:", reply_markup=reply_markup)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler(command="start",callback=kino))
dispatcher.add_handler(CallbackQueryHandler(callback=button))

updater.start_polling()
updater.idle()




