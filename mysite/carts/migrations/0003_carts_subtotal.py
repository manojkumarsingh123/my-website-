# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-31 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20190330_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
