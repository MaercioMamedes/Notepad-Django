from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Nome da categoria', max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
