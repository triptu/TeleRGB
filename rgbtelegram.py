from telegram.ext import *
from webcolors import name_to_rgb as n2rgb
from rgbControl import rgb
from ardupy import *

board=Arduino("COM10")
board.pinMode(9, OUTPUT)
board.pinMode(10, OUTPUT)
board.pinMode(11, OUTPUT)


myToken="<Your toke here>"

def initial(bot, update):
    msg=update.message
    s=msg.text
    print s
    bot.sendmessage(msg.chat_id, text="Type color to make LED glow.")

def control(bot,update):
    msg=update.message
    s= msg.text
    print s
    reply= rgb(board,s)
    bot.sendMessage(msg.chat_id, text=reply)


updater=Updater(token=myToken)
dp=updater.dispatcher
dp.add_handler(CommandHandler("Instructions", initial))
dp.add_handler(MessageHandler([Filters.text], control))

updater.start_polling()
updater.idle()
board.close()
