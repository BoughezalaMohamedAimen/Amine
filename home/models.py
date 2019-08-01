from django.db import models

# Create your models here.
class Slider(models.Model):
    titre=models.CharField(max_length=255)
    sous_titre=models.CharField(max_length=255)
    image=models.ImageField(upload_to='slider')
    lien=models.CharField(max_length=255,default='#')

    def __str__(self):
        return self.titre





# delete image when deleting model
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Slider)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
