# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='follower_list',
        ),
        migrations.RemoveField(
            model_name='author',
            name='following_list',
        ),
        migrations.RemoveField(
            model_name='author',
            name='randomly_following',
        ),
    ]
