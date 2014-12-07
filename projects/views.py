from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from projects.models import Category, Project

class IndexView(ListView):
    model = Category
    template_name = 'index.html'

class ProjectView(DetailView):
    model = Project
    template_name = 'project.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'