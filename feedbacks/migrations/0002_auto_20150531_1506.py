# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_squashed_0009_feedback_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='poster',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
