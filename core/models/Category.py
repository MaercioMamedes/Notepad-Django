from django.db import models


class Category(models.Model):
    name = models.CharField('Nome da categoria', max_length=20)
