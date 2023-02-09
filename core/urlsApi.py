from rest_framework import routers
from core.apiViews import UserViewSet, CategoryViewSet, NoteViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register('category', CategoryViewSet, basename='Category')
router.register('note', NoteViewSet, basename='Note')
