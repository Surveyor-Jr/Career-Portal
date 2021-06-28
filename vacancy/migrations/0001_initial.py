# Generated by Django 3.2.4 on 2021-06-24 09:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Vacancy Type',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('company_logo', models.ImageField(upload_to='logos/')),
                ('salary', models.CharField(max_length=100)),
                ('date_posted', models.DateField(default=datetime.datetime(2021, 6, 24, 9, 37, 38, 758335, tzinfo=utc))),
                ('closing_date', models.DateField()),
                ('description', models.TextField()),
                ('qualifications', models.TextField()),
                ('source_link', models.URLField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('vacancyType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.vacancytypes')),
            ],
            options={
                'verbose_name_plural': 'Vacancies',
            },
        ),
    ]
