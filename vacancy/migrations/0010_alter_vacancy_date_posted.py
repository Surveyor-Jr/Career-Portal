# Generated by Django 3.2.4 on 2021-06-26 14:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0009_auto_20210626_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 6, 26, 14, 47, 28, 798064, tzinfo=utc)),
        ),
    ]
