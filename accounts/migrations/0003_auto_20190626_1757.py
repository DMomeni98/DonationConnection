# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190626_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='post_code',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=0),
        ),
    ]
