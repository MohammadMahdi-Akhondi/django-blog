from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Article, Category

# def home(request):
#     context = {
#         "articles" : Article.objects.published().order_by("-publish")
#     }
#     return render(request, "blog/index.html", context)

class IndexList(ListView):
    queryset =  Article.objects.published().order_by("-publish")
    template_name = "blog/index_list.html"
    paginate_by = 6


class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug = slug)


class ArticleList(ListView):
    queryset = Article.objects.published().order_by("-publish")
    paginate_by = 6


class CategoryList(ListView):
    paginate_by = 6
    template_name = 'blog/category_list.html'
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug = slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context