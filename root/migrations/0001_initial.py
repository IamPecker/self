# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('small', '小包'), ('middle', '中包'), ('large', '大包')], max_length=10, verbose_name='种类')),
                ('is_use', models.BooleanField(verbose_name='占用')),
                ('time_use', models.DateTimeField(verbose_name='时间')),
            ],
        ),
    ]
