from django.contrib.auth import views as auth_views
from django.urls import path

class CustomLogoutView(auth_views.LogoutView):
    next_page = '/'