from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    finished = models.BooleanField()
    order = models.IntegerField()
