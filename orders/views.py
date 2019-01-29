from django.shortcuts import get_object_or_404

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response

from .models import Order, OrderStatus, Attachment
from .serializers import AttachmentSerializer, OrderSerializer, OrderCreationSerializer, OrderStatusSerializer
from users.models import User
from users.permissions import IsInspectorOrStaff, IsInsuranceOrStaff


@api_view(['POST', ])
@permission_classes((IsInspectorOrStaff,))
def order_creation(request):
    """
    Creates a new order
    ---
    POST:
        serializer: orders.serializers.OrderCreationSerializer
    """
    serializer = OrderCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = request.user
        initial_status = OrderStatus.objects.filter(is_default=True).first()
        try:
            order = Order.objects.create(
                car_model=serializer.validated_data['car_model'],
                created_by=user,
                plate_number=serializer.validated_data['plate_number'],
                accident_location=serializer.validated_data['accident_location'],
                client=serializer.validated_data['client'],
                status=initial_status,
            )
        except Exception as e:
            print(e)
            raise NotAcceptable('Not valid.')
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
    orders = Order.objects.all()

    if request.GET.get('user'):
        user_id = request.GET.get('user')
        user = get_object_or_404(User, pk=user_id)
        orders = orders.filter(created_by=user)

    if request.GET.get('status'):
        status_id = request.GET.get('status')
        order_status = get_object_or_404(OrderStatus, pk=status_id)
        orders = orders.filter(status=order_status)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH', ])
@permission_classes((IsInsuranceOrStaff,))
def order_status_change(request, order_id, status_id):
    """
    Changes order status for an order
    """
    order_status = get_object_or_404(OrderStatus, pk=status_id)
    order = get_object_or_404(Order, pk=order_id)
    order.status = order_status
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', ])
@permission_classes((IsInsuranceOrStaff,))
def order_status_list(request):
    """
    Returns order status list
    """
    order_statuses = OrderStatus.objects.all()
    serializer = OrderStatusSerializer(order_statuses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH', ])
@permission_classes((IsInspectorOrStaff,))
def order_update(request, order_id):
    """
    Update an order
    ---
    PATCH:
        serializer: orders.serializers.OrderCreationSerializer
    """
    serializer = OrderCreationSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        try:
            Order.objects.filter(pk=order_id).update(
                car_model=serializer.validated_data['car_model'],
                plate_number=serializer.validated_data['plate_number'],
                accident_location=serializer.validated_data['accident_location'],
                client=serializer.validated_data['client'],
            )
        except Exception as e:
            print(e)
            raise NotAcceptable('Not valid.')
        order = get_object_or_404(Order, pk=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['POST', ])
@permission_classes((IsInspectorOrStaff,))
def upload_file(request, order_id):
    """
    Upload a file
    """
    order = get_object_or_404(Order, pk=order_id)
    file_to_upload = request.FILES['file']
    pre_attachment = Attachment.objects.create(order=order, file=file_to_upload, uploaded_by=request.user)
    attachment = get_object_or_404(Attachment, pk=pre_attachment.id)
    serializer = AttachmentSerializer(attachment)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
