from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from trebnitz.projects.views import news

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trebnitz.views.home', name='home'),
    # url(r'^trebnitz/', include('trebnitz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     url(r'^admin/', include(admin.site.urls)),
     url(r'^news/', news),
     url(r'^static/(?P<path>.*)$', 
         'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT},
         {'show_indexes': True}),
)
