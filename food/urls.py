from django.urls import path 


from . import views

urlpatterns = [
    path('',views.FoodListView.as_view()),

    #pass pk for each food item
    path('<int:pk>',views.FoodDetailView.as_view()),
]