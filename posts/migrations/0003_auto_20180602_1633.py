# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-02 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180602_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 2, 11, 3, 15, 124529, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
