
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),

    #get url from urls.py from the home app.
    path('',include('home.urls')),
]
