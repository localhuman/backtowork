# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20170116_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepliedTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.BigIntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='previoustweet',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='previoustweet',
            name='author',
        ),
        migrations.DeleteModel(
            name='TwitterUser',
        ),
        migrations.DeleteModel(
            name='PreviousTweet',
        ),
    ]
