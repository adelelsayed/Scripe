# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snomed',
            fields=[
                ('ide', models.AutoField(primary_key=True, serialize=False)),
                ('synonym', models.CharField(max_length=255)),
            ],
        ),
    ]