from django.shortcuts import render

from django.views.generic import CreateView,DetailView,ListView,UpdateView

#For delete views 
from django.views.generic.edit import DeleteView

#for error raising
from django.http import Http404

from .models import Food
from .forms import FoodForm

class FoodDeleteView(DeleteView):
    model = Food
    success_url = '/food/'
    template_name = 'food/food_delete.html'

class FoodUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    success_url = '/food/'    

class FoodCreateView(CreateView):
    model = Food
    #imported from forms.py
    form_class = FoodForm

    #Does the same thing as above
    # fields = ['title','text','calories']
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