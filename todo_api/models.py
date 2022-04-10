from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500, null=True, default=None)
    finished = models.BooleanField(null=True, default=None)
    order = models.IntegerField(null=True, default=None)
