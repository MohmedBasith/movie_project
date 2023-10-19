from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
