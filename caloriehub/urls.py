
from django.contrib import admin
from django.urls import path

#import views.py from the home app
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home)
]
