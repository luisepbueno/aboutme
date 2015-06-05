from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'user_profile.views.user_profile', name='user_profile'),
)
