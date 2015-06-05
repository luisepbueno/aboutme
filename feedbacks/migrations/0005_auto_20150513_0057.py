# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0004_auto_20150513_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='post_data',
            new_name='post_date',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='poster_id',
            new_name='poster',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='target_id',
            new_name='target',
        ),
    ]
