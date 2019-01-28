from rest_framework import serializers

from .models import Order, Attachment
from users.serializers import UserSerializer


class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer()

    class Meta(object):
        model = Attachment
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta(object):
        model = Order
        fields = '__all__'
        depth = 1


class OrderCreationSerializer(serializers.Serializer):
    car_model = serializers.CharField()
    plate_number = serializers.CharField()
    accident_location = serializers.CharField()
    client = serializers.CharField()
