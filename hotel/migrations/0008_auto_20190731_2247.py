# Generated by Django 2.1.9 on 2019-07-31 21:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20190731_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='recu',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 22, 47, 44, 340049)),
        ),
    ]