from django.db import models
from datetime import datetime
# Create your models here.
CLASSE_CHOICES = (
("economique" , 'economique'),
("affaire" , 'affaire'),
("premiere" , 'premiere'),
)
class Billeterie(models.Model):
    recu=models.DateTimeField(default=datetime.now())
    depart=models.CharField(max_length=120)
    arrive=models.CharField(max_length=120)
    dateAller=models.DateField()
    dateRetour=models.DateField(null=True,blank=True)
    classe=models.CharField(choices=CLASSE_CHOICES,default='economique',max_length=15)
    nbrAdulte=models.PositiveIntegerField()
    nbrEnfant=models.PositiveIntegerField()
    depart_multiple=models.CharField(max_length=120,blank=True,null=True)
    arrive_multiple=models.CharField(max_length=120,blank=True,null=True)
    dateAller_multiple=models.DateField(null=True,blank='True')
    dateRetour_multiple=models.DateField(null=True,blank='True')
    classe_multiple=models.CharField(choices=CLASSE_CHOICES,default='economique',max_length=15)
    nbrAdulte_multiple=models.PositiveIntegerField()
    nbrEnfant_multiple=models.PositiveIntegerField()
    nom=models.CharField(max_length=120)
    prenom=models.CharField(max_length=120)
    telephone=models.CharField(max_length=10)
    email=models.EmailField()
