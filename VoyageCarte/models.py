from django.db import models
from datetime import datetime
# Create your models here.

class VoyageCarte(models.Model):
    recu=models.DateTimeField(default=datetime.now())
    destination=models.CharField(max_length=120)
    ville=models.CharField(max_length=120)
    dateAller=models.DateField()
    dateRetour=models.DateField()
    nbrAdulte=models.PositiveIntegerField()
    nbrEnfant=models.PositiveIntegerField()
    message=models.TextField(null='True',blank='True')
    nom=models.CharField(max_length=120)
    prenom=models.CharField(max_length=120)
    telephone=models.CharField(max_length=10)
    email=models.EmailField()
