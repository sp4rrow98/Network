# Generated by Django 4.0 on 2022-01-04 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0028_auto_20211228_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 4, 7, 47, 53, 705057)),
        ),
    ]
