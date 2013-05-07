# -*- coding: utf8 -*-
from django.utils.encoding import smart_str

from irc import IRCBot, run_bot

import random
import requests
import json

from cihi_constats import GREETS, ZEN_LIST


class LogarBot(IRCBot):
    def greet(self, nick, message, channel):
        return '%s: %s' % (nick, random.choice(GREETS))

    def pyzen(self, nick, message, channel):
        return '%s: %s' % (nick, random.choice(ZEN_LIST))

    def random_log(self, nick, message, channel):
        r = requests.get("http://500t.org/api/random/")
        log = json.loads(r.text)[0]
        return smart_str('%s: %s - http://500t.org/log/%s' % (nick, log.get("fields").get("title"), log.get("pk")))

    def command_patterns(self):
        return (
            ('selam|merhaba|hi|hello', self.greet),
            ('!pyzen', self.pyzen),
            ('!500t', self.random_log),
        )

host = 'irc.freenode.net'
port = 6667
nick = 'esra'

run_bot(LogarBot, host, port, nick, ['#brotoss', '#pyistanbul', ])
