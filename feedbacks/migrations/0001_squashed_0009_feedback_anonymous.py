# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'feedbacks', '0001_initial'), (b'feedbacks', '0002_feedback_poster_id'), (b'feedbacks', '0003_feedback_target_id'), (b'feedbacks', '0004_auto_20150513_0047'), (b'feedbacks', '0005_auto_20150513_0057'), (b'feedbacks', '0006_feedback_deleted'), (b'feedbacks', '0007_feedback_seen_by'), (b'feedbacks', '0008_auto_20150530_1453'), (b'feedbacks', '0009_feedback_anonymous')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('post_date', models.DateField(default=datetime.datetime.now)),
                ('approved', models.BooleanField(default=False)),
                ('poster', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deleted', models.BooleanField(default=False)),
                ('seen_by', models.ManyToManyField(related_name='feedback_seen_by', to=settings.AUTH_USER_MODEL)),
                ('anonymous', models.BooleanField(default=True)),
            ],
        ),
    ]
