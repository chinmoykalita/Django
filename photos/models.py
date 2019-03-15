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
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category) 
    image = models.ImageField(upload_to = 'gallery/')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    @classmethod
    def get_photos(cls,id):
        try:
           photos = Image.objects.get(id=id)
           return photos
        except DoesNotExist:
            return Image.objects.get(id=1)

        
    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos