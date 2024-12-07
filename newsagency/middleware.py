from django.shortcuts import redirect
from django.urls import reverse
import re

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_management_paths = [
            '/user_management/', 
            '/user_management/users/', 
            '/user_management/users/create/'
        ]
        article_create_path = reverse('news:article_create')
        article_edit_pattern = re.compile(r'^/article/edit/\d+/$')

        if request.user.is_authenticated:
            if request.user.is_reader:
                if any(request.path.startswith(path) for path in user_management_paths):
                    return redirect('management:user_list')  
                elif article_edit_pattern.match(request.path) or request.path == article_create_path:
                    return redirect('news:index')

            if request.user.is_editor and not request.user.is_superuser:
                if any(request.path.startswith(path) for path in user_management_paths):
                    return redirect('news:index') 

        response = self.get_response(request)
        return response