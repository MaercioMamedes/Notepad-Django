from rest_framework import generics
from core.serializers import NoteListSerializer
from core.models import Note


class NoteListScheduleViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Note.objects.filter(urgency=False).filter(important=True)
        return queryset

    serializer_class = NoteListSerializer
