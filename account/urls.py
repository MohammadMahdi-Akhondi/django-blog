from django.contrib.auth import views
from django.urls import path
from .views import (
    ArticleList,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    Profile,
    Login,
    PasswordChange,
)

app_name = 'account'

urlpatterns = [
    path('login/', Login.as_view(), name = "login"),
    path('logout/', views.LogoutView.as_view(), name = "logout"),
    path('password_change/', PasswordChange.as_view(), name = "password_change"),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name = "password_chanage_done"),
]

urlpatterns += [
    path('', ArticleList.as_view(), name = 'home'),
    path('article/create', ArticleCreate.as_view(), name = 'article-create'),
    path('article/edit/<int:pk>', ArticleUpdate.as_view(), name = 'article-update'),
    path('article/delete/<int:pk>', ArticleDelete.as_view(), name = 'article-delete'),
    path('profile/', Profile.as_view(), name = 'profile'),
]