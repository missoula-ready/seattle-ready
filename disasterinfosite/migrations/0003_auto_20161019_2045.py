# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0002_auto_20161003_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasteventsphoto',
            name='caption',
            field=models.TextField(max_length=500, default=''),
        ),
    ]
