from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
# from .views import CustomLogoutView

urlpatterns = [
    # path('news/', include('news.urls')),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('login/', views.custom_login, name='login'),
    path('users/create/', views.user_create, name='user_create'), 
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
]