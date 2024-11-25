from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/edit/<int:id>/', views.article_edit, name='article_edit'),
    path('article/delete/<int:id>/', views.article_delete, name='article_delete'),
    path('comment/new/', views.comment_create, name='comment_create'),
]