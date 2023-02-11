from rest_framework import generics
from core.serializers import AssignmentUserSerializer
from core.models import Assignment


class AssignmentListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Assignment.objects.filter(assigned_to=self.kwargs['user_id'])
        return queryset

    serializer_class = AssignmentUserSerializer
