from django.urls import path 


from . import views

urlpatterns = [
    path('',views.list),

    #pass pk for each food item
    path('<int:pk>',views.detail),
]