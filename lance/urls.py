from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^healthierhabits/', include( 'healthierhabits.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
