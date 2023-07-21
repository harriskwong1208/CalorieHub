from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home/welcome.html',{'today': datetime.today()})

#redirects user to admin login form if not logged in
@login_required(login_url='/admin')
def authorized(request):
    return render(request,'home/authorized.html',{})