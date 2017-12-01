# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20171201_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='province',
            field=models.CharField(blank=True, default=b'', max_length=96),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, default=b'', max_length=96),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, default=b'', max_length=96),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(blank=True, default=b'', max_length=96),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='owner',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]