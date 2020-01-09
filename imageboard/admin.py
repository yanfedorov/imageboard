from django.contrib import admin
from .models import Thread, Board, Post, FilePost, FileThread

admin.site.register(Thread)
admin.site.register(Board)
admin.site.register(Post)
admin.site.register(FilePost)
admin.site.register(FileThread)
