# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 02:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0007_object_pk_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logentry',
            name='additional_data',
        ),
    ]
