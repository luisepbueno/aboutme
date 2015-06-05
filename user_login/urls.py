from django.conf.urls import patterns, include, url
#from django.contrib import admin
from user_login import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aboutme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.login_page, name='login_page'),
    
    url(r'^$', views.user_login, name='user_login'),
)
