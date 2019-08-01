from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    recu=models.DateTimeField(default=datetime.now())    
    nom=models.CharField(max_length=120)
    prenom=models.CharField(max_length=120)
    telephone=models.CharField(max_length=10)
    email=models.EmailField()
    message=models.TextField(null='True',blank='True')
