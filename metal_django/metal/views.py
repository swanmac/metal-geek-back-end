from django.shortcuts import render
from rest_framework import generics
from .serializers import ArtistSerializer, ArtistRigSerializer, RigDetailSerializer, GearSerializer
from .models import Artist, ArtistRig, RigDetail, Gear
from rest_framework.response import Response


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

class GearList(generics.ListCreateAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer

class GearDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer    

class GearPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer
    def get(self, request):
        gearObj=Gear.objects.all()
        gearSerializeObj=GearSerializer(gearObj,many=True)
        return Response(gearSerializeObj.data)
    
    def post(self,request):
        serializeobj=GearSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class GearUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer
    def post(self,request,pk):
        try:
            gearObj=Gear.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeobj=GearSerializer(gearObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class GearDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer
    def post(self,request,pk):
        try:
            gearObj=Gear.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        gearObj.delete()
        return Response(200)    

