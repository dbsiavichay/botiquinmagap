# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_localizacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asociacion',
            old_name='cordenadax',
            new_name='latitud',
        ),
        migrations.RenameField(
            model_name='asociacion',
            old_name='cordenaday',
            new_name='longitud',
        ),
    ]
