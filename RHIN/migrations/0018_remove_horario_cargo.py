# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RHIN', '0017_auto_20170428_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='cargo',
        ),
    ]