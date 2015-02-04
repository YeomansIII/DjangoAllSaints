# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypage', '0004_auto_20150204_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ForeignKey(to='assets.Image'),
        ),
        migrations.AlterField(
            model_name='quicklink',
            name='image',
            field=models.ForeignKey(to='assets.Image'),
        ),
    ]
