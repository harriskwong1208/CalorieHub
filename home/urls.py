from django.urls import path 


from . import views

urlpatterns = [
    #Using class-based view
    path('home',views.HomeView.as_view(),name="home"),

    path('authorized',views.AuthorizedView.as_view()),
]