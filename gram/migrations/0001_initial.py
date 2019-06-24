# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 09:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.ImageField(default='', upload_to='posts/')),
                ('img_title', models.CharField(max_length=60)),
                ('img_caption', tinymce.models.HTMLField(blank=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('insta_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(default='', upload_to='profile_pictures/')),
                ('user_bio', models.CharField(blank=True, max_length=200)),
                ('user_profile', models.IntegerField(default=0)),
            ],
        ),
    ]