from django.conf.urls import patterns, include, url
from django.contrib import admin

from projects.views import IndexView, ProjectView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/(?P<slug>[A-Za-z0-9_\-]+)/$', ProjectView.as_view(), name='project'),
)
