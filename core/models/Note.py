from django.db import models
from core.models import Category


class Note(models.Model):
    title = models.CharField('Título', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField('conteúdo')

