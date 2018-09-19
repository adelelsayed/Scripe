# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-07 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ScripeAlpha', '0002_snomed_initials'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICD',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('synonym', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('initials', models.CharField(max_length=255)),
            ],
        ),
    ]
