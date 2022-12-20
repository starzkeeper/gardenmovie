from django.db import models

from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.name