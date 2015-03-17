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
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(unique=True, max_length=10)),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('precio_unitario', models.DecimalField(max_digits=7, decimal_places=2)),
                ('precio_total', models.DecimalField(max_digits=9, decimal_places=2)),
                ('producto', models.ForeignKey(to='app_botiquin.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsoVenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=5, decimal_places=2)),
                ('detalle_venta', models.ForeignKey(to='app_ventas.DetalleVenta')),
                ('enfermedad', models.ForeignKey(to='app_ventas.Enfermedad')),
                ('especie', models.ForeignKey(to='app_ventas.Especie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('valor_total', models.DecimalField(max_digits=9, decimal_places=2)),
                ('asociacion', models.ForeignKey(to='app_localizacion.Asociacion')),
                ('cliente', models.ForeignKey(to='app_ventas.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(to='app_ventas.Venta'),
            preserve_default=True,
        ),
    ]
