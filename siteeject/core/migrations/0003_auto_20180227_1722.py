# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 20:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180227_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 27, 20, 22, 3, 717495, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
