Django Imageboard
=================
Мой первый проект с использование Django Framework.


------------
1.  [Django 3.0.2](https://github.com/django/django)
2.  [sorl-thumbnail 12.6.0](https://github.com/jazzband/sorl-thumbnail)
3.  [Django Simple Captcha](https://github.com/mbi/django-simple-captcha)
4.  [Django Cleanup](https://github.com/un1t/django-cleanup)
5.  [django-precise-bbcode](https://github.com/ellmetha/django-precise-bbcode)

sorl-thumbnail устанавливать версии 12.6.0 с [GitHub](https://github.com/jazzband/sorl-thumbnail/releases/tag/12.6.0), так как на pypi.org лежит версия без поддержки Django 3.x.
pip install django
pip install django-precise-bbcode
pip install  django-simple-captcha
pip install django-cleanup

prectise.models precise.fields.py
from django.utils.encoding import python_2_unicode_compatible -> from six import python_2_unicode_compatible
tampletags.bbcode_tags.py 
from django.utils import six -> import six