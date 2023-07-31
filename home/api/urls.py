from django.urls import path 

from . import views

urlpatterns= [
    path('',views.getRoutes),
    path('food/',views.getFood),
    path('users/',views.getUsers),
    
]