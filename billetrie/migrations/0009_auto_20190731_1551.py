# Generated by Django 2.1.9 on 2019-07-31 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetrie', '0008_auto_20190731_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billeterie',
            name='recu',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 15, 51, 41, 874600)),
        ),
    ]
