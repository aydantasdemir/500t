# -*- coding: utf8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver

from models import Vote


@receiver(post_save, sender=Vote)
def update_log_karma(sender, instance, **kwargs):
    """
    updates log karma based on ups & downs.
    """
    instance.vote_type = int(instance.vote_type)

    if instance.vote_type == 1:
        instance.log.karma += 1
    else:
        instance.log.karma -= 1


    instance.log.save()