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

class ArtistRig(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistRig.objects.all()
    serializer_class = ArtistRigSerializer


class RigDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RigDetail.objects.all()
    serializer_class = RigDetailSerializer
    