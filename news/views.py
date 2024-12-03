from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

@login_required(login_url='/user_management/login/')
def index(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    return render(request, 'news/article_detail.html', {'article': article, 'comments': comments})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('index')
    else:
        form = ArticleForm()
    return render(request, 'news/article_form.html', {'form': form})

@login_required
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', id=id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news/article_form.html', {'form': form})

@login_required
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('index')
    return render(request, 'news/article_confirm_delete.html', {'article': article})

@login_required
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('article_detail', id=comment.article.id)
    return redirect('index')