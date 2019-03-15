from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name       
    class Meta:
        ordering = ['name']


class Image(models.Model):
    name = models.CharField(max_length =60)
    image_url = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category) 

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']


    def save_image(self):
        self.save()