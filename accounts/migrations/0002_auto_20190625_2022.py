# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.AlterModelManagers(
            name='member',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='member',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, default=datetime.datetime(2019, 6, 25, 15, 52, 38, 681340, tzinfo=utc), serialize=False, auto_created=True),
            preserve_default=False,
        ),
    ]
