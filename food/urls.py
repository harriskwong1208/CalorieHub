from django.urls import path 


from . import views

urlpatterns = [
    path('',views.FoodListView.as_view(),name="food.list"),

    #pass pk for each food item
    path('<int:pk>',views.FoodDetailView.as_view(),name="food.detail"),
    path('new/',views.FoodCreateView.as_view(),name="food.new"),
]