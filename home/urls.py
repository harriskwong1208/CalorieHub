from django.urls import path 


from . import views

urlpatterns = [
    #Using class-based view
    path('home',views.HomeView.as_view()),

    path('authorized',views.authorized),
]