# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-16 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190216_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerregistration',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.manufacturerRegistration'),
        ),
    ]
