from django.db import models

# Create your models here.
# Create your models here.
class Movie(models.Model): 
    name = models.CharField(max_length=50) 
    Rating= models.CharField(max_length=200) 
    def __str__(self): 
        return self.name