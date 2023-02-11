from rest_framework import routers
from core.apiViews import UserViewSet, CategoryViewSet, NoteViewSet, AssignmenteViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='User')
router.register('category', CategoryViewSet, basename='Category')
router.register('note', NoteViewSet, basename='Note')
router.register('assignment', AssignmenteViewSet, basename='Assignment')

