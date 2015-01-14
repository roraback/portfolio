from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from django.conf import settings
from projects.views import IndexView, ProjectView, AboutView, ContactView, SitemapView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/(?P<slug>[A-Za-z0-9_\-]+)/$', ProjectView.as_view(), name='project'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^sitemap\.xml$', SitemapView.as_view(), name='sitemap'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
