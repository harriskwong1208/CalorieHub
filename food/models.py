from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    calories = models.IntegerField()
    created = models.DateTimeField(auto_created=True)