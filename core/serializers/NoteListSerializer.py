from rest_framework import serializers
from core.models import Note


class NoteListSerializer(serializers.ModelSerializer):
    note_content = serializers.ReadOnlyField()

    class Meta:
        model = Note
        fields = '__all__'
