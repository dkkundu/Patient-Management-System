"""API > urls.py"""
# DJANGO IMPORTS
from django.urls import path, include
# DRF IMPORTS
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# API IMPORTS
from core.api import views


# /api/... browsable drf api
app_name = 'api'

# https://www.django-rest-framework.org/api-guide/routers/
router = DefaultRouter()
router.register('users', views.UserViewSet)

# https://docs.djangoproject.com/en/3.1/topics/http/urls/
urlpatterns = [
    # profile
    path(
        'profiles/<int:pk>/image/',
        views.ImageUploadAPI.as_view(),
        name='profile-image'
    ),
    path('auth/login/', views.ObtainTokenView.as_view(), name='auth-login'),
    path(
        'auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/logout/', views.LogoutView.as_view(), name='auth-logout'),

    # router ------------------------------------------------------------------
    path('', include(router.urls)),
]
