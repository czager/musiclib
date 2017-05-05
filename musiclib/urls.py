from rest_framework import routers
from musiclib.views import CategoryViewSet, ArtistViewSet, DiscographyViewSet, SongViewSet

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'discographies', DiscographyViewSet)
router.register(r'songs', SongViewSet)
urlpatterns = router.urls
