# Generated by Django 2.2.9 on 2020-05-17 09:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qary_app', '0004_auto_20200511_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 9, 46, 45, 752954, tzinfo=utc)),
        ),
    ]
