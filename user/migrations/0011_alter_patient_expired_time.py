# Generated by Django 4.0.1 on 2022-03-11 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_patient_expired_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='expired_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 9, 58, 23, 391431, tzinfo=utc), null=True),
        ),
    ]
