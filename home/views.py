from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime

# Create your views here.
def home(request):
    return render(request,'home/welcome.html',{'now': datetime.now()})
