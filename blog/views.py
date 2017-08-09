# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Article,Author
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    post = Article.objects.all()
    return render(request,'index.html',{'post':post})

def about(request):
    author = Author.objects.all()
    return render(request,'about.html',{'author':author})
def article(request,article_id):
    article = Article.objects.get(id = article_id)
    return render(request,'view.html',{'article':article})

def article_about(request):
    author = Author.objects.all()
    return render(request,about.html,{'author':author})

# def listing(request,part_page):
#     article_list = Article.objects.all()
#     paginator = Paginator(article_list,3)
#     page = request.GET.get(page = part_page)
#     try:
#         part_list = paginator.page(page)
#     except PageNotAnInteger:
#         part_list = paginator.page(1)
#     except EmptyPage:
#         part_list = paginator.page(paginator.num_pages)
#     return render(request,'index.html',{'part_list':part_list})
