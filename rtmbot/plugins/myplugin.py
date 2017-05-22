from __future__ import print_function
from rtmbot.core import Plugin

class MyPlugin(Plugin):

    def catch_all(self, data):
        print('## From MyPlugin:', data)
