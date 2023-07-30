from django.db import models

#import user model 
from django.contrib.auth.models import User


# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    calories = models.IntegerField()

    #Set up foreign key.
    #on_delete=models.CASCADE = all food info gets deleted 
    #if user assiocated with that data gets deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="food")