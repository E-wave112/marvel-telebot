##using telegram to creat a an mcu video downloader bot
from telegram.ext import Updater,InlineQueryHandler, CommandHandler
import requests,logging
from decouple import config

from bs4 import BeautifulSoup
import time


##starter function
def starter():
    return 'welcome to the Marvel Cinematic Universe movie downloader bot!\n\
        To download any movie in the mcu type the command : /moviename (e.g /ironman, /captainamerica e.t.c)\n\
        Get news and movie updates about the MCU by checking the following platforms:\n\
        Official Website: https://www.marvel.com/movies\n\
        Twiiter Handle : http://twitter.com/marvel\n\
        Facebbok Fan Page:http://facebook.com/marvel\n \
        Youtube Channel:http://youtube.com/marvel\n\
        Instagram:http://instagram.com/marvel\n\
        Pinterest:https://www.pinterest.com/marvelofficial'
##we are to define custom scripts for movies in the mcu (starting with captain america, iron man, thor and avengers)
def mcuiron():
    iron_dict = {
        'iron_man':config('iron_man'), 
        'iron_man_2':config('iron_man_2'),
        'iron_man_3':config('iron_man_3')
    }
    return '\n\n\n\n'.join([iron_dict[i] for i in iron_dict])


def mcucap():
    cap_dict = {
        'capfirst':config('capfirst'),
        'capwin':config('capwin'),
        'capcivil':config('capcivil')
    }
    return '\n\n\n\n'.join([cap_dict[i] for i in cap_dict])

def mcuavengers():
    avg_dict = {
        'avg1':config('avg1'),
        'avgultron':config('avgultron'),
        'avginfinity':config('avginfinity'),
        'avgendgame':config('avgendgame')
    }

    return '\n\n\n\n'.join([avg_dict[i] for i in avg_dict])

def mcuhulk():
    return config('hulk')

def mcuthor():
    thor = {
        'thor':config('thor'),
        'thor2':config('thor2'),
        'thorrag':config('thorrag')
    }

    return '\n\n\n\n'.join([thor[i] for i in thor])


def mcudrstrange():
    return config('strange')


def mcuguardians():
    guardians_dict = {
        'guardians':config('guardians'),
        'guardians2':config('guardians2')
    }
    return '\n\n\n\n'.join([guardians_dict[i] for i in guardians_dict])


def mcublackpanther():
    return config('blackpanther')

def mcuspider():
    spider_dict = {
        'spider':config('spider'),
        'spiderfar':config('spiderfar')
    }

    return '\n\n\n\n'.join([spider_dict[i] for i in spider_dict])

def mcucapmarvel():
    return config('capmarvel')


def mcuantman():
    antman_dict = {
        'antman':config('antman'),
        'antman2':config('antman2')
        }

    return '\n\n\n\n'.join(antman_dict[i] for i in antman_dict)




##starter for the telegram bot
def start(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=starter())

##dispatcher for iron man
def iron(update,context):
    ironman= mcuiron()
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=ironman)

##telegram dispatcher for cap america
def captain(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=mcucap())

##telegram dispatcher for avengers
def avengers(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcuavengers())

##telegram dispatcher for the hulk
def hulk(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcuhulk())
##telegram dispatcher for thor
def thor(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcuthor())
##telegram dispatcher for guardians for the galaxy
def guardians(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcuguardians())
##telegram dispatcher for antman
def antman(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcuantman())
##telegram dispatcher for doctorstrange
def drstrange(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcudrstrange())
##telegram dispatcher for blackpanther
def blackpanther(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcublackpanther())
##telegram dispatcher for captainmarvel
def captainmarvel(update,context):
    chat_id=update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcucapmarvel())
##telegram dispatcher spiderman
def spiderman(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text=mcuspider())
##driver function
def main():
    updater = Updater(config("token2"),use_context=True)
    dp = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logger = logging.getLogger(__name__)
    dp.add_handler(CommandHandler('ironman',iron))
    dp.add_handler(CommandHandler('hulk',hulk))
    dp.add_handler(CommandHandler('thor',thor))
    dp.add_handler(CommandHandler('doctorstrange',drstrange))
    dp.add_handler(CommandHandler('blackpanther',blackpanther))
    dp.add_handler(CommandHandler('spiderman',spiderman))
    dp.add_handler(CommandHandler('captainmarvel',captainmarvel))
    dp.add_handler(CommandHandler('guardiansofthegalaxy',guardians))
    dp.add_handler(CommandHandler('antman',antman))
    dp.add_handler(CommandHandler('captainamerica',captain))
    dp.add_handler(CommandHandler('avengers',avengers))
    dp.add_handler(CommandHandler('start',start))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
