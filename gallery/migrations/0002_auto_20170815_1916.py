# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery_img',
            old_name='img_name',
            new_name='img',
        ),
    ]