# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_localizacion', '0002_auto_20150320_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asociacion',
            options={'verbose_name': 'asociacion', 'verbose_name_plural': 'asociaciones'},
        ),
        migrations.AlterModelOptions(
            name='canton',
            options={'verbose_name': 'canton', 'verbose_name_plural': 'cantones'},
        ),
        migrations.AlterModelOptions(
            name='sector',
            options={'verbose_name': 'sector', 'verbose_name_plural': 'sectores'},
        ),
    ]
