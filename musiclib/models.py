from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s"%self.name

class Artist(models.Model):
    name = models.CharField(max_length = 128)
    picture = models.ImageField(upload_to = "artists", null = True, blank = True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s"%self.name

class Discography(models.Model):
    name = models.CharField(max_length = 128) 
    artist = models.ForeignKey(Artist)
    year = models.IntegerField(null = True, blank = True)
    category = models.ManyToManyField(Category)
    picture = models.ImageField(upload_to = "discographies", null = True, blank = True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s"%self.name

class Song(models.Model):
    name = models.CharField(max_length = 128)
    number = models.IntegerField(null = True,blank = True,help_text="This is the number of the song in the disc")
    discography = models.ForeignKey(Discography)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"%s"%self.name
