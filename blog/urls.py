from django.urls import path
from .views import IndexList, ArticleList, ArticleDetail, CategoryList, AuthorList

app_name = "blog"

urlpatterns = [
    path('', IndexList.as_view(), name="home"),
    path('blog/', ArticleList.as_view(), name="blog"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="detail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author")
]