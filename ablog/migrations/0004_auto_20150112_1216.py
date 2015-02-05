# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0003_auto_20150109_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['created'], 'verbose_name': 'Blog Entrdqsdqsy', 'verbose_name_plural': 'Blog Entriessd'},
        ),
    ]
