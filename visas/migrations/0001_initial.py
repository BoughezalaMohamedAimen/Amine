# Generated by Django 2.1.9 on 2019-08-02 12:46

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank='true', default=django.utils.timezone.now)),
                ('slug', models.SlugField(max_length=400, null='true', unique='true')),
                ('destination', django_countries.fields.CountryField(blank='true', max_length=2)),
                ('delai', models.PositiveIntegerField(blank='true')),
                ('prix', models.PositiveIntegerField(blank='true')),
                ('commission', models.PositiveIntegerField(blank='true', default=0)),
                ('dossier', models.TextField(blank='true')),
            ],
        ),
    ]
