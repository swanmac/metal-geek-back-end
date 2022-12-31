from django.contrib import admin
from .models import Artist
from .models import ArtistRig
from .models import RigDetail
from .models import Gear

# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistRig)
admin.site.register(RigDetail)
admin.site.register(Gear)
