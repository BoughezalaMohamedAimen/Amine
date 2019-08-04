from django.db import models
from django_countries.fields import CountryField
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
TRANSPORT_CHOICES=(('Avion','Avion'),('Bus','Bus'),('Bateau','Bateau'),)
from ckeditor.fields import RichTextField






# Create your models here.
class Voyage(models.Model):
    created= models.DateTimeField(default=datetime.now, blank='true')
    slug=models.SlugField(max_length=400,unique='true',null='true')
    titre=models.CharField(max_length=255,blank='true')
    destination=CountryField(blank='true')
    ville_depart=models.CharField(max_length=255,blank='true')
    nom_hotel=models.CharField(max_length=255,null='true')
    etoiles=models.PositiveIntegerField(blank='true',validators=[MaxValueValidator(5),MinValueValidator(1)],null='true')
    aller=models.DateField(blank='true')
    retour=models.DateField(blank='true')
    transport=models.CharField(max_length=255,blank='true',choices=TRANSPORT_CHOICES)
    prix=models.PositiveIntegerField(blank='true')
    prix_chd=models.PositiveIntegerField(blank='true' ,default=0)
    prix_chd2=models.PositiveIntegerField(blank='true' ,default=0)
    prix_inf=models.PositiveIntegerField(blank='true' ,default=0)
    image=models.ImageField(upload_to='voyages',null='true',blank='true')
    image2=models.ImageField(upload_to='voyages',null='true',blank='true')
    image3=models.ImageField(upload_to='voyages',null='true',blank='true')
    image4=models.ImageField(upload_to='voyages',null='true',blank='true')
    description=RichTextField()



    def  __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('single_voyages',args=[str(self.slug)])







# delete image when deleting model
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Voyage)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
