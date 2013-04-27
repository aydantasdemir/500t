logar
=======

webapp for storing funny irc logs. contains exclusive turkish trolling, powers 500t.org

<img src="https://raw.github.com/pyistanbul/500t/master/500t.png">

installation
===================

* ```pip install -r requirements.txt```
* move local_settings.ex to local_settings.py and set your config.
* ```python manage.py collectstatic```
* ```python manage.py syncdb```
* ```python manage.py migrate```
* ```python manage.py runserver``` 

