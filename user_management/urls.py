from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('login/', views.custom_login, name='login'),
    path('users/create/', views.user_create, name='user_create'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]