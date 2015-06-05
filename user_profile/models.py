from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    facebook_id = models.IntegerField()
    #user        = models.ForeignKey(User, unique=True)
    user        = models.OneToOneField(User)