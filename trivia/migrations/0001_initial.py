# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.NullBooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('current_round', models.IntegerField(default=0)),
                ('number_right', models.IntegerField(default=0)),
                ('category_1', models.BooleanField(default=False)),
                ('category_2', models.BooleanField(default=False)),
                ('category_3', models.BooleanField(default=False)),
                ('category_4', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('win_loss', models.NullBooleanField()),
                ('opponent_game', models.ForeignKey(to='trivia.Game')),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('question', models.TextField()),
                ('answer_a', models.TextField()),
                ('answer_b', models.TextField(blank=True, null=True)),
                ('answer_c', models.TextField(blank=True, null=True)),
                ('answer_d', models.TextField(blank=True, null=True)),
                ('correct_answer', models.TextField()),
                ('number', models.DecimalField(decimal_places=2, blank=True, max_digits=9, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.NullBooleanField(default=True)),
                ('category', models.ForeignKey(to='trivia.Category')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='answered_questions',
            field=models.ManyToManyField(to='trivia.Question'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
