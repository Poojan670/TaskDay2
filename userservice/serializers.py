from rest_framework import serializers
from .models import User, Roles


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'phone_no', 'address', 'created_date', 'updated_date', 'roles')
        extra_kwargs = {
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
            'password': {'write_only': True}
        }


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
