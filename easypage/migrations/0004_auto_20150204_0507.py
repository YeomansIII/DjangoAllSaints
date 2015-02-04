# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypage', '0003_auto_20150204_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicklink',
            name='button_text',
            field=models.CharField(default='View details \xbb', max_length=20),
        ),
    ]
