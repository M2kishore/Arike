# Generated by Django 4.0.1 on 2022-03-11 02:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2022, 3, 11)),
        ),
    ]