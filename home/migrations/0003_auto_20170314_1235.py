# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170314_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practical_test',
            name='image',
            field=models.ImageField(upload_to=b'\\Users\\guptaane\\PycharmProjects\\homeania\\home\\static\\media'),
        ),
    ]
