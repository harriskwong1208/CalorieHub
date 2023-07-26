from django.shortcuts import render

from django.views.generic import CreateView,DetailView,ListView

#for error raising
from django.http import Http404

from .models import Food

class FoodCreateView(CreateView):
    model = Food
    fields = ['title','text','calories']
    success_url = '/food/'

class FoodListView(ListView):
    model = Food
    #Change it from default name("objects") to 'food'
    context_object_name = 'food'
    template_name = 'food/food_list.html'

#function classed view, does the same thing from above
# def list(request):
#     all_food = Food.objects.all()
#     return render(request,'food/food_list.html',{
#         'food':all_food
#     })



class FoodDetailView(DetailView):
    model = Food
    context_object_name = "food"


#function based view, does the same thing as above
# def detail(request,pk):
#     try:
#         food = Food.objects.get(pk=pk)
#     except:
#         raise Http404("Food does not exists.")
#     return render(request,'food/food_detail.html',{
#         'food': food
#     })