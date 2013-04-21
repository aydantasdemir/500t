# -*- coding: utf8 -*-
from fabric.api import local, settings

GUNICORN_PORT = 8055


def restart():
    with settings(warn_only=True):
        local("ps ax | grep {0} | awk '{{print $1}}' | xargs kill -9".format(GUNICORN_PORT))
    local("git pull")
    local("./manage.py migrate logs")
    local("./manage.py collectstatic --noinput")
    local("python manage.py run_gunicorn -b 0.0.0.0:{0} -D".format(GUNICORN_PORT))
