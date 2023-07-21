from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)