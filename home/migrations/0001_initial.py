# Generated by Django 2.1.9 on 2019-08-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('sous_titre', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='slider')),
                ('lien', models.CharField(default='#', max_length=255)),
            ],
        ),
    ]
