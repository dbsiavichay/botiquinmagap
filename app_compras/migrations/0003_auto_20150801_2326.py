# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_compras', '0002_auto_20150317_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallecompra',
            options={'verbose_name': 'detalle de compra', 'verbose_name_plural': 'detalles de compra'},
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='compra',
            field=models.ForeignKey(related_name='detalles', to='app_compras.Compra'),
            preserve_default=True,
        ),
    ]
