# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiTec', '0014_auto_20170411_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='driver',
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone_number_2',
            field=models.CharField(blank=True, default='XXXXXXXXXX', max_length=10),
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]