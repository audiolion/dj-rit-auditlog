# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 02:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0008_remove_logentry_additional_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='additional_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='additional data'),
        ),
    ]