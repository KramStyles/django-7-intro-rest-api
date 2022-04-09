from operator import mod
from django.db import models

class Languages(models.Model):
    name = models.CharField(max_length=100)
    paradigm = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
