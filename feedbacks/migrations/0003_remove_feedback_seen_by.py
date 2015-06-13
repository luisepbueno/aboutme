# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0002_auto_20150531_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='seen_by',
        ),
    ]
