# Generated by Django 2.1.9 on 2019-07-31 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recu', models.DateTimeField(default=datetime.datetime(2019, 7, 31, 2, 54, 58, 999292))),
                ('nom', models.CharField(max_length=120)),
                ('prenom', models.CharField(max_length=120)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank='True', null='True')),
            ],
        ),
    ]
