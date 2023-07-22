from django.shortcuts import render

from .models import Food

def list(request):
    all_food = Food.objects.all()
    return render(request,'food/food_list.html',{
        'food':all_food
    })