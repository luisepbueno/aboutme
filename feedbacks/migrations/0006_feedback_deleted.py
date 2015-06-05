# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0005_auto_20150513_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
