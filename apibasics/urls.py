from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articleList),
    path('articles/<int:pk>/', views.article_detail),
    ]