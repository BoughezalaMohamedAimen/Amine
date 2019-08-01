from django.db import models
from datetime import datetime
# Create your models here.

class Hotel(models.Model):
    recu=models.DateTimeField(default=datetime.now())
    destination=models.CharField(max_length=120)
    ville=models.CharField(max_length=120)
    dateAller=models.DateField()
    dateRetour=models.DateField()
    nbrAdulte=models.PositiveIntegerField()
    nbrEnfant=models.PositiveIntegerField()
    nbrChambre=models.PositiveIntegerField()
    nom=models.CharField(max_length=120)
    prenom=models.CharField(max_length=120)
    telephone=models.CharField(max_length=10)
    email=models.EmailField()
