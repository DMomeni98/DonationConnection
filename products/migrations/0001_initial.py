# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('charity', models.CharField(max_length=200, db_index=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('overview', models.TextField(blank=True)),
                ('picture', models.ImageField(upload_to='static/images/')),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('stock', models.DecimalField(max_digits=10, decimal_places=0)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
