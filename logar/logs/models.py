# -*- coding: utf8 -*-

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

from managers import LogManager
from managers import VoteManager


class Log(models.Model):
    title = models.CharField("Başlık", max_length=255)
    body = models.TextField("İçerik")
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, verbose_name="Gönderen")
    visit_count = models.IntegerField(default=0)
    karma = models.IntegerField(default=0)

    def __unicode__(self):
        return "<Log: {0}>".format(self.id)

    class Meta:
        db_table = 'logs'

    objects = LogManager()


VOTE_CHOICES = (
    (1, 'up'),
    (2, 'down'),
)


class Vote(models.Model):

    log = models.ForeignKey(Log)
    ip = models.IPAddressField()
    vote_type = models.IntegerField("Oy tipi", choices=VOTE_CHOICES)

    objects = VoteManager()

    def __unicode__(self):
        return smart_unicode("<Rating: {0}-{1}>".format(self.log.title, self.ip))

    class Meta:
        db_table = 'votes'

