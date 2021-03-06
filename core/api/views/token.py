"""API > views > token.py"""
# PYTHON IMPORTS
import logging
from sys import _getframe
# DRF IMPORTS
from django.utils import timezone
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from hospital.uility import user_has_group
from django.contrib.auth import authenticate, login, logout

# API IMPORTS
from core.api.serializers import (
    TokenSerializer, LogoutSerializer, UserSerializer
)

logger = logging.getLogger(__name__)


class ObtainTokenView(TokenObtainPairView):
    """Gets a authentication token for user with provided credentials"""
    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                user = authenticate(
                    phone=serializer.data.get('phone'),
                    password=serializer.data.get('password')
                    )
                if user:
                    serializer.is_valid(raise_exception=True)
                    serialized_user = UserSerializer(user)

                    user.last_login = timezone.now()
                    user.save()  # save the last login time to now()

                    user_type = "Unauthorized"

                    try:
                        user_id = user.doctor.pk
                        user_name = user.doctor.name
                        user_type = 'Doctor'
                    except Exception as e:
                        print(e)
                        user_id = user.patient_data.pk
                        user_name = user.patient_data.name
                        user_type = 'Patient'
                        
                    refresh = RefreshToken.for_user(user)
                    data = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token).encode().decode(),
                        'user_type': user_type,
                        'id': user_id,
                        'name': user_name
                    }
                    data.update(serialized_user.data)
                    return Response(data)
            return Response({
                        'status': 500,
                        'message': "Faild To login",
                    })
        except Exception as e:
             return Response({
                        'status': 500,
                        'message': "invalid serializer To login",
                    })




class LogoutView(generics.DestroyAPIView):
    """Delete token upon user logout"""
    serializer_class = LogoutSerializer
    authentication_classes = (
        authentication.TokenAuthentication,
        authentication.SessionAuthentication
    )  # auth class not required because set as default in settings
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        """Overriding for complex check and returns token"""
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Retrieving token: email={self.request.POST.get('email')}"
        )
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        obj = get_object_or_404(
            Token, user=user, key=serializer.validated_data['token']
        )

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
