from django.db import models

# Create your models here.
class Catalog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='catalog_images', blank=True)

    def __str__(self):
        return self.title



