from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'management'

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('login/', views.custom_login, name='login'),
    path('users/create/', views.user_create, name='user_create'), 
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]