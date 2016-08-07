from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from projects.models import Category, Project

class IndexView(ListView):
    model = Category
    template_name = 'index.html'
    
    # Forward old URLs to correct views
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
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=18).slug}))
            elif project == 'globalbillboard':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=17).slug}))
            elif project == 'firstreaders':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=8).slug}))
            elif project == 'learnwithhomer':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=28).slug}))
            elif project == 'opensansschoolbook':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=19).slug}))
            elif project == 'vulnerabilitymapping':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=27).slug}))
            elif project == 'costofhcv':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=24).slug}))
            elif project == 'hrmap':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=10).slug}))
            elif project == 'explodingtwitbird':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=15).slug}))
            elif project == 'tweetstalker':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=25).slug}))
            elif project == 'bigbook':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=6).slug}))
            elif project == 'ehrntemplates':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=11).slug}))
            elif project == 'ehrnstyleguide':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=12).slug}))
            elif project == 'emmanuel':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=14).slug}))
            elif project == 'benpowell':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=3).slug}))
            elif project == '3x3':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=4).slug}))
            elif project == 'bicycle':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=5).slug}))
            elif project == 'psychosis_text':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=22).slug}))
            elif project == 'psychosis_design':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=21).slug}))
            elif project == 'psychosis_direction':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=20).slug}))
            elif project == 'ecity':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=13).slug}))
            elif project == 'readingroom':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=23).slug}))
            elif project == 'designstudio':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=1).slug}))
            elif project == 'wolfgangweingart':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=26).slug}))
            elif project == 'expressivetype':
                return HttpResponsePermanentRedirect(reverse('project', kwargs={'slug':Project.objects.get(pk=16).slug}))
            else:
                return super(IndexView, self).dispatch(*args, **kwargs)
        else:
            return super(IndexView, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['randomPopOrder'] = ('pop-zero', 'pop-one', 'pop-two', 'pop-three', 'pop-four', 'pop-five', 'pop-six', 'pop-seven', 'pop-eight', 'pop-nine', )
        return context

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
    template_name ="xml/sitemap.xml"

class BingView(TemplateView):
    template_name = "xml/BingSiteAuth.xml"