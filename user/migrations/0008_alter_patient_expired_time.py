# Generated by Django 4.0.1 on 2022-03-11 09:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_lsg_body_code_lgsbody_lgs_body_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='expired_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 9, 55, 52, 385201, tzinfo=utc), null=True),
        ),
    ]