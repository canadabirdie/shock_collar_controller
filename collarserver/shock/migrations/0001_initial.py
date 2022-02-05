# Generated by Django 4.0.1 on 2022-01-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControllerState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_press_time', models.FloatField(default=0)),
                ('power_level', models.IntegerField(default=0)),
            ],
        ),
    ]
