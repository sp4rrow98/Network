# Generated by Django 3.2.9 on 2021-12-27 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0022_auto_20211227_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='people_who_liked',
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 22, 40, 40, 319512)),
        ),
    ]
