#!/usr/bin/env python3
# coding: utf-8

from unittest.mock import create_autospec
from slackclient import SlackClient, _channel, _server, _util
from rtmbot.core import RtmBot
from testfixtures import LogCapture

from plugins.chatbot import Reply


def init_rtmbot():
    ''' Initializes an instance of RTMBot with some default values '''
    rtmbot = RtmBot({
        'SLACK_TOKEN': 'test-12345',
        'BASE_PATH': '/tmp/',
        'LOGFILE': '/tmp/rtmbot.log',
        'DEBUG': True
    })
    return rtmbot


def test_init():
    with LogCapture() as l:
        rtmbot = init_rtmbot()

    assert rtmbot.token == 'test-12345'
    assert rtmbot.directory == '/tmp/'
    assert rtmbot.debug == True

    l.check(
        ('root', 'INFO', 'Initialized in: /tmp/')
    )


class TestRTMBot:

    RTMBot = init_rtmbot()

    Server_mock = create_autospec(_server.Server)
    SlackClient_mock = create_autospec(SlackClient)
    SearchList_mock = create_autospec(_util.SearchList)
    Channel_mock = create_autospec(_channel.Channel)

    # Mock Server with channels method and correct return value
    Server_mock.channels = SearchList_mock
    SlackClient_mock.server = Server_mock
    SlackClient_mock.server.channels.find.return_value = Channel_mock

    RTMBot.slack_client = SlackClient_mock

    #Plugin_mock = create_autospec(Reply)
    Plugin_mock = Reply()
    #plugin_mock.slack_client = SlackClient_mock

    RTMBot.bot_plugins.append(Plugin_mock)

    message = {
        'channel': 'D5FQCHAN',
        'source_team': 'T5HQTEAM',
        'team': 'T5HQTEAM',
        'text': '',
        'type': 'message',
        'user': 'U5THEBEST'}

    def bot_trigger(self, txt):
        self.message['text'] = txt
        self.Plugin_mock.process_message(self.message)
        self.RTMBot.output()

    def test_tellme(self):
        self.bot_trigger('')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert a[0] == '<BOT> Unknown command...'
        self.Channel_mock.reset_mock()

        self.bot_trigger('@tellme')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert a[0] == '<BOT> Unknown command...'
        self.Channel_mock.reset_mock()

    def test_tellme_help(self):
        self.bot_trigger('@tellme help')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert 'Please use' in a[0]
        self.Channel_mock.reset_mock()

    def test_tellme_list(self):
        self.bot_trigger('@tellme list')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert 'Currently online' in a[0]
        self.Channel_mock.reset_mock()

    def test_start_sess(self):
        self.bot_trigger('@tellme start_session')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert 'forgotten to specify Bot name' in a[0]
        self.Channel_mock.reset_mock()

        self.bot_trigger('@tellme start_session unknown_bot')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert '"unknown_bot"' in a[0]
        self.Channel_mock.reset_mock()

        self.bot_trigger('@tellme start_session Agent Smith')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert 'BOT@Agent Smith' in a[0]
        self.Channel_mock.reset_mock()

    def test_end_sess(self):
        self.bot_trigger('@tellme end_session')
        assert self.Channel_mock.send_message.called
        a, kw = self.Channel_mock.send_message.call_args
        assert 'Session ended' in a[0]
        self.Channel_mock.reset_mock()
