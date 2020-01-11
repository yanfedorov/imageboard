from django.core.validators import FileExtensionValidator
from django.core.files.images import get_image_dimensions
from precise_bbcode.fields import BBCodeTextField
from django.db import models
import io
import os


class God(models.Model):
    name = models.CharField(blank=True, max_length=50, default='Аноним', verbose_name='Имя')
    content = BBCodeTextField(max_length=15000, verbose_name='Содержимое')
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата', null=True)

    class Meta:
        abstract = True


class Board(models.Model):
    name = models.TextField()
    letter = models.TextField(max_length=3, unique=True)

    class Meta:
        verbose_name = 'Доска'
        verbose_name_plural = 'Доски'

    def __str__(self):
        return self.name


class Thread(God):
    title = models.TextField(max_length=150, verbose_name='Название треда')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='Доска')

    class Meta:
        verbose_name = 'Тред'
        verbose_name_plural = 'Треды'


class Post(God):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, verbose_name='Тред', related_name='Post.thread+')
    sage = models.BooleanField(verbose_name='SAGE', default=False)
    op_mark = models.BooleanField(verbose_name='ОП треда', default=False)

    def reply(self):
        pass

    # TODO: MAKE REPLIES

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class File(models.Model):
    file = models.FileField(blank=True, verbose_name='Файлы',
                            validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg',
                                                                                   'mp4', 'webm'])])

    def resolution(self):
        width, height = get_image_dimensions(self.file.file)
        return str(width) + 'x' + str(height)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension

    class Meta:
        abstract = True


class FilePost(File):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл поста'
        verbose_name_plural = 'Файлы постов'


class FileThread(File):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Файл треда'
        verbose_name_plural = 'Файлы тредов'
