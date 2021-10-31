from django.db import models
from datetime import datetime

from django.db.models.enums import Choices
# Create your models here.
class Popup(models.Model):
    title = models.CharField(max_length=100)
    CHOICES = [
        ('space', 'space'),
        ('cnt223', 'cnt223'),
      ]
        
    category = models.CharField(max_length=10, choices = CHOICES)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
     return self.title