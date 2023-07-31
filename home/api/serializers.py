from rest_framework.serializers import ModelSerializer

from food.models import Food



from django.contrib.auth.models import User


#Turn model objects into JSON for api

class FoodSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'    

class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'            