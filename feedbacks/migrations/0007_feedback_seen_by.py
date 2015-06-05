# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedbacks', '0006_feedback_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='seen_by',
            field=models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
