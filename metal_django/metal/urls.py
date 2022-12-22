# metal/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artists/<int:pk>', views.artist_rig, name='artist_rig'),
    path('artist_rigs/<int:pk>', views.rig_detail, name='rig_detail'),
]