# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0008_auto_20150530_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='anonymous',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
