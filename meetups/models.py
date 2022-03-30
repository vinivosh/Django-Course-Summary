from pydoc import describe
from django.db import models



class Location(models.Model):
    city = models.CharField(max_length=120)
    province = models.CharField(max_length=120)
    provAcronym = models.CharField(max_length=4)
    country = models.CharField(max_length=60)
    fullAddress = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.country}, {self.city} - {self.province} ({self.fullAddress})'

    def strSmall(self):
        return f'{self.city} - {self.provAcronym}, {self.fullAddress}'

    def strSmaller(self):
        return f'{self.country}, {self.city} - {self.provAcronym}'

class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    date = models.DateField()
    organizerEmail = models.EmailField()
    image = models.ImageField(upload_to='images', default='defaultImage.jpg')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True)

    # Defining this will change how an object of this class will be converted to a string via the default python function str(). Cool!
    def __str__(self):
        return f'{self.title} ({self.slug})'