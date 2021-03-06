from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.zanryu.views.index'),
    url(r'^insert/', 'mysite.zanryu.views.insert'),
    #server
     url(r'^static/(?P<path>/*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),

    #url(r'^static/(?P<path>/*)$', 'django.views.static.serve',{'document_root':settings.STATICFILES_DIRS}),
)
#local
#urlpatterns += staticfiles_urlpatterns()
