# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_botiquin', '0001_initial'),
        ('app_localizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('valor_total', models.DecimalField(max_digits=9, decimal_places=2)),
                ('asociacion', models.ForeignKey(to='app_localizacion.Asociacion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('costo_unitario', models.DecimalField(max_digits=7, decimal_places=2)),
                ('costo_total', models.DecimalField(max_digits=9, decimal_places=2)),
                ('compra', models.ForeignKey(to='app_compras.Compra')),
                ('producto', models.ForeignKey(to='app_botiquin.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
