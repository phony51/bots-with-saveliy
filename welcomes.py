import random
from answers import *


def main(bot):
    def welcome(message):
        rand = random.randint(0, 5)
        if message.text.lower == 'привет':
            bot.send_message(message.chat.id, ans_hello[rand])
        elif message.text.lower == 'как дела' or 'как дела?':
            bot.send_message(message.chat.id, ans_howareu[rand])
        elif message.text.lower == 'что делаешь' or 'что делаешь?':
            bot.send_message(message.chat.id, ans_whatdoudo[rand])
