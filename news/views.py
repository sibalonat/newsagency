from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Article, Comment
from django.core.paginator import Paginator
from .forms import ArticleForm, CommentForm


def index(request):
    articles = Article.objects.all().order_by('-updated_at')
    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/index.html', {'page_obj': page_obj})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('article_detail', id=id)
    else:
        form = CommentForm()
    return render(request, 'news/article_detail.html', {'article': article, 'comments': comments, 'form': form})

@login_required(login_url='/user_management/login/')
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('news:index')
    else:
        form = ArticleForm()
    return render(request, 'news/article_form.html', {'form': form})

@login_required(login_url='/user_management/login/')
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('news:article_detail', id=id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'news/article_form.html', {'form': form})

@login_required(login_url='/user_management/login/')
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('news:index')
    return render(request, 'news/article_confirm_delete.html', {'article': article})

@login_required
def comment_create(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('news:article_detail', id=comment.article.id)
    return redirect('news:index')

def user_articles(request, user_id):
    articles = Article.objects.filter(author_id=user_id).values('id', 'title', 'created_at')
    return JsonResponse(list(articles), safe=False)