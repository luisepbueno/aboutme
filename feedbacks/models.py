from django.db import models
from django.contrib.auth.models import User
import datetime

class Feedback(models.Model):
    message     = models.TextField()
    poster      = models.ForeignKey(User)
    target      = models.ForeignKey(User, related_name='+') # nao sei o por que desse +, mas funcionou
    post_date   = models.DateField(default=datetime.datetime.now)
    anonymous   = models.BooleanField(default=True)
    approved    = models.BooleanField(default=False)
    deleted     = models.BooleanField(default=False)
    seen_by     = models.ManyToManyField(User, related_name='feedback_seen_by')