from django.db import models

# Create your models here.

class Words(models.Model):
    def __str__(self):
        return self.noun
    
    noun=models.CharField(max_length=100)
    adjective=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    expression= models.CharField(max_length=100)
