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


# class ArtistPost(generics.RetrieveUpdateDestroyAPIView):
#     def get(self, request):
#         artistObj=Artist.objects.all()
#         artistSerializeObj=ArtistSerializer(artistObj,many=True)
#         return Response(artistSerializeObj.data)
    
#     def post(self,request):
#         serializeobj=ArtistSerializer(data=request.data)
#         if serializeobj.is_valid():
#             serializeobj.save()
#             return Response(200)
#         return Response(serializeobj.errors)


# class ArtistUpdate(generics.RetrieveUpdateDestroyAPIView):
#     def post(self,request,pk):
#         try:
#             artistObj=Artist.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         serializeobj=ArtistSerializer(artistObj,data=request.data)
#         if serializeobj.is_valid():
#             serializeobj.save()
#             return Response(200)
#         return Response(serializeobj.errors) 


# class ArtistDelete(generics.RetrieveUpdateDestroyAPIView):
#     def post(self,request,pk):
#         try:
#             artistObj=Artist.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")
#         artistObj.delete()
#         return Response(200)              

