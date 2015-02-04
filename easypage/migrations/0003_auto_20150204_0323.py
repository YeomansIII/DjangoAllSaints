# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypage', '0002_auto_20150204_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to=b'assets/image/carousel/'),
        ),
        migrations.AlterField(
            model_name='quicklink',
            name='image',
            field=models.ImageField(upload_to=b'assets/image/quicklinks/'),
        ),
    ]
