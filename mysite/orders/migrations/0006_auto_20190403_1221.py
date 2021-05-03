# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-03 06:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orders_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user',
        ),
        migrations.AddField(
            model_name='orders',
            name='Bookingdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
