# Generated by Django 3.2.7 on 2021-09-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collective', '0008_auto_20210923_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataentry',
            name='dropdown1_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='dropdown2_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='float1_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='float2_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='float3_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='float4_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='img_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='int1_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='int2_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='int3_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='int4_label',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]