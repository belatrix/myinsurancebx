from django.shortcuts import get_object_or_404

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(['GET', ])
@permission_classes((permissions.AllowAny,))
def user_detail(request, user_id):
    """
    Returns user detail
    ---
    GET:
        response_serializer: users.serializers.UserSerializer
    """
    user = get_object_or_404(User, pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
