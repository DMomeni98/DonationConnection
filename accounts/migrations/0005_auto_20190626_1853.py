# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190626_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='national_code',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=0),
        ),
        migrations.AddField(
            model_name='member',
            name='post_code',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=0),
        ),
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='timestamp',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
