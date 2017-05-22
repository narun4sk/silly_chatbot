#!/usr/bin/env python3
# coding: utf-8

from chatterbot import ChatBot


class Command:
    """ Handle user input and commands.
    """

    def __init__(self, bot=None, bot_dict=None):
        self._prefix = '@tellme'
        self._user_in = None
        self._bot = bot
        self._bot_dict = bot_dict if isinstance(bot_dict, dict) else {}
        self._error = None

    def user_in(self, q=''):
        """ Remove prefix from the user input and convert it to the list.
        """
        user_in = q.split()
        if len(user_in) > 1 and user_in[0]==self._prefix:
            self._user_in = user_in[1:]
        else:
            self._error = 'Please use "​%s" prefix with all the input.\n' % self._prefix
        return self._user_in

    @property
    def bot(self):
        return self._bot

    @property
    def error(self):
        return self._error

    @property
    def _commands(self):
        """ Known commands.
        """
        return {'help': self.bot_help,
                'list': self.bot_list,
                'start_session': self.start_session,
                'end_session': self.end_session}

    def run(self, q=''):
        """ If user input seems valid, then call appropriate handler function.
        """
        commands = self._commands
        user_in = self.user_in(q=q)
        if user_in and user_in[0] in commands:
            return commands[user_in[0]]()
        elif user_in and self._bot:
            return self.bot_response()
        else:
            self._error = 'Unknown command...'

# --- Handler functions

    def bot_help(self, *a, **kw):
        """ Print basic help.
        """
        msg = 'Please use "​%s" prefix with all the input.\n' % self._prefix
        msg += 'Available Bot commads are:\n'
        for x in self._commands:
            msg += str('- %s %s\n' % (self._prefix, x))
        return msg

    def bot_list(self, *a, **kw):
        """ Display Bot list.
        """
        msg = 'Currently online:\n'
        return msg + '\n'.join('- %s' % b for b in self._bot_dict)

    def start_session(self, *a, **kw):
        """ Starting the session is nothing more than selecting the valid Bot instance.
        """
        user_in = self._user_in
        if user_in and len(user_in) > 1:
            bot = ' '.join(self._user_in[1:])
            if bot in self._bot_dict:
                self._bot = self._bot_dict[bot]
                assert isinstance(self._bot, ChatBot),\
                'Must be an instance of chatterbot.ChatBot'
                return 'Selected "%s" for this session.' % self._bot.name
            else:
                self._error = 'Bot "%s" does not exist, sorry :/' % bot
        else:
            self._error = "You've forgotten to specify Bot name"

    def end_session(self, *a, **kw):
        """ Session is invalidated when there's no Bot selected.
        """
        self._bot = None
        return 'Session ended.'

    def bot_response(self, *a, **kw):
        """ Return Bot response to the question.
        """
        bot = self._bot
        user_in = ' '.join(self._user_in)
        if not self._bot:
            self._error = "Please choose a Bot"
        # Get a response to an input statement
        try:
            bot_response = bot.get_response(user_in)
        except Exception as e:
            self._error = e
            print(e)
        else:
            return bot_response.text