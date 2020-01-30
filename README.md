Django Imageboard
=================
Мой первый проект с использованием Django Framework.

------------
1.  [Django 3.0.2](https://github.com/django/django)
2.  [sorl-thumbnail 12.6.0](https://github.com/jazzband/sorl-thumbnail)
3.  [Django Simple Captcha](https://github.com/mbi/django-simple-captcha)
4.  [Django Cleanup](https://github.com/un1t/django-cleanup)
5.  [django-precise-bbcode](https://github.com/ellmetha/django-precise-bbcode)

Инструкция
----------
Создаем виртуальное окружение

    virtualenv imageboard
Переходим в папку imageboard

    cd imageboard
Активируем виртуальное окружение Python

    source bin/activate
Скачиваем данный проект 

    git clone https://github.com/yanfedorov/imageboard.git
    cd imageboard
Установка Django и дополнительных библиотек в виртуальное окружение

    pip install -r requirements.txt
Установка sorl-thumbnail производится с GitHub, так как на pypi.org лежит версия 12.5.0 без поддержки Django 3.x.

    git clone https://github.com/jazzband/sorl-thumbnail.git
    cd sorl-thumbnail
    python setup.py install
    cd ..
Запускаем сервер

    python manage.py runserver
    

