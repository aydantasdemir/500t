# -*- coding: utf8 -*-

from django.db import models


class LogManager(models.Manager):

    def get_latest_logs(self):
        return self.get_query_set().filter(is_enabled=True).order_by("-id")

    def get_favorites(self):
        return self.get_query_set().filter(is_enabled=True).order_by("-karma")

    def get_most_visited(self):
        return self.get_query_set().filter(is_enabled=True).order_by("-visit_count")


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
