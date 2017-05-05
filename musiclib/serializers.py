from rest_framework import routers, serializers, viewsets
from musiclib.models import Category, Artist, Discography, Song

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class DiscographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Discography
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
