# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxiTec', '0013_auto_20170411_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxiTec.Owner'),
        ),
    ]
