# Generated by Django 3.2.9 on 2021-12-27 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_auto_20211227_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likes',
            old_name='owner',
            new_name='likes',
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 27, 22, 44, 27, 949835)),
        ),
    ]
