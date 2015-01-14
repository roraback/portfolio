from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.core.urlresolvers import reverse

from projects.models import Category, Project

class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    
    def dispatch(self, *args, **kwargs):
        if 'section' in self.request.GET:
            section = self.request.GET["section"]
            
            if section == 'about':
                return HttpResponsePermanentRedirect(reverse('about'))
            elif section == 'contact':
                return HttpResponsePermanentRedirect(reverse('contact'))
            else:
                return super(IndexView, self).dispatch(*args, **kwargs)
        elif 'project' in self.request.GET:
            project = self.request.GET["project"]

            if project == 'mfadtsymposium':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=18).slug}))
            elif project == 'globalbillboard':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=17).slug}))
            elif project == 'costofhcv':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=24).slug}))
            elif project == 'hrmap':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=10).slug}))
            elif project == 'explodingtwitbird':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=15).slug}))
            elif project == 'tweetstalker':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=25).slug}))
            elif project == 'bigbook':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=6).slug}))
            elif project == 'ehrntemplates':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=11).slug}))
            elif project == 'ehrnstyleguide':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=12).slug}))
            elif project == 'emmanuel':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=14).slug}))
            elif project == 'benpowell':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=3).slug}))
            elif project == '3x3':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=4).slug}))
            elif project == 'bicycle':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=5).slug}))
            elif project == 'psychosis_text':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=22).slug}))
            elif project == 'psychosis_design':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=21).slug}))
            elif project == 'psychosis_direction':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=20).slug}))
            elif project == 'ecity':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=13).slug}))
            elif project == 'readingroom':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=23).slug}))
            elif project == 'designstudio':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=1).slug}))
            elif project == 'wolfgangweingart':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=26).slug}))
            elif project == 'expressivetype':
                return HttpResponseRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=16).slug}))
            else:
                return super(IndexView, self).dispatch(*args, **kwargs)
        else:
            return super(IndexView, self).dispatch(*args, **kwargs)

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