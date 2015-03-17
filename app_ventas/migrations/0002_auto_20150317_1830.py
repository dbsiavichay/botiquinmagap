# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='cantidad',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usoventa',
            name='cantidad',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
