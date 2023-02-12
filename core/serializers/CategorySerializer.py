from rest_framework import serializers
from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        name_category = data['name']
        categories = Category.objects.all()

        if categories.filter(name__icontains=name_category):
            raise serializers.ValidationError({'name': "Já existe uma categoria com esse nome"})

        return data
