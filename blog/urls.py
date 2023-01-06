from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('blog', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('projects/', views.ArticleList.as_view(), name='article'),
    path('projects/<slug:slug>/', views.ArticleContent.as_view(), name='article_detail'),
]
