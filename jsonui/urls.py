from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^notifications$', 'jsonui.views.notifications', name='notifications'),
    url(r'^forbidden$', 'jsonui.views.forbidden', name='forbidden'),
)
