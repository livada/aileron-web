# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='card_avatar',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Member'),
        ),
    ]
