# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_localizacion', '0003_auto_20150801_2326'),
        ('app_botiquin', '0002_auto_20150801_2326'),
        ('app_inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caducidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('cantidad', models.DecimalField(max_digits=7, decimal_places=2)),
                ('asociacion', models.ForeignKey(to='app_localizacion.Asociacion')),
                ('producto', models.ForeignKey(to='app_botiquin.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='caducado',
            name='detalleCompra',
        ),
        migrations.RemoveField(
            model_name='caducado',
            name='inventario',
        ),
        migrations.DeleteModel(
            name='Caducado',
        ),
        migrations.RemoveField(
            model_name='kardex',
            name='asociacion',
        ),
        migrations.RemoveField(
            model_name='kardex',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Kardex',
        ),
    ]
