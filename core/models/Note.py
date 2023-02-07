from django.db import models
from core.models import Category


class Note(models.Model):

    title = models.CharField('Título', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    urgency = models.BooleanField('Urgente', default=False)
    important = models.BooleanField('Importante', default=False)
    created_in = models.DateTimeField('criado em', editable=False)
    modified = models.DateTimeField('modificado em', editable=True)
    content = models.TextField('conteúdo')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        """Implementar método para garantir autalização da data da modificação"""
        pass
