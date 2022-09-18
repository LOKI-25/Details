from django.db import models

# Create your models here.

class Details(models.Model):
    name=models.CharField(max_length=100)
    skill=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self) :
        return self.name