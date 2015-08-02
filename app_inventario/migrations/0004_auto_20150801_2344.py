# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventario', '0003_auto_20150801_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='cantidad_inicial',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
