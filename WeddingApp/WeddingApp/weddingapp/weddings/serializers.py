from rest_framework.serializers import ModelSerializer
from .models import WeddingHall, Service, Menu, User, DishesAndDrink


class WeddingHallSerializer(ModelSerializer):
    class Meta:
        model = WeddingHall
        fields = ['id', 'name', 'time_wedding', 'wedding_hall_images', 'location', 'capacity', 'wedding_hall_price']


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'service_images', 'price']


class DishesAndDrinkSerializer(ModelSerializer):
    class Meta:
        model = DishesAndDrink
        fields = ['id', 'name', 'dishes_drinks_images']


class MenuSerializer(ModelSerializer):
    dishes_and_drink = DishesAndDrinkSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['id', 'name', 'dishes_and_drink', 'total_money']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user






