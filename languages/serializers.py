from rest_framework import serializers

from . import models

# class LanguageSerializer(serializers.ModelSerializer):
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Languages
        fields = ('id', 'url', 'name', 'paradigm')
