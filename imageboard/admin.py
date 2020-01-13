from django.contrib import admin
from django import forms
from django.urls import reverse
from django.db import models
from .models import Thread, Board, Post, FilePost, FileThread


@admin.register(FilePost, FileThread)
class AuthorAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'thread', 'date')
    search_fields = ('content', 'title')
    fields = ('name', 'content', 'thread', ('sage', 'op_mark'), 'date')
    readonly_fields = ('date',)


class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'letter')


class ThreadAdmin(admin.ModelAdmin):
    fields = ('name', 'board', 'title', 'content', 'date')
    list_display = ('__str__', 'title', 'date')
    readonly_fields = ('date',)


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Board, BoardAdmin)
admin.site.register(Thread, ThreadAdmin)
