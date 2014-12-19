from django import template
from django.core.urlresolvers import reverse
from random import randint

from projects.models import Project

register = template.Library()

@register.simple_tag
def random_project():
    project = Project.objects.all()[randint(0, Project.objects.count() - 1)]
    project_url = reverse('project', kwargs={'slug':project.slug})
    return project_url