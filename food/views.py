from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView,DetailView,ListView,UpdateView

#For delete views 
from django.views.generic.edit import DeleteView

#for error raising
from django.http import Http404

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Food
from .forms import FoodForm

class FoodDeleteView(LoginRequiredMixin,DeleteView):
    model = Food
    success_url = '/food/'
    template_name = 'food/food_delete.html'
    login_url = '/admin'

class FoodUpdateView(LoginRequiredMixin,UpdateView):
    model = Food
    form_class = FoodForm
    success_url = '/food/'    
    login_url = '/admin'

class FoodCreateView(LoginRequiredMixin,CreateView):
    model = Food
    #imported from forms.py
    form_class = FoodForm

    #Does the same thing as above
    # fields = ['title','text','calories']
    login_url = '/admin'
    success_url = '/food'

    # When a user submits a form, this method is called. 
    # It takes the form data, associates it with the currently 
    # logged-in user (assuming the user is authenticated), 
    # saves it to the database, and then redirects the user to a 
    # specified URL upon successful submission.
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


#LoginRequireMIxin = only list food items that belows to the user
class FoodListView(LoginRequiredMixin,ListView):
    model = Food
    #Change it from default name("objects") to 'food'
    context_object_name = 'food'
    template_name = 'food/food_list.html'
    login_url = '/admin/'

    def get_queryset(self):
        return self.request.user.food.all()

#function classed view, does the same thing from above
# def list(request):
#     all_food = Food.objects.all()
#     return render(request,'food/food_list.html',{
#         'food':all_food
#     })



class FoodDetailView(LoginRequiredMixin,DetailView):
    model = Food
    context_object_name = "food"
    login_url = '/admin'


#function based view, does the same thing as above
# def detail(request,pk):
#     try:
#         food = Food.objects.get(pk=pk)
#     except:
#         raise Http404("Food does not exists.")
#     return render(request,'food/food_detail.html',{
#         'food': food
#     })