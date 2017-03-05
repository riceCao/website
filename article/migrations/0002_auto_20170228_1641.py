# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='最后更新时间'),
        ),
    ]
