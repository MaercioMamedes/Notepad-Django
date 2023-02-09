from django.db import models
from core.models import Category
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Título', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    urgency = models.BooleanField('Urgente', default=False)
    important = models.BooleanField('Importante', default=False)
    created_in = models.DateTimeField('criado em', editable=False, auto_now_add=True)
    modified = models.DateTimeField('modificado em', editable=True, auto_now=True)
    content = models.TextField('conteúdo')

    def __str__(self):
        return self.title

