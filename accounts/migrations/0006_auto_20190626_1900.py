# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190626_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 14, 30, 37, 503338, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 14, 30, 48, 392842, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
