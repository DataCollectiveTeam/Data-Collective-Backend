# Generated by Django 3.2.7 on 2021-09-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collective', '0010_datavis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datavis',
            name='chart_title',
            field=models.CharField(max_length=150),
        ),
    ]
