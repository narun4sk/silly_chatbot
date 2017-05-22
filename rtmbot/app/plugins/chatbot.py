#!/usr/bin/env python3
# coding: utf-8

from rtmbot.core import Plugin
from chatterbot import ChatBot

from plugins.console import Command


# Sessions
SESS = {}


# Init ChatBots
BOTS = ['HAL 9000', 'Wall-E', 'Agent Smith']
TRAINER='chatterbot.trainers.ChatterBotCorpusTrainer'
BOT_DICT = {B: ChatBot(B, trainer=TRAINER) for B in BOTS}


# Train based on the english corpus
#for B in BOT_DICT.values():
#    B.train("chatterbot.corpus.english")


class Reply(Plugin):

    def process_message(self, data):
        print(data)
        channel = data['channel']
        if not channel.startswith("D"):
            return
        user = data['user']
        team = data['team']
        # User ID
        uid = '_'.join([user,team])
        bot = SESS.get(uid, None)
        cmd = Command(bot=bot, bot_dict=BOT_DICT)
        question = data['text'].strip()
        if bot:
            print(bot.name, 'is processing question:', question)
        else:
            print('Processing question:', question)
        bot_response = cmd.run(q=question)
        if cmd.error:
            self.outputs.append([channel, '<BOT> {answer}'.format(answer=cmd.error)])
        elif cmd.bot:
            bot = cmd.bot
            SESS[uid] = bot
            answ_dict = dict(bot=bot.name, answer=bot_response)
            self.outputs.append([channel, '<BOT@{bot}> {answer}'.format(**answ_dict)])
        elif not cmd.bot:
            if uid in SESS:
                del SESS[uid]
            self.outputs.append([channel, '<BOT> {answer}'.format(answer=bot_response)])
