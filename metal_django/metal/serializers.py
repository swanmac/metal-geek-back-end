from rest_framework import serializers

from .models import Artist, ArtistRig, RigDetail

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    artist_rig = serializers.HyperlinkedRelatedField(
        view_name='artist_rig_detail',
        read_only=True
    )

    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'website', 'bio','name', 'band')

class ArtistRigSerializer(serializers.HyperlinkedModelSerializer):
    rig_detail = serializers.HyperlinkedRelatedField(
        view_name='rig_detail',
        read_only=True
    )
    class Meta:
        model = ArtistRig
        fields = ('id', 'guitar', 'pedal1', 'pedal2', 'pedal3', 'amplifier', 'rig_year','photo_url')

class RigDetailSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        many=True,
        read_only=True    
        )
    class Meta:
        model = RigDetail
        fields = ('id','description''tuning')        