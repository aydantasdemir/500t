# -*- coding: utf8 -*-

import json

from django.contrib import messages
from django.contrib.auth.views import auth_logout
from django.core import serializers
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from models import Log, Vote
from forms import AddLogForm


def logs(request):
    template_data = {
        'logs': Log.objects.get_all(request)
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
    log = get_object_or_404(Log, pk=log_id).increment_visit_count()

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


@require_POST
def search(request):
    if 'search_text' not in request.POST:
        raise Http404

    logs = Log.objects.search_text(request.POST.get("search_text"))

    if not logs:
        messages.error(request, 'Sonuç bulunamadı.')

    return render(request, "logs.html", {"logs": logs})


def random_log(request):
    data = serializers.serialize("json", Log.objects.all().order_by("?")[0:1])
    return HttpResponse(data, content_type="application/json")
