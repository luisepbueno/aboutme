from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User
import datetime

class Feedback(models.Model):
    message     = models.TextField()
    #poster      = models.ForeignKey(User)
    poster      = models.ForeignKey(settings.AUTH_USER_MODEL)
    #target      = models.ForeignKey(User, related_name='+') # nao sei o por que desse +, mas funcionou
    target      = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+') # nao sei o por que desse +, mas funcionou
    post_date   = models.DateField(default=datetime.datetime.now)
    anonymous   = models.BooleanField(default=True)
    approved    = models.BooleanField(default=False)
    deleted     = models.BooleanField(default=False)
    #seen_by     = models.ManyToManyField(User, related_name='feedback_seen_by')
    seen_by     = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='feedback_seen_by')