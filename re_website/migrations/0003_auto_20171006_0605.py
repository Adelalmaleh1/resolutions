# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-06 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('re_website', '0002_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='organisation',
            new_name='organization',
        ),
    ]
