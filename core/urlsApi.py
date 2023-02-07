from rest_framework import routers
from django.urls import path
from core.apiViews import UserViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
