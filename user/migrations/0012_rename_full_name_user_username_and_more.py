# Generated by Django 4.0.1 on 2022-03-11 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_patient_expired_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='patient',
            name='expired_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 10, 0, 45, 825798, tzinfo=utc), null=True),
        ),
    ]
