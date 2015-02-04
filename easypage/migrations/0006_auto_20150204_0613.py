# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypage', '0005_auto_20150204_0551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='title',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='carousel',
            old_name='image',
            new_name='image_file',
        ),
        migrations.RenameField(
            model_name='quicklink',
            old_name='title',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='quicklink',
            old_name='image',
            new_name='image_file',
        ),
    ]
