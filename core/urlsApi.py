from rest_framework import routers
from core.apiViews import UserViewSet, CategoryViewSet, NoteViewSet, AssignmentViewSet


router = routers.DefaultRouter()
router.register('usuarios', UserViewSet, basename='User')
router.register('categoria', CategoryViewSet, basename='Category')
router.register('notas', NoteViewSet, basename='Note')
router.register('atribuicao', AssignmentViewSet, basename='Assignment')

