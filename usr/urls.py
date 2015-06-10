from django.conf.urls import patterns, include, url
#from django.contrib import admin
from usr import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aboutme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.login_page, name='login_page'),
    
    url(r'^login$', views.user_login, name='user_login'),
    url(r'^logout$', views.user_logout, name='user_logout'),
    url(r'^profile$', views.user_profile, name='user_profile'),
    url(r'^register$', views.user_register, name='user_register'),
)
