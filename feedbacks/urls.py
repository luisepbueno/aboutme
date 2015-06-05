from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       
    url(r'^$', 'feedbacks.views.feedbacks', name='feedbacks'),
    url(r'^(\d+)/$', 'feedbacks.views.friends_feedbacks', name='friends_feedbacks'),
    url(r'^(\d+)/write$', 'feedbacks.views.write_feedback', name='write_feedbacks'),
    url(r'^(\d+)/publish$', 'feedbacks.views.publish_feedback', name='publish_feedback'),
    url(r'^(\d+)/delete$', 'feedbacks.views.delete_feedback', name='delete_feedback'),
)
