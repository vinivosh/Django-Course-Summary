from pydoc import describe
from django.db import models



class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default='defaultImage.jpg')

    # Defining this will change how an object of this class will be converted to a string via the default python function str(). Cool!
    def __str__(self) -> str:
        return f'{self.title} - {self.slug}'