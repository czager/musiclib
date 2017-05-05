from rest_framework import viewsets
from musiclib.serializers import CategorySerializer, ArtistSerializer, DiscographySerializer, SongSerializer
from musiclib.models import Category, Artist, Discography, Song

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Category instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ArtistViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Artist instances.
    """
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class DiscographyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Discography instances.
    """
    serializer_class = DiscographySerializer
    queryset = Discography.objects.all()

class SongViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Song instances.
    """
    serializer_class = SongSerializer
    queryset = Song.objects.all()
