# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_music', '0014_auto_20180411_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgenre',
            name='name',
            field=models.CharField(db_column='subname', max_length=50),
        ),
    ]
