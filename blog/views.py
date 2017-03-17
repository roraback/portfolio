from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from blog.models import Article, BlogCategory, BlogTag

# Create your views here.
class ArticleView(DetailView):
    model = Article
    template_name = 'blog/article.html'

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'

class BlogCategoryView(DetailView):
    model = BlogCategory
    template_name = 'blog/category.html'

    # def get_context_data(self, **kwargs):
    #      context = super(BlogCategoryView, self).get_context_data(**kwargs)
    #      context.update({
    #          'articles': Article.objects.filter(article__published=True, article__category=category).order_by('rank')
    #      })
 
class BlogTagView(DetailView):
    model = BlogTag
    template_name = 'blog/tag.html'

class BlogIndexView(ListView):
    queryset = Article.objects.filter(published=True)
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super(BlogIndexView, self).get_context_data(**kwargs)
        context.update({
            'categories': BlogCategory.objects.filter(article__published=True).order_by('rank'),
            'blog_tags': BlogTag.objects.filter(article__published=True).order_by('rank')
        })
        return context     
        