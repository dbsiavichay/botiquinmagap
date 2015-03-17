# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_compras', '0001_initial'),
        ('app_botiquin', '0001_initial'),
        ('app_localizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caducado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('fecha', models.DateField()),
                ('detalleCompra', models.ForeignKey(to='app_compras.DetalleCompra')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('valor_unitario', models.DecimalField(max_digits=7, decimal_places=2)),
                ('asociacion', models.ForeignKey(to='app_localizacion.Asociacion')),
                ('producto', models.ForeignKey(to='app_botiquin.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('tipo_transaccion', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=256)),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('valor_unitario', models.DecimalField(max_digits=7, decimal_places=2)),
                ('saldo', models.DecimalField(max_digits=7, decimal_places=2)),
                ('asociacion', models.ForeignKey(to='app_localizacion.Asociacion')),
                ('producto', models.ForeignKey(to='app_botiquin.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='caducado',
            name='inventario',
            field=models.ForeignKey(to='app_inventario.Inventario'),
            preserve_default=True,
        ),
    ]
