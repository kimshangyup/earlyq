# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
