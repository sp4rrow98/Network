# Generated by Django 3.2.9 on 2021-12-28 06:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0027_auto_20211228_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 8, 7, 4, 869746)),
        ),
        migrations.AlterUniqueTogether(
            name='followers',
            unique_together=set(),
        ),
    ]
