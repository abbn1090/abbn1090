# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0006_entry_enable_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='enable_comments',
        ),
    ]
