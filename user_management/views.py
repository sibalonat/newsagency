from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login, authenticate
from news.models import User

from .forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect

@login_required(login_url=reverse_lazy('management:login'))
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_management/user_list.html', {'users': users})

@login_required(login_url=reverse_lazy('management:login'))
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.is_editor = not user.is_editor
        user.is_reader = not user.is_reader
        user.save()
        return redirect('management:user_detail', user_id=user.id)
    return render(request, 'user_management/user_detail.html', {'user': user})

@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.is_superuser:
                return redirect('management:user_list')
            else:
                return redirect('news:article_create')
    else:
        form = AuthenticationForm(request)
    return render(request, 'user_management/login.html', {'form': form})

@login_required(login_url=reverse_lazy('management:login'))
def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            form = UserCreationForm()
            return redirect('management:user_list')
    else:
        form = UserCreationForm()
    return render(request, 'user_management/user_create.html', {'form': form})

@login_required(login_url=reverse_lazy('management:login'))
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('management:user_list')
    return render(request, 'user_management/user_confirm_delete.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_reader = True
            user.save()
            
            auth_login(request, user) 
            return redirect('news:index')
    else:
        form = UserCreationForm()
    return render(request, 'user_management/register.html', {'form': form})
