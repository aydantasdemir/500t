# -*- coding: utf8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.views import auth_logout
from django.contrib import messages

from models import Log, Vote
from forms import AddLogForm

try:
    import simplejson as json
except ImportError:
    import json


def home(request):

    template_data = {
        'logs': Log.objects.get_latest_logs(),
    }

    return render(request, "logs.html", template_data)


def favorites(request):
    template_data = {
        'logs': Log.objects.get_favorites(),
    }

    return render(request, "logs.html", template_data)


def logout(request):
    auth_logout(request)
    return redirect('home')


def add_log(request):

    if not request.user.is_authenticated():
        return redirect('login')

    form = AddLogForm()

    if request.method == 'POST':
        form = AddLogForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            messages.success(request, 'Log başarıyla eklendi.')
            return redirect('home')

    template_data = {
        'form': form,
    }

    return render(request, "add_log.html", template_data)


def login(request):
    return render(request, "login.html", {})


def log_detail(request, log_id):
    log = get_object_or_404(Log, pk=log_id)

    template_data = {
        'log': log,
    }

    return render(request, "log_detail.html", template_data)


def vote(request, log, vote_type):
    log = get_object_or_404(Log, pk=log)

    response = dict()

    try:
        vote = Vote.objects.add_vote(log, vote_type, request.META["REMOTE_ADDR"])

        response.update({
            'status': 1,
            'message': vote.log.karma,
        })
    except Exception as error:
        response.update({
            'status': 0,
            'message': str(error),
        })

    return HttpResponse(json.dumps(response), content_type="application/json")
