# Generated by Django 3.2.9 on 2021-12-19 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 19, 3, 59, 48, 959607)),
        ),
    ]