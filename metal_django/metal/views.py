from django.shortcuts import render
from rest_framework import generics
from .serializers import ArtistSerializer, ArtistRigSerializer, RigDetailSerializer
from .models import Artist, ArtistRig, RigDetail


# Create your views here.
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRigList(generics.ListCreateAPIView):
    queryset = ArtistRig.objects.all()
    serializer_class = ArtistRigSerializer    

class ArtistRigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistRig.objects.all()
    serializer_class = ArtistRigSerializer

class RigDetailList(generics.ListCreateAPIView):
    queryset = RigDetail.objects.all()
    serializer_class = RigDetailSerializer    


class RigDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RigDetail.objects.all()
    serializer_class = RigDetailSerializer

