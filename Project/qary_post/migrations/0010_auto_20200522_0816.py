# Generated by Django 2.2.9 on 2020-05-22 08:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qary_post', '0009_auto_20200522_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 22, 8, 15, 46, 780956, tzinfo=utc)),
        ),
    ]
