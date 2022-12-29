from django.db import models
from django.db.models import Model

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    band = models.TextField(max_length=100)
    website = models.TextField(max_length=50)
    bio = models.TextField(max_length=500)
    photo_url= models.TextField(null=True, max_length=600)

    def __str__(self):
        return self.name

class ArtistRig(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name= 'artist_rig')
    name = models.CharField(null=True, max_length=200)
    guitar = models.TextField(max_length=300)
    pedal1 = models.TextField(max_length=200)
    pedal2 = models.TextField(max_length=200)
    pedal3 = models.TextField(max_length=200)
    amplifier = models.TextField(max_length=400)
    rig_year = models.TextField(max_length=200)
    photo_url= models.TextField(null=True, max_length=600)

    def __str__(self):
        return self.name 

class RigDetail(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True,related_name= 'rig_detail')
    name = models.TextField(null=True, max_length=200)
    description = models.TextField(max_length=1000)
    tuning = models.TextField(max_length=300)
    photo_url= models.TextField(null=True, max_length=600)

    def __str__(self):
        return self.name
        