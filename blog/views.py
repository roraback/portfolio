from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from blog.models import Article

# Create your views here.
class ArticleView(DetailView):
    model = Article
    template_name = 'article.html'
