from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def home(request):
    context = {
        "articles" : Article.objects.published().order_by("-publish")
    }
    return render(request, "blog/index.html", context)

def detail(request, slug):
    context = {
        "article" : get_object_or_404(Article.objects.published(), slug = slug)
    }
    return render(request, "blog/detail.html", context)

def blog(request):
    context = {
        "articles" : Article.objects.published().order_by("-publish")
    }
    return render(request, "blog/blog.html", context)

def category(request, slug):
    context = {
        "category" : get_object_or_404(Category, slug = slug, status = True)
    }
    return render(request, "blog/category.html", context)