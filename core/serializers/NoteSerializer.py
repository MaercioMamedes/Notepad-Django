from rest_framework import serializers
from core.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        excludes = ['created_in', 'modified']
