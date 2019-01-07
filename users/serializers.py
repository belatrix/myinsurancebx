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
