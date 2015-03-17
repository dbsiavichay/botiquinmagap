# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidad',
            field=models.DecimalField(max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
    ]
