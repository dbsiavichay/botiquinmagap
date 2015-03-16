# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MedidaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('compuesto', models.CharField(max_length=256, null=True, blank=True)),
                ('presentacion', models.CharField(max_length=64, null=True, blank=True)),
                ('precio_referencial', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('registro_sanitario', models.CharField(max_length=64, null=True, blank=True)),
                ('grupo', models.ForeignKey(to='app_botiquin.GrupoProducto')),
                ('medida', models.ForeignKey(to='app_botiquin.MedidaProducto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(to='app_botiquin.TipoProducto'),
            preserve_default=True,
        ),
    ]
