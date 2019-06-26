# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190626_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='address',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='member',
            name='national_code',
        ),
        migrations.RemoveField(
            model_name='member',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
    ]
