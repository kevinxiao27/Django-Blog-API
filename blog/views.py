from django.views import generic
from .models import Post, Article
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'article.html'

class ArticleContent(generic.DetailView):
    model = Article
    template_name = 'article_detail.html'