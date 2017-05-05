from django.contrib import admin
from musiclib.models import Category, Artist, Discography, Song

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Discography)
class DiscographyAdmin(admin.ModelAdmin):
    pass

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
