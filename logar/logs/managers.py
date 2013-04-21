# -*- coding: utf8 -*-

from django.db import models


class LogManager(models.Manager):

    def get_all(self, request):

        logs = self.get_query_set().all()

        if 'o' in request.GET:
            if request.GET["o"] == 'favorites':
                logs = logs.order_by("-karma")
            elif request.GET["o"] == 'visit_count':
                logs = logs.order_by("-visit_count")
            elif request.GET["o"] == 'huseyinalb':
                logs = logs.order_by("karma")

        else:
            logs = logs.order_by("-id")

        return logs


class VoteManager(models.Manager):
    def add_vote(self, log, vote_type, ip_adress):
        try:
            vote = self.model.objects.get(
                log=log,
                ip=ip_adress
            )

        except self.model.DoesNotExist:
            vote = self.model()
            vote.vote_type = vote_type
            vote.ip = ip_adress
            vote.log= log
            vote.save()

        return vote
