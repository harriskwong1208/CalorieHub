from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
#from django.contrib.auth.decorators import login_required

#For login authorization
from django.contrib.auth.mixins import LoginRequiredMixin

#Used for class-base views
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

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
class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = '/food'
    
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'