# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abrechnung', '0002_auto_20171114_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rechnung',
            name='leistung',
            field=models.CharField(max_length=200),
        ),
    ]
