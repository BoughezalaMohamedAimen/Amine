from django.db import models
from django_countries.fields import CountryField
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone








# Create your models here.
class Visa(models.Model):
    created= models.DateTimeField(default=timezone.now, blank='true')
    slug=models.SlugField(max_length=400,unique='true',null='true')
    destination=CountryField(blank='true')
    delai=models.PositiveIntegerField(blank='true')
    prix=models.PositiveIntegerField(blank='true')
    commission=models.PositiveIntegerField(blank='true',default=0)
    dossier=models.TextField(blank='true')

    def __str__(self):
        return self.destination
    def get_absolute_url(self):
        return reverse('single_visas',args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug='visa-'+str(self.destination.name).replace(' ','-')
        super().save(*args, **kwargs)
    def update(self, *args, **kwargs):
        self.slug='visa-'+str(self.destination.name).replace(' ','-')
        super().update(*args, **kwargs)
