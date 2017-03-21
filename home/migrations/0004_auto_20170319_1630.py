# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170314_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('correct_option', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Second_level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('correct_option', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Third_level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('correct_option', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='practical_test',
            name='image',
            field=models.ImageField(max_length=2000, upload_to=b'C:\\Users\\guptaane\\PycharmProjects\\Homeania-Photocert\\Homeania-Photocert\\home\\static\\media'),
        ),
    ]
