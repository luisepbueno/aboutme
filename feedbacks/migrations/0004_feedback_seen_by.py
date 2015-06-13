# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedbacks', '0003_remove_feedback_seen_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='seen_by',
            field=models.ManyToManyField(related_name='feedback_seen_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
