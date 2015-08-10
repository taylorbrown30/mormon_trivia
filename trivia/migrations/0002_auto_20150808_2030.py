# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='opponent_game',
            field=models.ForeignKey(to='trivia.Game', null=True),
        ),
    ]
