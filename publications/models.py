from django.db import models
from datetime import datetime

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=150)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=200)
    docu_main = models.FileField(upload_to='docs/%Y/%m/%d/')
    def __str__(self):
        return self.title