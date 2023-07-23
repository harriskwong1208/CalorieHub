from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required

#Used for class-base views
from django.views.generic import TemplateView

#Using a class-based view to render out template
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    #context 
    extra_context = {'today': datetime.today()}


# Function to render out template, a different way of doing 
#the same thing as above
# def home(request):
#     return render(request,'home/welcome.html',{'today': datetime.today()})

#redirects user to admin login form if not logged in
@login_required(login_url='/admin')
def authorized(request):
    return render(request,'home/authorized.html',{})