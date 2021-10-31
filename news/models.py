from django.db import models
from datetime import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    article = models.TextField()
    posted = models.DateTimeField()
    def __str__(self):
        return self.title