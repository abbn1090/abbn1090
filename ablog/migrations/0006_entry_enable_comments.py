# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0005_auto_20150206_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='enable_comments',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
