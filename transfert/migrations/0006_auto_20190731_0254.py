# Generated by Django 2.1.9 on 2019-07-31 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfert', '0005_auto_20190731_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfert',
            name='recu',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 2, 54, 58, 993308)),
        ),
    ]
