from rest_framework import serializers

from . import models

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Languages
        fields = ('id', 'name', 'paradigm')
