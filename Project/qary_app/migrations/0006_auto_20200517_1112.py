# Generated by Django 2.2.9 on 2020-05-17 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qary_app', '0005_auto_20200517_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 11, 12, 0, 175486, tzinfo=utc)),
        ),
    ]
