from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name