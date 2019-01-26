from django.shortcuts import get_object_or_404

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from users.models import User


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated,))
def order_detail(request, order_id):
    """
    Returns order detail
    ---
    GET:
        response_serializer: orders.serializers.OrderSerializer
    """
    order = get_object_or_404(Order, pk=order_id)
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated,))
def order_list(request):
    """
    Returns order list
    """
    if request.GET.get('user'):
        user_id = request.GET.get('user')
        user = get_object_or_404(User, pk=user_id)
        orders = Order.objects.filter(created_by=user)
    else:
        orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
