# Generated by Django 3.2.4 on 2021-06-24 17:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_auto_20210624_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 6, 24, 17, 9, 35, 303153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
