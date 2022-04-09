from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers

class LanguageView(viewsets.ModelViewSet):
    queryset = models.Languages.objects.all()
    serializer_class = serializers.LanguageSerializer
