# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_botiquin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupoproducto',
            options={'verbose_name': 'grupo de producto', 'verbose_name_plural': 'grupos de producto'},
        ),
        migrations.AlterModelOptions(
            name='medidaproducto',
            options={'verbose_name': 'medida de producto', 'verbose_name_plural': 'medidas de producto'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AlterModelOptions(
            name='tipoproducto',
            options={'verbose_name': 'tipo de producto', 'verbose_name_plural': 'tipos de producto'},
        ),
    ]
