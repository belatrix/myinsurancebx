from rest_framework import serializers

from .models import Order, OrderStatus, Attachment, AutoRepairShop, FileHash
from users.serializers import UserSerializer


class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer()

    class Meta(object):
        model = Attachment
        fields = '__all__'


class AutoRepairShopSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = AutoRepairShop
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    order_attachment = AttachmentSerializer(many=True)

    class Meta(object):
        model = Order
        fields = '__all__'
        depth = 1


class OrderBudgetSerializer(serializers.Serializer):
    budget = serializers.CharField()


class OrderCreationSerializer(serializers.Serializer):
    car_model = serializers.CharField()
    plate_number = serializers.CharField()
    accident_location = serializers.CharField()
    client = serializers.CharField()


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = OrderStatus
        fields = '__all__'

class FileHashSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = FileHash
        fields = '__all__'
