from django.db import models
from django.db.models import Model

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    band = models.TextField(max_length=100)
    website = models.TextField(max_length=50)
    bio = models.TextField(max_length=200)
    photo_url= models.TextField(null=True, max_length=500)

    def __str__(self):
        return self.name

class ArtistRig(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name= 'artist_rig')
    guitar = models.TextField(max_length=200)
    pedal1 = models.TextField(max_length=100)
    pedal2 = models.TextField(max_length=100)
    pedal3 = models.TextField(max_length=100)
    amplifier = models.TextField(max_length=100)
    rig_year = models.TextField(max_length=200)
    photo_url= models.TextField(null=True, max_length=500)

    def __str__(self):
        return self.name        

class RigDetails(models.Model):
    artistRig = models.ForeignKey(ArtistRig, on_delete=models.CASCADE, related_name= 'rig_details')
    description = models.TextField(max_length=400)
    tuning = models.TextField(max_length=200)

    def __str__(self):
        return self.name 