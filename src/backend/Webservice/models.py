from django.db import models

# Create your models here.

class Porker(models.Model):
    serial = models.IntegerField(max_length=15)
    shape = models.CharField(max_length=15)
    number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.serial