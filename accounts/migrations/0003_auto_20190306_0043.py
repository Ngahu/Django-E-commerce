# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-05 21:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestemail',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Guest User', 'verbose_name_plural': 'Guest Users'},
        ),
    ]
