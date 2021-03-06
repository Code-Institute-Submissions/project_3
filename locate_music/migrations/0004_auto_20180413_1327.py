# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locate_music', '0003_auto_20180413_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(help_text='What is happening at the event?', max_length=800),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text='Name of the event.', max_length=50),
        ),
    ]
