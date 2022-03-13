# Generated by Django 4.0.1 on 2022-03-12 19:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_user_isfirst_alter_lgsbody_kind_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_email_sent_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='visitdetails',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='visitschedule',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2022, 3, 13)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='expired_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 19, 47, 41, 944474, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='primarynurse', max_length=100),
        ),
        migrations.AlterField(
            model_name='visitschedule',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 12, 19, 47, 41, 944474, tzinfo=utc)),
        ),
    ]