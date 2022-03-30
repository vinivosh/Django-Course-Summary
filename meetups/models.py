from pydoc import describe
from django.db import models



class Location(models.Model):
    city = models.CharField(max_length=120)
    province = models.CharField(max_length=120)
    country = models.CharField(max_length=60)
    fullAdress = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.city} - {self.province} ({self.fullAdress})'

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='defaultImage.jpg')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, default=None)

    # Defining this will change how an object of this class will be converted to a string via the default python function str(). Cool!
    def __str__(self):
        return f'{self.title} ({self.slug})'