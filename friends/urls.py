from django.conf.urls import patterns, include, url
from friends import views

urlpatterns = patterns('',
    #url(r'^$', views.list_friends, name='list_friends'),
    url(r'^$', 'friends.views.friends', name='friends'),
)
