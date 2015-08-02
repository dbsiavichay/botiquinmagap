# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventario', '0002_auto_20150801_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caducidad',
            options={'verbose_name': 'Caducidad', 'verbose_name_plural': 'Caducidad'},
        ),
        migrations.AddField(
            model_name='inventario',
            name='cantidad_inicial',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inventario',
            name='es_inicial',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
