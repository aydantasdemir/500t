# -*- coding: utf8 -*-

from django.contrib import admin

from models import Log, Vote


class LogAdmin(admin.ModelAdmin):
    pass


class VoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Log, LogAdmin)
admin.site.register(Vote, VoteAdmin)
