# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planning', to='login_reg.User')),
            ],
            managers=[
                ('ApptManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
