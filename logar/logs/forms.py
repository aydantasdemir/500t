# -*- coding: utf8 -*-

from django import forms

from models import Log


class AddLogForm(forms.ModelForm):

    class Meta:
        model = Log
        exclude = ('sender', 'is_enabled', 'created_at', 'visit_count', 'karma')

    def save(self, user, *args, **kwargs):
        instance = super(AddLogForm, self).save(commit=False)
        instance.sender = user
        instance.save()

        return instance

