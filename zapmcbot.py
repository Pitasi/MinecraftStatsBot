#!/usr/bin/env python3

#############################################
#                                           #
#  IMPORT                                   #
#                                           #
#############################################

import telebot
import re
import json
import logging
from time import time, strftime
from aux import *
from config import *

#############################################
#                                           #
#  DEBUG LOGGER TO FILE                     #
#  (uncomment to enable)                    #
#                                           #
#############################################

'''
logpath = '/var/tagalertbot'
logname = 'registro.log'

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler("{0}/{1}".format(logpath, logname))
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)
'''


#############################################
#                                           #
#  STARTING THE BOT(s)                      #
#                                           #
#############################################

bot = telebot.TeleBot(main_bot_token)
bot.skip_pending = skip_pending


#############################################
#                                           #
#  HANDLERS                                 #
#                                           #
#############################################

@bot.message_handler(commands=['utenti'])
def utenti(message):
    bot.reply_to(message,
    "Ci sono *%s giocatori* registrati nel nostro server." % users_number(),
    parse_mode="markdown")


@bot.message_handler(commands=['salti'])
def salti(message):
    bot.reply_to(message, print_jumps(), parse_mode="markdown")


@bot.message_handler(commands=['morti'])
def morti(message):
    bot.reply_to(message, print_deaths(), parse_mode="markdown")
    
    
@bot.message_handler(commands=['scheletro, scheletri'])
def skeletons(message):
    bot.reply_to(message, "Per colpa di *scheletri*:\n%s" %
                           print_killed_by("skeleton"),
    parse_mode="markdown")
    
    
@bot.message_handler(commands=['zombie'])
def zombie(message):
    bot.reply_to(message, "Per colpa di *zombie*:\n%s" %
                           print_killed_by("zombie"),
                 parse_mode="markdown")
    
    
@bot.message_handler(commands=['enderman'])
def enderman(message):
    bot.reply_to(message, "Per colpa di *enderman*:\n%s" % 
                           print_killed_by("enderman"),
                 parse_mode="markdown")


#############################################
#                                           #
#  POLLING                                  #
#                                           #
#############################################

bot.polling(none_stop=False)
