from django.shortcuts import render

#for error raising
from django.http import Http404

from .models import Food

def list(request):
    all_food = Food.objects.all()
    return render(request,'food/food_list.html',{
        'food':all_food
    })

def detail(request,pk):
    try:
        food = Food.objects.get(pk=pk)
    except:
        raise Http404("Food does not exists.")
    return render(request,'food/food_detail.html',{
        'food': food
    })