from rest_framework import viewsets
from core.serializers import AssignmentSerializer
from core.models import Assignment


class AssignmenteViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
