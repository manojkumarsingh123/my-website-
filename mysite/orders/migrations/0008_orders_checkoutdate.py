# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-03 07:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190403_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='checkoutdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
