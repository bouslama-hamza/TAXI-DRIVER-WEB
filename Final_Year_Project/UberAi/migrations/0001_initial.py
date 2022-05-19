# Generated by Django 3.1.12 on 2022-05-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
            ],
        ),
    ]
