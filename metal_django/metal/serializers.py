from rest_framework import serializers

from .models import Artist, ArtistRig, RigDetail

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    artist_rig = serializers.HyperlinkedRelatedField(
        view_name='artist_rig_detail',
        many=True,
        read_only=True
    )
    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'artist_detail'
    )
    class Meta:
        model = Artist
        fields = ('id', 'photo_url', 'website', 'bio','name', 'band', 'artist_url', 'artist_rig')


class ArtistRigSerializer(serializers.HyperlinkedModelSerializer):
    
    artists = ArtistSerializer(
        many=True,
        read_only=True
    )
    artist_rig_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'artist_rig_detail'
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source= 'artist'
    )
        
    class Meta:
        model = ArtistRig
        fields = ('id', 'guitar', 'pedal1', 'pedal2', 'pedal3', 'amplifier', 'rig_year','photo_url', 'artist_rig_url', 'artist_id', 'artists', 'name')



class RigDetailSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        many=True,
        read_only=True    
    )
    # rig_detail_url = serializers.ModelSerializer.serializer_url_field(
    #     view_name = 'rig_detail'
    # )    
    class Meta:
        model = RigDetail
        fields = ('id','description', 'tuning', 'name', 'artists', 'photo_url')        