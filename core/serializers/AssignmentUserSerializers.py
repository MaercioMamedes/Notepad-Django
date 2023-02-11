from rest_framework import serializers
from core.models import Assignment


class AssignmentUserSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.first_name')
    note = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ['user_name', 'note']

    @staticmethod
    def get_note(obj):

        return {
            'id': obj.note.id,
            'title':obj.note.title,
        }
