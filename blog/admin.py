# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article,Author



# class   TagAdmin(admin.ModelAdmin):
#     list_display = ('tag_name')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','category')
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','desc')
#Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
