# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RHIN', '0021_auto_20170428_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='sal',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='horario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RHIN.Horario'),
            preserve_default=False,
        ),
    ]