from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from news.models import User

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_management/user_list.html', {'users': users})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.is_editor = not user.is_editor
        user.is_reader = not user.is_reader
        user.save()
        return redirect('user_detail', user_id=user.id)
    return render(request, 'user_management/user_detail.html', {'user': user})