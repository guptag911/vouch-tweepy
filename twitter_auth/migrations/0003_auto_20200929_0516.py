# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-09-29 05:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_auth', '0002_tweets_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='name',
            field=models.CharField(default=datetime.datetime(2020, 9, 29, 5, 16, 11, 280536, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweets',
            name='tweet_id',
            field=models.CharField(default=datetime.datetime(2020, 9, 29, 5, 16, 20, 718010, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
