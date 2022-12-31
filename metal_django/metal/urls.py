# metal/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    # path('artist-details/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artist-rig/', views.ArtistRigList.as_view(), name='artist_rig'),
    path('artist-rig/<int:pk>', views.ArtistRigDetail.as_view(), name='artist_rig_detail'),
    path('rig-detail/', views.RigDetailList.as_view(), name='rig_detail'),
    path('rig-detail/<int:pk>', views.RigDetailDetail.as_view(), name='rig_detail_detail')
    path('artistspost/', views.ArtistPost.as_view(), name='artist_detail'),
    path('artistsupdate/<int:pk>', views.ArtistUpdate.as_view(), name='artist_detail'),
    path('artistsdelete/<int:pk>', views.ArtistDelete.as_view(), name='artist_detail'),
]