from django.urls import path
from .views import home, blog, detail, category

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('blog/', blog, name="blog"),
    path('article/<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category, name="category")
]