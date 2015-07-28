from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from .views import IndexView


urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')),
    url(r'^admin/', include(admin.site.urls)),

    # News
    url(r'^news/', include('blanc_basic_news.urls', namespace='blanc_basic_news')),
    url(r'^newstext/news/(?P<year1>\d{4})/(?P<month1>\d{2})/(?P<day1>\d{2})/(?P<slug1>.+)/$', 'django_project.views.NewsText', name='news-text'),

    # Events
    url(r'^events/', include('blanc_basic_events.urls', namespace='blanc_basic_events')),
)

# Serving media under debug
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
