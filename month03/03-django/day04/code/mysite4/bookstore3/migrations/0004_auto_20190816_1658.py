# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-16 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore3', '0003_auto_20190816_1657'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author3',
            table='myauthor3',
        ),
        migrations.AlterModelTable(
            name='book3',
            table='mybook3',
        ),
    ]
