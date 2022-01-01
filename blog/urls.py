from django.urls import path
from .views import home, blog, detail

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('blog/', blog, name="blog"),
    path('article/<slug:slug>', detail, name="detail")
]