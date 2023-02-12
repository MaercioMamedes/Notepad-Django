from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Nome da categoria', max_length=20, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
