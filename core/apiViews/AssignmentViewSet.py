from rest_framework import viewsets
from core.serializers import AssignmentSerializer
from core.models import Assignment


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
