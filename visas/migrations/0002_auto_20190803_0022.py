# Generated by Django 2.1.9 on 2019-08-02 23:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='dossier',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
