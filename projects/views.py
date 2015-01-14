from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse

from projects.models import Category, Project

class IndexView(ListView):
    model = Category
    template_name = 'index.html'

class ProjectView(DetailView):
    model = Project
    template_name = 'project.html'
    
    def post(self, request, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("success")
            else:
                return HttpResponse("It Looks like this account is disabled.")
        else:
            return HttpResponse("Your username/password is incorrect. Please try again.")

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class SitemapView(ListView):
    model = Project
    template_name="sitemap.xml"