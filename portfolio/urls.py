from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.conf import settings
from projects.views import IndexView, ProjectView, AboutView, ContactView, SitemapView, BingView
from blog.views import ArticleView, ArticleListView, BlogTagView, BlogCategoryView, BlogIndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/(?P<slug>[A-Za-z0-9_\-]+)/$', ProjectView.as_view(), name='project'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^sitemap\.xml$', SitemapView.as_view(), name='sitemap'),
    url(r'^BingSiteAuth\.xml$', BingView.as_view(), name='bing'),
    url(r'^blog/$', BlogIndexView.as_view(), name='article_list'),
    url(r'^blog/articles/(?P<category_slug>[A-Za-z0-9_\-]+)/(?P<slug>[A-Za-z0-9_\-]+)/$', ArticleView.as_view(), name='article'),
    url(r'^blog/categories/(?P<slug>[A-Za-z0-9_\-]+)/$', BlogCategoryView.as_view(), name='category'),
    url(r'^blog/tags/(?P<slug>[A-Za-z0-9_\-]+)/$', BlogTagView.as_view(), name='tag'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Resume redirect from old site's URL to home
urlpatterns += url(r'^kenneth_roraback_resume.pdf$', RedirectView.as_view(url=reverse('home')), name="resume_redirect"),
