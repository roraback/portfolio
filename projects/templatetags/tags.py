from django import template
from django.core.urlresolvers import reverse
from django.db.models import Q
from random import randint

from projects.models import Project
from blog.models import Article, BlogCategory, BlogTag

register = template.Library()

@register.simple_tag
def random_project():
    project = Project.objects.all()[randint(0, Project.objects.count() - 1)]
    project_url = reverse('project', kwargs={'slug':project.slug})
    return project_url
    
@register.inclusion_tag('blog/nav/related_posts.html')
def related_posts(article, number=3):
    """
    Return posts related to the current article
    """
    tag_list = Q()
    for tag in article.tags.all():
        tag_list = tag_list | Q(tags = tag)
    articles_by_tag = Article.objects.filter(tag_list).exclude(id=article.id).distinct()[0:number]
    articles_by_category = article.category.article_set.filter(published=True).exclude(id=article.id).order_by('-posted')[0:number]
    return {
        'current_article': article,
        'articles_by_category': articles_by_category,
        'articles_by_tag': articles_by_tag
    }

@register.inclusion_tag('blog/nav/categories.html')
def blog_categories():
    """
    Return a list of all categories
    """
    return {
        'categories': BlogCategory.objects.filter(article__published=True).distinct().order_by('rank')
    }

@register.inclusion_tag('blog/nav/tags.html')
def blog_tags():
    """
    Return a list of all tags
    """
    return {
        'tags': BlogTag.objects.filter(article__published=True).distinct().order_by('rank')
    }
