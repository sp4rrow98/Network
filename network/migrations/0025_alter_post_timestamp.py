# Generated by Django 3.2.9 on 2021-12-27 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0024_auto_20211227_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 22, 49, 29, 74739)),
        ),
    ]
