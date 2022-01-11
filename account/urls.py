from django.contrib.auth import views
from django.urls import path
from .views import ArticleList

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name = "login")
]

urlpatterns += [
    path('', ArticleList.as_view(), name = 'home')
]