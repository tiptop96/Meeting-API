# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20171015_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]