from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'is_inspector',
                  'is_from_insurance',
                  'is_from_auto_repair_shop',
                  'is_staff',
                  'is_active')


class UserAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)


class UserAuthenticationResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()
    is_inspector = serializers.BooleanField()
    is_from_insurance = serializers.BooleanField()
    is_from_auto_repair_shop = serializers.BooleanField()
