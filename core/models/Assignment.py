from django.db import models
from django.contrib.auth.models import User
from core.models import Note


class Assignment(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    
