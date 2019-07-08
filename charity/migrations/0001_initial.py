# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('phone_number', models.DecimalField(null=True, max_digits=11, decimal_places=0)),
                ('post_code', models.DecimalField(null=True, max_digits=10, decimal_places=0)),
            ],
        ),
    ]
