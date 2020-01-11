from django.contrib import admin
from .models import Thread, Board, Post, FilePost, FileThread


@admin.register(Thread, Board, Post, FilePost, FileThread)
class AuthorAdmin(admin.ModelAdmin):
    pass
