# Generated by Django 2.1.9 on 2019-07-31 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_auto_20190731_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='recu',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 22, 48, 44, 545857)),
        ),
    ]
