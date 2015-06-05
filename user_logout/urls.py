from django.conf.urls import patterns, include, url
from user_logout import views

urlpatterns = patterns('',
    url(r'^$', views.user_logout, name='logout'),
)
