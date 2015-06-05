# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedbacks', '0002_feedback_poster_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='target_id',
            field=models.ForeignKey(related_name='target_id', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
