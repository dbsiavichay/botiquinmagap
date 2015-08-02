# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_ventas', '0002_auto_20150317_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleventa',
            options={'verbose_name': 'detalle de venta', 'verbose_name_plural': 'detalles de venta'},
        ),
        migrations.AlterModelOptions(
            name='enfermedad',
            options={'verbose_name': 'enfermedad', 'verbose_name_plural': 'enfermedades'},
        ),
        migrations.AlterModelOptions(
            name='usoventa',
            options={'verbose_name': 'uso de venta', 'verbose_name_plural': 'usos de venta'},
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(related_name='detalles', to='app_ventas.Venta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usoventa',
            name='detalle_venta',
            field=models.ForeignKey(related_name='usos', to='app_ventas.DetalleVenta'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(related_name='data_cliente', to='app_ventas.Cliente'),
            preserve_default=True,
        ),
    ]
