# Generated by Django 3.2.9 on 2021-12-15 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 4, 10, 17, 109947)),
        ),
    ]