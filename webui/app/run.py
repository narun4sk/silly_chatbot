#!/usr/bin/env python3
# coding: utf-8

from bottle import Bottle, request, response
from bottle import static_file, template
from chatterbot import ChatBot

from console import Command


HOST = '0.0.0.0'
PORT = 8000


# Init WSGI App
bot_ui = Bottle()


# Init ChatBots
BOTS = ['HAL 9000', 'Wall-E', 'Agent Smith']
TRAINER='chatterbot.trainers.ChatterBotCorpusTrainer'
BOT_DICT = {B: ChatBot(B, trainer=TRAINER) for B in BOTS}


# Train based on the english corpus
#for B in BOT_DICT.values():
#    B.train("chatterbot.corpus.english")


# Static resources
@bot_ui.route('/static/<path:path>')
def static(path):
    return static_file(path, root='static/')


# Home page
@bot_ui.route('/')
def home():
    return template('templates/index.html')


# Bot interaction
@bot_ui.route('/askmeanything/')
def askmeanything():
    bot_c = request.get_cookie('bot')
    bot = BOT_DICT.get(bot_c, None)
    cmd = Command(bot=bot, bot_dict=BOT_DICT)
    question = request.query.q.strip()
    print(bot_c, 'is processing question:', question)
    bot_response = cmd.run(q=question)
    if cmd.error:
        return {'response': '<BOT> {answer}'.format(answer=cmd.error)}
    elif cmd.bot:
        bot = cmd.bot
        response.set_cookie('bot', bot.name)
        return {'response': '<BOT@{bot}> {answer}'.format(bot=bot.name, answer=bot_response)}
    elif not cmd.bot:
        response.set_cookie('bot', '')
        return {'response': '<BOT> {answer}'.format(answer=bot_response)}


if __name__ == "__main__":
    from waitress import serve
    msg = 'Serving on -- http://{host}:{port}'
    print(msg.format(host=HOST, port=PORT))
    serve(bot_ui, host=HOST, port=PORT, _quiet=True)
