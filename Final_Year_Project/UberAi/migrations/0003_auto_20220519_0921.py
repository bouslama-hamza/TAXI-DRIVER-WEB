# Generated by Django 3.1.12 on 2022-05-19 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UberAi', '0002_taxi_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxi',
            name='time_end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='time_start',
            field=models.TimeField(),
        ),
    ]
