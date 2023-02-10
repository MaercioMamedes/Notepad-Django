from rest_framework import generics
from core.serializers import NoteListSerializer
from core.models import Note


class NoteListDelegateViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Note.objects.filter(urgency=True).filter(important=False)
        return queryset

    serializer_class = NoteListSerializer
