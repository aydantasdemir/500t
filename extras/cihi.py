# -*- coding: utf8 -*-
from django.utils.encoding import smart_str

from irc import IRCBot, run_bot

import random
import requests
import json
import re

from cihi_constants import GREETS, ZEN_LIST


class LogarBot(IRCBot):
    def greet(self, nick, message, channel):
        return '%s: %s' % (nick, random.choice(GREETS))
   
    def hamachi(self, nick, message, channel):
        return "WIN/MAC: https://secure.logmein.com/products/hamachi/download.aspx, LINUX: http://www.haguichi.net/download/ "

    def pyzen(self, nick, message, channel):
        return '%s: %s' % (nick, random.choice(ZEN_LIST))

    def cs(self, nick, message, channel):
        return "http://pirateproxy.net/torrent/3825488/Counter_strike_1.6"

    def cs_macfag(self, nick, message, channel):
        return "http://pirateproxy.net/torrent/8221915/Counter_Strike_1.6_for_Mac_OS"

    def random_log(self, nick, message, channel):
        r = requests.get("http://500t.org/api/random/")
        log = json.loads(r.text)[0]
        return smart_str('%s: %s - http://500t.org/log/%s' % (nick, log.get("fields").get("title"), log.get("pk")))

    def talk(self, nick, message, channel):
        if 'oguz' in nick:
            content = requests.get("http://www.guzelsozlerin.com/sevgi-sozleri.html").text
            return smart_str(random.choice(re.findall('<p><strong>(.*?)</strong></p>', content, flags=re.MULTILINE)))


        r = requests.get("http://eksisozluk.com/?q=%s" % " ".join(message.split(" ")[0:2]))
        results = re.findall('<div class="content">(.*?)</div>', r.text)

        if len(results) == 0:
            r = requests.get("http://eksisozluk.com/?q=%s" % " ".join(message.split(" ")[0:1]))
            results = re.findall('<div class="content">(.*?)</div>', r.text)

        if len(results) > 0:
            result = random.choice(results)
            result = re.sub('<[^<]+?>', '', result)

            return smart_str(result)

    def command_patterns(self):
        return (
            ('selam|merhaba|hi|hello', self.greet),
            ('!pyzen', self.pyzen),
            ('!cs$', self.cs),
            ('!hamachi', self.hamachi),
            ('!cs_macfag', self.cs_macfag),
            ('!500t', self.random_log),
            self.ping('.*', self.talk),
        )

host = 'irc.freenode.net'
port = 6667
nick = 'selin'

run_bot(LogarBot, host, port, nick, ['#brotoss', '#pyistanbul', ])
