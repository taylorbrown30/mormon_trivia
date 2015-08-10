# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20150808_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='my_turn',
            field=models.BooleanField(default=False),
        ),
    ]
