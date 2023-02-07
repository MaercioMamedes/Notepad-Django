from rest_framework import serializers
from django.contrib.auth.models import User

"""Verificar método para gerar uma senha a partir de uma requisição post"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

