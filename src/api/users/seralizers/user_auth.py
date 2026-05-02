from apps.users.models import User
from rest_framework.serializers import ModelSerializer


class UserSeralizer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSeralizer(ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'email', 'last_name', 'password']
