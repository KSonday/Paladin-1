# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0022_auto_20160824_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attorney_list',
            name='Last_Visited',
        ),
    ]
