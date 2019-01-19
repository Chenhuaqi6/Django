# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-17 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterField(
            model_name='users',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='活动用户'),
        ),
        migrations.AlterField(
            model_name='users',
            name='uemail',
            field=models.CharField(max_length=245, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='users',
            name='uname',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
        migrations.AlterModelTable(
            name='users',
            table='user',
        ),
    ]
