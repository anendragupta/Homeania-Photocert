# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practical_test',
            name='image',
            field=models.ImageField(upload_to=b'/home/static/media/'),
        ),
    ]
