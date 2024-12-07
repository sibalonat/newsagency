from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    # path('user_management/', include('user_management.urls')),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/edit/<int:id>/', views.article_edit, name='article_edit'),
    path('article/delete/<int:id>/', views.article_delete, name='article_delete'),
    path('comment/new/', views.comment_create, name='comment_create'),
    path('logout/', LogoutView.as_view(), name='logout'),
]