# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171014_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='when',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.When'),
        ),
    ]