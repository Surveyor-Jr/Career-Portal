# Generated by Django 3.2.4 on 2021-06-24 18:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0007_auto_20210624_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 6, 24, 18, 42, 54, 473137, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(editable=False, max_length=500),
        ),
    ]
