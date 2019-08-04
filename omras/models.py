from django.db import models
from django_countries.fields import CountryField
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# TRANSPORT_CHOICES=(('Avion','Avion'),('Bus','Bus'),('Bateau','Bateau'),)

from ckeditor.fields import RichTextField
from django.utils.text import slugify




# Create your models here.
class Omra(models.Model):
    created= models.DateTimeField(default=datetime.now, blank='true')

    titre=models.CharField(max_length=255,blank='true')
    slug=models.SlugField(max_length=400,unique='true',null='true')


    ville_depart=models.CharField(max_length=255,blank='true')
    aller=models.DateField(blank='true')
    retour=models.DateField(blank='true')

    escale=models.BooleanField(default='False')

    nom_hotel_mekka=models.CharField(max_length=255,null='true')
    etoiles_mekka=models.PositiveIntegerField(blank='true',validators=[MaxValueValidator(5),MinValueValidator(1)],null='true')
    nombre_nuit_mekka=models.PositiveIntegerField(blank='true')
    distance_kaaba=models.PositiveIntegerField(blank='true',null='True')

    nom_hotel_madina=models.CharField(max_length=255,null='true')
    etoiles_madina=models.PositiveIntegerField(blank='true',validators=[MaxValueValidator(5),MinValueValidator(1)],null='true')
    nombre_nuit_madina=models.PositiveIntegerField(blank='true')
    distance_masjid=models.PositiveIntegerField(blank='true',null='True')




    prix=models.PositiveIntegerField(blank='true')
    prix_chd=models.PositiveIntegerField(blank='true' ,default=0)
    prix_chd2=models.PositiveIntegerField(blank='true' ,default=0)
    prix_inf=models.PositiveIntegerField(blank='true' ,default=0)
    commission=models.PositiveIntegerField(blank='true')


    image=models.ImageField(upload_to='omras',null='true',blank='true')
    image2=models.ImageField(upload_to='omras',null='true',blank='true')
    image3=models.ImageField(upload_to='omras',null='true',blank='true')
    image4=models.ImageField(upload_to='omras',null='true',blank='true')
    description=RichTextField()



    def save(self,*args,**kwargs):
        self.slug='offre-omra-'+slugify(self.titre)+'-hotel-'+slugify(self.nom_hotel_mekka)
        super().save(*args,**kwargs)

    def  __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('single_omras',args=[str(self.slug)])






# delete image when deleting model
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Omra)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
