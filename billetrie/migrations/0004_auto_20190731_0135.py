# Generated by Django 2.1.9 on 2019-07-31 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billetrie', '0003_auto_20190731_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billeterie',
            name='recu',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 1, 35, 43, 595283)),
        ),
    ]
