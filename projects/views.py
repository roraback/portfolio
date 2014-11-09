from django.shortcuts import render
from django.views.generic import ListView

from projects.models import Category

class IndexView(ListView):
    model = Category
    template_name = 'index.html'