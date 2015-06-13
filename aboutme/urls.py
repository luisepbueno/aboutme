from django.conf.urls import patterns, include, url
#from django.conf.urls.i18n import i18n_patterns
#from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'aboutme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^usr/', include('usr.urls')),
    url(r'^friends/', include('friends.urls')),
    url(r'^feedbacks/', include('feedbacks.urls')),
    url(r'^jsonui/', include('jsonui.urls')),
)
