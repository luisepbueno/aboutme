from django.conf.urls import patterns, include, url
from jsonui import views

urlpatterns = patterns('',
    url(r'^notifications$', views.notifications, name='notifications'),
    url(r'^forbidden$', views.forbidden, name='forbidden'),
)
