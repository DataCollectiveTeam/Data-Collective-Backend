# Generated by Django 3.2.7 on 2021-09-22 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collective', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='account_updated',
        ),
        migrations.RemoveField(
            model_name='project',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='citizen',
            name='account_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
