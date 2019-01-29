from django.shortcuts import get_object_or_404

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import User
from .serializers import UserSerializer


@api_view(['GET', ])
@permission_classes((permissions.IsAuthenticated,))
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


@api_view(['GET', ])
@permission_classes((permissions.IsAdminUser,))
def user_list(request):
    """
    get:
        returns user list
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        """
        Authenticate user with provided credentials
        ---
        serializer: users.serializers.UserAuthenticationSerializer
        response_serializer: users.serializers.UserAuthenticationResponseSerializer
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "data": [{
                'authToken': token.key,
                'user_id': user.pk,
                'is_inspector': user.is_inspector,
                'is_from_insurance': user.is_from_insurance,
                'is_from_auto_repair_shop': user.is_from_auto_repair_shop,
            }]
        })
