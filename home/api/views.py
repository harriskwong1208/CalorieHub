from rest_framework.decorators import api_view
from rest_framework.response import Response
from food.models import Food
from .serializers import FoodSerializer,UsersSerializer

from django.contrib.auth.models import User



#Function based view 

@api_view(['GET'])
def getRoutes(request):

    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/food',
        'GET /api/food/:id',

    ]
    return Response(routes)

@api_view(['GET'])
def getFood(request):
    food = Food.objects.all()

    # many = serializing many objects
    serializer = FoodSerializer(food,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request):
    user = User.objects.all()

    # many = serializing many objects
    serializer = UsersSerializer(user,many=True)
    return Response(serializer.data)
