#!/usr/bin/env python3
# coding: utf-8

from webtest import TestApp as App
from urllib.parse import urlencode

from run import bot_ui


class TestWebui:

    app = App(bot_ui)

    def uri(self, path, query={}):
        path = '/' + path.lstrip('/')
        if query:
            return '?'.join([path, urlencode(query)])
        return path + urlencode(query)

    def test_home(self):
        uri = self.uri('/')
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'text/html'

    def test_askmeanything(self):
        uri = self.uri('askmeanything/')
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert resp.json['response'] == '<BOT> Unknown command...'

    def test_askmeanything_tellme(self):
        uri = self.uri('askmeanything/', {'q': '@tellme'})
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert resp.json['response'] == '<BOT> Unknown command...'

    def test_askmeanything_tellme_help(self):
        uri = self.uri('askmeanything/', {'q': '@tellme help'})
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert 'Please use' in resp.json['response']

    def test_askmeanything_tellme_list(self):
        uri = self.uri('askmeanything/', {'q': '@tellme list'})
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert 'Currently online' in resp.json['response']

    def test_askmeanything_start_sess(self):
        uri = self.uri('askmeanything/', {'q': '@tellme start_session'})
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert 'forgotten to specify Bot name' in resp.json['response']
        uri = self.uri('askmeanything/', {'q': '@tellme start_session unknown_bot'})
        resp = self.app.get(uri)
        assert '"unknown_bot"' in resp.json['response']
        uri = self.uri('askmeanything/', {'q': '@tellme start_session Agent Smith'})
        resp = self.app.get(uri)
        assert 'BOT@Agent Smith' in resp.json['response']

    def test_askmeanything_end_sess(self):
        uri = self.uri('askmeanything/', {'q': '@tellme end_session'})
        resp = self.app.get(uri)
        assert resp.status_int == 200
        assert resp.content_type == 'application/json'
        assert 'Session ended' in resp.json['response']
